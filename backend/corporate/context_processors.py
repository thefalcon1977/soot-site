from corporate.admin import socialmedia
from corporate.models.site import SiteContent
from django.utils import timezone
from django.db.models import Q
from corporate.models import LiveStream, SocialMediaBadge


def site_content(request):
    """
    Provides site-wide footer content to all templates.
    """
    try:
        # Fetch the first (or only) site content entry
        site_content = SiteContent.objects.first()
        socialmedia_badges = SocialMediaBadge.objects.filter(is_active=True)
    except SiteContent.DoesNotExist:
        site_content = None  # If no site content exists, return None

    return {
        "site_content": site_content,
        "favicon_url": site_content.site_logo.url if site_content and site_content.site_logo else "/static/assets/images/icon/logo.png",
        "socialmedia_badges": socialmedia_badges,
    }


def live_stream_count(request):
    """
    Add the count of active or scheduled live streams to the template context.
    """
    count = LiveStream.objects.filter(
        Q(is_active=True) | Q(scheduled_at__gt=timezone.now())
    ).count()
    return {'live_stream_count': count}


def site_meta(request):
    title = 'Default Site Title'
    a = site_content(request)
    favicon = a["favicon_url"]
    return {
        'page_title': title,
        'favicon_url': favicon,
    }
