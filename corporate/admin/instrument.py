from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from corporate.models import Instrument


@admin.register(Instrument)
class InstrumentAdmin(TabbedTranslationAdmin, AdminImageMixin):
    """
    Django admin customization for the Instrument model.

    This admin class customizes the display, search, and filter capabilities for instruments
    in the Django admin interface.
    """

    # Display settings
    list_display = ("title", "get_instructors", "created_at", "modified_at")
    list_filter = ("created_at", "modified_at")
    search_fields = ("title", "slug", "description", "instructors__username")
    filter_horizontal = ("instructors",)
    save_on_top = True
    autocomplete_fields = ("instructors",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "modified_at", "slug")

    fieldsets = (
        (
            _("Basic Information"),
            {"fields": ("title", "slug")},
        ),
        (
            _("Instrument Details"),
            {
                "fields": (
                    "description",
                    "image",
                    "alternate_text",
                )
            },
        ),
        (
            _("Instructor Assignment"),
            {
                "fields": ("instructors",),
                "description": _("Only users in the 'Instructor' group can be assigned."),
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": (
                    "created_at",
                    "modified_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    @staticmethod
    @admin.display(description=_("Instructors"))
    def get_instructors(obj):
        return ", ".join([user.get_full_name() for user in obj.instructors.all()])

    # Optimized queryset for better performance
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset
