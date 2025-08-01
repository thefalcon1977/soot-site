from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail.fields import ImageField

from sage_tools.mixins.models.abstract import PictureOperationAbstract
from sage_tools.mixins.models.base import TimeStampMixin


class SocialMediaBadge(TimeStampMixin, PictureOperationAbstract):
    """
    SocialMediaBadge Model - Represents a badge that users can earn or display on their social media profiles.
    This model supports badge creation with customizable names, images, and earning criteria.
    """

    name = models.CharField(
        _("Name"),
        max_length=50,
        help_text=_(
            "Enter the name of the badge. Keep it concise and descriptive. (Max 50 characters)"
        ),
        db_comment="The name of the badge; max 50 characters.",
    )

    image = ImageField(
        _("Badge Image"),
        max_length=110,
        width_field="width_field",
        height_field="height_field",
        help_text=_(
            "Upload the badge image. Supported formats include JPG, PNG, etc."
        ),
        db_comment="Path to the badge image file, with details on dimensions.",
    )

    description = models.TextField(
        _("Description"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_(
            "Provide a brief description of the badge and how it can be earned. (Max 200 characters)"
        ),
        db_comment="Description of the badge and its earning criteria; optional, max 200 characters.",
    )

    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Check this box if the badge is currently available for users to earn."
        ),
        db_comment="Indicates whether the badge is active and can be earned.",
    )

    criteria_link = models.URLField(
        _("Criteria Link"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Enter an optional URL for detailed badge earning criteria. Must start with http:// or https://."
        ),
        db_comment="Optional URL for badge earning criteria; max 255 characters.",
    )

    objects = models.Manager()

    class Meta:
        """
        Meta Information
        """
        verbose_name = _("Social Media Badge")
        verbose_name_plural = _("Social Media Badges")
        ordering = ['name']  # Order by badge name alphabetically

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<SocialMediaBadge id={self.id}, name={self.name}>"