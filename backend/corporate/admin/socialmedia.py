from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from corporate.models import SocialMediaBadge

from django.utils import translation
import jdatetime


@admin.register(SocialMediaBadge)
class SocialMediaBadgeAdmin(AdminImageMixin, admin.ModelAdmin):
    """
    Admin configuration for SocialMediaBadge model.
    Provides a user-friendly interface for managing social media badges.
    """

    list_display = ('name', 'is_active', 'created_at_jalali', 'modified_at_jalali', 'thumbnail')
    list_filter = ('is_active', 'created_at', 'modified_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'modified_at', 'thumbnail')
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'thumbnail')
        }),
        ('Details', {
            'fields': ('description', 'is_active', 'criteria_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',)
        }),
    )

    def thumbnail(self, obj):
        """Display a thumbnail of the badge image in the admin list view."""
        if obj.image:
            from sorl.thumbnail import get_thumbnail
            thumb = get_thumbnail(obj.image, '35x35', crop='center', format='WEBP')
            return format_html(
                '<img src="{}" alt="{}" style="max-width: 35px; max-height: 35px;">',
                thumb.url,
                obj.alternate_text or obj.name or 'Thumbnail'
            )
        return 'No Image'

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image Preview'

    def get_queryset(self, request):
        """Return the default queryset without select_related for non-relational fields."""
        return super().get_queryset(request)

    def save_model(self, request, obj, form, change):
        """Custom save to handle any additional logic if needed."""
        super().save_model(request, obj, form, change)


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