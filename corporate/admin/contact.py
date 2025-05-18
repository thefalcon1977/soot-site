from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from sage_tools.mixins.admins import ReadOnlyAdmin

from corporate.models import Contact


@admin.register(Contact)
class ContactAdmin(ReadOnlyAdmin):
    # List display
    list_display = ("full_name", "email", "phone_number", "subject", "created_at")

    # Detail view settings
    readonly_fields = ("created_at",)

    # Search
    search_fields = ("full_name", "email", "subject")

    # Filters
    list_filter = ("created_at",)

    # Ordering
    ordering = ("-created_at",)

    # Date hierarchy for easy navigation by date
    date_hierarchy = "created_at"

    # Fieldset to organize the form layout
    fieldsets = (
        (
            None,
            {
                "fields": ("full_name", "email", "phone_number", "subject", "message"),
                "description": _(
                    "These are the primary details of the contact request."
                ),
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": ("created_at",),
                "description": _("Automatically generated timestamp for the message."),
            },
        ),
    )

    # Display a custom empty value if the field is missing (especially useful for phone numbers)
    empty_value_display = "-empty-"
