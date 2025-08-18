from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import translation
import jdatetime
from sage_tools.mixins.admins import ReadOnlyAdmin

from corporate.models import Contact


@admin.register(Contact)
class ContactAdmin(ReadOnlyAdmin):
    # List display
    list_display = ("full_name", "email", "phone_number", "subject", "created_at_jalali")

    # Detail view settings
    readonly_fields = ("created_at",)

    # Search
    search_fields = ("full_name", "email", "subject")

    # Filters
    list_filter = ("created_at",)

    # Ordering
    ordering = ("-created_at",)

    # Date hierarchy for easy navigation by date
    date_hierarchy = "created_at"

    # Fieldset to organize the form layout
    fieldsets = (
        (
            None,
            {
                "fields": ("full_name", "email", "phone_number", "subject", "message"),
                "description": _(
                    "These are the primary details of the contact request."
                ),
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": ("created_at",),
                "description": _("Automatically generated timestamp for the message."),
            },
        ),
    )

    # Display a custom empty value if the field is missing (especially useful for phone numbers)
    empty_value_display = "-empty-"
    
    def created_at_jalali(self, obj):
        """
        Display created_at in Jalali format for Persian locale.
        """
        if obj.created_at:
            if translation.get_language() == 'fa':
                # Convert to Jalali date
                jalali_datetime = jdatetime.datetime.fromgregorian(datetime=obj.created_at)
                return jalali_datetime.strftime('%Y/%m/%d %H:%M')
            else:
                # Return Gregorian format for other languages
                return obj.created_at.strftime('%Y-%m-%d %H:%M')
        return '-'
    
    created_at_jalali.short_description = _('Created At (Jalali)')
    created_at_jalali.admin_order_field = 'created_at'  # Allows column sorting
