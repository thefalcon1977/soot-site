from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from corporate.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin, AdminImageMixin):
    """
    Django admin customization for the Profile model.

    This admin class customizes the display, search, and filter capabilities
    for user profiles in the Django admin interface.
    """

    list_display = ("user", "get_user_full_name", "created_at", "modified_at")
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
