from django import template
from django.utils import translation
from django.http import QueryDict
from django.utils.timezone import now
from django.utils.timesince import timesince

import jdatetime
from urllib.parse import urlencode, unquote

register = template.Library()


@register.simple_tag
def url_with_params(request, key, value):
    query_params = request.GET.copy()
    query_params[key] = value
    return query_params.urlencode()

@register.filter
def format_date(value):
    if translation.get_language() == 'fa':
        jalali_date = jdatetime.date.fromgregorian(date=value)
        return jalali_date.strftime('%Y/%m/%d')
    else:
        return value.strftime('%Y-%m-%d')

@register.simple_tag
def multiple_url_with_params(request, key, value):
    query_params = request.GET.copy()
    if query_params.get(key):
        existing_values = query_params.get(key).split(',')
        if value in existing_values:
            existing_values.remove(value)
        else:
            existing_values.append(value)
        query_params[key] = ','.join(existing_values)
    else:
        query_params[key] = value
    
    # Encode the query parameters and then replace '%2C' with ','
    return unquote(query_params.urlencode())


@register.filter
def split(string, key):
    """
    Returns a list of the string split by the key
    """
    return string.split(key)


@register.filter(name="replace_space_to")
def replace_space_to(value, replace_to):
    """Converts a string to lowercase and replaces spaces with underscores."""
    return value.replace(" ", replace_to)


@register.filter(name="replace_to")
def replace_to(value, args):
    """
    Replaces occurrences of a specified character in a string with the given replacement string.
    The args parameter should contain the character to replace and the replacement character, 
    separated by a comma. If only one argument is provided, it defaults to replacing spaces.

    :param value: The string in which to replace characters.
    :param args: A string containing the character to replace and the replacement character,
                 separated by a comma.
    :return: The modified string with specified characters replaced.
    """
    # Split the args on comma to get the character to replace and the replacement
    args_list = args.split(',')
    char_to_replace = args_list[0] if args_list else ' '
    replace_to = args_list[1] if len(args_list) > 1 else '_'

    return value.replace(char_to_replace, replace_to)


@register.filter(name="comma_to_amp")
def comma_to_amp(value):
    values_list = value.split(",")
    if len(values_list) > 2:
        return ", ".join(values_list[:-1]) + " & " + values_list[-1]
    else:
        return " & ".join(values_list)


@register.filter(name="name_or_hex")
def name_or_hex(value, arg):
    """Distinguishes between a name and its hex value based on the given argument."""
    parts = value.split("-")
    name = parts[0].strip()
    hex_value = (
        parts[1].strip() if len(parts) > 1 else "#000000"
    )  # Default to black if no hex value is provided

    if arg == "name":
        return name
    elif arg == "hex":
        return hex_value
    else:
        return value  # Return the original value if the argument doesn't match


@register.filter
def keyvalue(dict, arg):
    """Update or insert a key-value pair into a dictionary."""
    key, value = arg.split("|", 1)
    dict[key] = value
    return dict


@register.filter
def get(dict, key):
    """Retrieve value from dictionary by key."""
    return dict.get(key)


@register.filter(name="split")
def split(value, arg):
    """Split a string by a delimiter to produce a list."""
    return value.split(arg)


@register.filter
def remove(urlencoded, filter_to_remove):
    query_list = urlencoded.split("&")
    updated_query_list = [
        query for query in query_list if not query.startswith(filter_to_remove)
    ]
    return "&".join(updated_query_list)


@register.filter
def update_query_parameter(url, page_number):
    qd = QueryDict("", mutable=True)
    qd.update(url)
    qd["page"] = str(page_number)
    return qd.urlencode(safe=",:")


@register.filter(name='format_date')
def format_date(value):
    if translation.get_language() == 'fa':
        # Convert to Jalali and format
        jalali_date = jdatetime.date.fromgregorian(date=value)
        return jalali_date.strftime('%Y/%m/%d')  # Example format
    else:
        # Format Gregorian date
        return value.strftime('%Y-%m-%d')


@register.filter(name='in_range')
def in_range(value):
    """
    Creates a range of numbers for iteration in templates based on the input value.

    :param value: The maximum number of the range (exclusive)
    :return: A range object from 1 to value
    """
    return range(1, value + 1)


@register.filter
def get_field(form, field_name):
    return form[field_name]


@register.filter(name='yesno_bool')
def yesno_bool(value):
    return "Yes" if value else "No"


@register.filter
def get(dict, key):
    """Retrieve value from dictionary by key."""
    return dict.get(key, "")

@register.filter(name='has_group')
def has_group(user, group_name):
    if not user.is_authenticated:
        return False
    return user.groups.filter(name__iexact=group_name).exists()


@register.filter()
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


@register.filter(name='range')
def get_range(value):
    """
    Returns a range for iteration in the template.
    Usage: {% for i in 10|range %}
    """
    return range(value)

@register.filter
def multiply(value, arg):
    """Multiplies the value by the given argument."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def percentage(part, total):
    """Perceng"""
    try:
        return (int(part) / int(total)) * 100 if total > 0 else 0
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def created_at_display(value):
    """Formats the created_at field."""
    if not value:
        return "Unknown time"

    relative_time = timesince(value, now=now())
    exact_time = value.strftime("%d.%m.%Y at %I:%M %p")
    return f"{relative_time} ago ({exact_time})"

@register.filter
def relative_time_display(value):
    """
    Returns the relative time (e.g., '3 days ago') for a given datetime.
    """
    if not value:
        return "Unknown time"
    return f"{timesince(value, now=now())} ago"

@register.filter
def exact_time_display(value):
    """
    Returns the exact formatted time (e.g., '12.10.2023 at 03:45 PM') for a given datetime.
    """
    if not value:
        return "Unknown time"
    return value.strftime("%d.%m.%Y at %I:%M %p")


@register.filter
def bytes_to_mb(value):
    """Converts a size in bytes to megabytes (MB)."""
    try:
        value = int(value)
        return f"{value / (1024 * 1024):.2f} MB"
    except (ValueError, TypeError):
        return "0.00 MB"
