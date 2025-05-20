from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

try:
    from sorl.thumbnail.fields import ImageField
except ImportError:
    raise ImportError(
        "Install `sorl-thumbnail` package. Run `pip install sorl-thumbnail`."
    )

from sage_tools.mixins.models.base import TimeStampMixin
from sage_tools.mixins.models.abstract import PictureOperationAbstract


class Gallery(PictureOperationAbstract, TimeStampMixin):
    """
    Represents a media gallery containing pictures and videos.
    """

    image = ImageField(
        _("Image"),
        upload_to="gallery/images/",
        blank=True,
        null=True,
        help_text=_("Upload an image for the gallery."),
        db_comment="Stores images in the gallery.",
    )

    # video = models.FileField(
    #     _("Video"),
    #     upload_to="gallery/videos/",
    #     blank=True,
    #     null=True,
    #     help_text=_("Upload a video for the gallery."),
    #     db_comment="Stores videos in the gallery.",
    # )

    class Meta:
        """
        Meta options for the Gallery model.
        """

        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")
        db_table = "gallery"
        db_table_comment = "Table storing images and videos uploaded by users."

    def __str__(self):
        return f"Gallery Item {self.pk}"

    def __repr__(self):
        """
        Developer-friendly string representation of the Gallery instance.
        """
        return f"<Gallery: {self.pk}>"
