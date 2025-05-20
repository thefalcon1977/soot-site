from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from corporate.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin, AdminImageMixin):
    """
    Django admin customization for the Gallery model.

    This admin class customizes the display, search, and filter capabilities
    for media galleries in the Django admin interface.
    """

    list_display = ("id", "created_at", "modified_at")
    search_fields = ("id",)
    list_filter = ("created_at", "modified_at")
    readonly_fields = ("created_at", "modified_at")
    save_on_top = True
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    fieldsets = (
        (
            _("Media"),
            {
                "fields": (
                    "image",
                    "alternate_text",
                    # "video",
                )
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": ("created_at", "modified_at"),
                "classes": ("collapse",),
            },
        ),
    )
