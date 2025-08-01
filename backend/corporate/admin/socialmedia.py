from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from corporate.models import SocialMediaBadge


@admin.register(SocialMediaBadge)
class SocialMediaBadgeAdmin(AdminImageMixin, admin.ModelAdmin):
    """
    Admin configuration for SocialMediaBadge model.
    Provides a user-friendly interface for managing social media badges.
    """

    list_display = ('name', 'is_active', 'created_at', 'modified_at', 'thumbnail')
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
            return '<img src="%s" style="max-width: 50px; max-height: 50px;" />' % obj.image.url
        return 'No Image'
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image Preview'

    def get_queryset(self, request):
        """Return the default queryset without select_related for non-relational fields."""
        return super().get_queryset(request)

    def save_model(self, request, obj, form, change):
        """Custom save to handle any additional logic if needed."""
        super().save_model(request, obj, form, change)