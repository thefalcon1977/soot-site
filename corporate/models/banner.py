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
