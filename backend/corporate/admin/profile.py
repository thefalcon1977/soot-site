from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from corporate.models import Profile

from django.utils import translation
import jdatetime


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin, AdminImageMixin):
    """
    Django admin customization for the Profile model.

    This admin class customizes the display, search, and filter capabilities
    for user profiles in the Django admin interface.
    """

    list_display = ("user", "get_user_full_name", "created_at_jalali", "modified_at_jalali")
    search_fields = ("user__username", "user__first_name", "user__last_name")
    list_filter = ("created_at", "modified_at")
    readonly_fields = ("created_at", "modified_at")
    save_on_top = True
    autocomplete_fields = ("user",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    fieldsets = (
        (
            _("User Information"),
            {"fields": ("user",)},
        ),
        (
            _("Profile Details"),
            {
                "fields": (
                    "description",
                    "picture",
                    "alternate_text",
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

    @staticmethod
    @admin.display(description=_("Full Name"))
    def get_user_full_name(obj):
        return obj.user.get_full_name() or obj.user.username

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("user")


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