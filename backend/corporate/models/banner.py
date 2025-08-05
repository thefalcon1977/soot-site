from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail.fields import ImageField

from sage_tools.mixins.models.abstract import PictureOperationAbstract
from sage_tools.mixins.models.base import TimeStampMixin


class Banner(TimeStampMixin, PictureOperationAbstract):
    """
    Banner Model - Represents a customizable banner element in the application.
    This model allows for the creation, modification, and display of banners with
    varying priorities and active states.
    """

    title = models.CharField(
        _("Title"),
        max_length=30,
        null=True,
        blank=True,
        help_text=_(
            "Enter the title of the banner. Keep it concise and informative. (Max 30 characters)"
        ),
        db_comment="The title of the banner; optional, max 110 characters.",
    )

    description = models.TextField(
        _("Description"),
        null=True,
        blank=True,
        help_text=_(
            "Enter a detailed description of the banner. This can include HTML tags."
        ),
        db_comment="A detailed description of the banner; optional, max 255 characters.",
    )

    picture = ImageField(
        _("Picture"),
        max_length=110,
        width_field="width_field",
        height_field="height_field",
        help_text=_(
            "Upload the banner image. Supported formats include JPG, PNG, etc."
        ),
        db_comment="Path to the banner image file, with details on dimensions.",
    )

    button = models.BooleanField(
        _("Button"),
        default=False,
        help_text=_(
            "Check this box if the banner should include a call-to-action button."
        ),
        db_comment="Indicates whether the banner includes a call-to-action button.",
    )

    button_text = models.CharField(
        _("Button Text"),
        max_length=30,
        null=True,
        blank=True,
        help_text=_(
            "Enter the text for the call-to-action button. Keep it concise and informative. (Max 30 characters)"
        ),
        db_comment="The text on the call-to-action button; optional, max 30 characters.",
    )

    button_link = models.URLField(
        _("Button Link"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Enter the URL for the call-to-action button. Make sure it's a valid URL starting with http:// or https://."
        ),
        db_comment="The URL for the call-to-action button; optional, max 255 characters.",
    )

    objects = models.Manager()

    class Meta:
        """
        Meta Information
        """

        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)
