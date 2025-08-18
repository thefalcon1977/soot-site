from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.translation import gettext_lazy as _
from django.utils import translation
import jdatetime

from corporate.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin, AdminImageMixin):
    """
    Administrator Panel for Banner.
    Provides a detailed and user-friendly interface for managing banners,
    including fields for title, subtitle, image, and priority settings.
    """
    save_on_top = True

    fieldsets = (
        (
            _("Banner Information"),
            {
                "fields": (
                    "title",
                    "description",
                    "picture",
                    "button",
                    "button_text",
                    "button_link",
                    "alternate_text",
                )
            },
        ),
        (
            _("Meta Information"),
            {
                "classes": ("collapse",),
                "fields": ("created_at", "modified_at"),
            },
        ),
    )

    list_display = (
        "title",
        "created_at_jalali",
        "modified_at_jalali",
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
