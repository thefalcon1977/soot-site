from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.translation import gettext_lazy as _

from corporate.models import SiteContent


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin, AdminImageMixin):
    """
    Administrator Panel for SiteContent.
    Provides an interface for managing site content, including contact details, footer information, and branding.
    """
    save_on_top = True

    fieldsets = (
        (
            _( "General Information"),
            {
                "fields": (
                    "brand_name",
                    "phone_number",
                    "email",
                    "site_logo",
                )
            },
        ),
        (
            _( "Footer Information"),
            {
                "fields": (
                    "footer_description",
                    "footer_copyright",
                )
            },
        ),
        (
            _( "Meta Information"),
            {
                "classes": ("collapse",),
                "fields": ("created_at", "modified_at"),
            },
        ),
    )

    list_display = (
        "brand_name",
        "phone_number",
        "email",
        "created_at",
        "modified_at",
    )

    list_filter = (
        "created_at",
        "modified_at",
    )

    search_fields = (
        "brand_name",
        "phone_number",
        "email",
    )

    readonly_fields = ("created_at", "modified_at")

    ordering = ("created_at",)

    list_per_page = 20

    list_select_related = True