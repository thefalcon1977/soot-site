from corporate.models.site import SiteContent
from django.utils import timezone
from django.db.models import Q
from corporate.models import LiveStream

def site_content(request):
    """
    Provides site-wide footer content to all templates.
    """
    try:
        site_content = SiteContent.objects.first()  # Fetch the first (or only) site content entry
    except SiteContent.DoesNotExist:
        site_content = None  # If no site content exists, return None

    return {
        "site_content": site_content
    }


def live_stream_count(request):
    """
    Add the count of active or scheduled live streams to the template context.
    """
    count = LiveStream.objects.filter(
        Q(is_active=True) | Q(scheduled_at__gt=timezone.now())
    ).count()
    return {'live_stream_count': count}