from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from corporate.models import LiveStream


@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the LiveStream model.
    """
    list_display = ('title', 'slug', 'is_active', 'scheduled_at', 'status', 'thumbnail')
    list_filter = ('is_active', 'scheduled_at')
    search_fields = ('title', 'slug', 'description')
    date_hierarchy = 'scheduled_at'
    ordering = ('-is_active', '-scheduled_at', 'title')
    readonly_fields = ('status', 'created_at', 'modified_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
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
            thumb = get_thumbnail(obj.image, '100x100', crop='center', format='WEBP')
            return f'<img src="{thumb.url}" alt="{obj.alternate_text or obj.title}" style="max-width: 100px; max-height: 100px;">'
        return 'No Image'
    thumbnail.allow_tags = True
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