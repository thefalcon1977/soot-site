from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.utils import translation
import jdatetime
from corporate.models import LiveStream


@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the LiveStream model.
    """
    list_display = ('card_title', 'slug', 'is_active', 'scheduled_at_jalali', 'status', 'thumbnail')
    list_filter = ('is_active', 'scheduled_at')
    search_fields = ('card_title', 'slug', 'description')
    date_hierarchy = 'scheduled_at'
    ordering = ('-is_active', '-scheduled_at', 'title')
    readonly_fields = ('stream_url', 'status', 'created_at', 'modified_at')
    fieldsets = (
        (None, {
            'fields': ('card_title', 'title', 'description')
        }),
        (_('Image'), {
            'fields': ('image',)
        }),
        (_('Stream Details'), {
            'fields': ('stream_url', 'is_active', 'scheduled_at', 'status')
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',)
        }),
    )

    def thumbnail(self, obj):
        """
        Display a thumbnail of the live stream image in the admin list view.
        """
        if obj.image:
            from sorl.thumbnail import get_thumbnail
            thumb = get_thumbnail(obj.image, '75x50', crop='center', format='WEBP')
            return format_html(
                '<img src="{}" alt="{}" style="max-width: 75px; max-height: 50px;">',
                thumb.url,
                obj.alternate_text or obj.title or 'Thumbnail'
            )
        return 'No Image'
    
    thumbnail.short_description = _('Thumbnail')

    def get_queryset(self, request):
        """
        Optimize queryset by ordering consistently with the list view.
        """
        return super().get_queryset(request).order_by('-is_active', '-scheduled_at', 'title')

    def get_readonly_fields(self, request, obj=None):
        """
        Include slug as readonly when editing an existing object.
        """
        if obj:  # Editing an existing object
            return self.readonly_fields + ('slug',)
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        """
        Only prepopulate slug for new objects if it's editable.
        """
        if obj:  # Editing an existing object
            return {}
        return {'slug': ('title',)} if 'slug' in self.model._meta.get_fields() and self.model._meta.get_field('slug').editable else {}
    
    def scheduled_at_jalali(self, obj):
        """
        Display scheduled_at in Jalali format for Persian locale.
        """
        if obj.scheduled_at:
            if translation.get_language() == 'fa':
                # Convert to Jalali date
                jalali_datetime = jdatetime.datetime.fromgregorian(datetime=obj.scheduled_at)
                return jalali_datetime.strftime('%Y/%m/%d %H:%M')
            else:
                # Return Gregorian format for other languages
                return obj.scheduled_at.strftime('%Y-%m-%d %H:%M')
        return '-'
    
    scheduled_at_jalali.short_description = _('Scheduled Time (Jalali)')
    scheduled_at_jalali.admin_order_field = 'scheduled_at'  # Allows column sorting

    def scheduled_at_display(self, obj):
        """
        Display both Gregorian and Jalali dates.
        """
        if obj.scheduled_at:
            gregorian = obj.scheduled_at.strftime('%Y-%m-%d %H:%M')
            jalali_datetime = jdatetime.datetime.fromgregorian(datetime=obj.scheduled_at)
            jalali = jalali_datetime.strftime('%Y/%m/%d %H:%M')
            return format_html(
                '<div>🗓️ {}<br/>📅 {}</div>',
                gregorian,
                jalali
            )
        return '-'
    
    scheduled_at_display.short_description = _('Scheduled Time')
    scheduled_at_display.admin_order_field = 'scheduled_at'