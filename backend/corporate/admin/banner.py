from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.translation import gettext_lazy as _
from sage_tools.mixins.admins import LimitOneInstanceAdminMixin

from corporate.models import Banner


@admin.register(Banner)
class BannerAdmin(LimitOneInstanceAdminMixin, AdminImageMixin):
    """
    Administrator Panel for Banner.
    Provides a detailed and user-friendly interface for managing banners,
    including fields for title, subtitle, image, and priority settings.
    """
    save_on_top = True

    fieldsets = (
        (
            _( "Banner Information"),
            {
                "fields": (
                    "title",
                    "picture",
                    "alternate_text",
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
        "title",
        "created_at",
        "modified_at",
    )

    list_filter = (
        "created_at",
        "modified_at",
    )

    search_fields = (
        "title",
    )

    readonly_fields = ("created_at", "modified_at")

    ordering = ("created_at",)

    list_per_page = 20

    list_select_related = True
