from corporate.models.site import SiteContent

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
