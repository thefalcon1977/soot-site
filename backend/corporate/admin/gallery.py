from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from corporate.models import Gallery
from django.utils import translation
import jdatetime



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin, AdminImageMixin):
    """
    Django admin customization for the Gallery model.

    This admin class customizes the display, search, and filter capabilities
    for media galleries in the Django admin interface.
    """

    list_display = ("id", "created_at_jalali", "modified_at_jalali")
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
    
    def modified_at_jalali(self, obj):
        """
        Display modified_at in Jalali format for Persian locale.
        """
        if obj.modified_at:
            if translation.get_language() == 'fa':
                # Convert to Jalali date
                jalali_datetime = jdatetime.datetime.fromgregorian(datetime=obj.modified_at)
                return jalali_datetime.strftime('%Y/%m/%d %H:%M')
            else:
                # Return Gregorian format for other languages
                return obj.modified_at.strftime('%Y-%m-%d %H:%M')
        return '-'
    
    modified_at_jalali.short_description = _('Modified At (Jalali)')
    modified_at_jalali.admin_order_field = 'modified_at'  # Allows column sorting