from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

try:
    from sorl.thumbnail.fields import ImageField
except ImportError:
    raise ImportError(
        "Install `sorl-thumbnail` package. Run `pip install sorl-thumbnail`."
    )

from sage_tools.mixins.models.abstract import PictureOperationAbstract
from sage_tools.mixins.models.base import TimeStampMixin, TitleSlugDescriptionMixin


class Instrument(TitleSlugDescriptionMixin, PictureOperationAbstract, TimeStampMixin):
    """
    Represents a musical instrument in the system.
    """

    description = CKEditor5Field(
        _("Description"),
        help_text=_(
            "Provide a detailed description of the musical instrument, including features and specifications."
        ),
        db_comment="Stores the detailed description of the instrument.",
    )

    image = ImageField(
        _("Instrument Image"),
        upload_to="music/instruments/",
        help_text=_("Upload an image of the musical instrument."),
        db_comment="Image representing the musical instrument.",
    )

    instructors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        verbose_name=_("Instructors"),
        related_name="musical_instruments",
        help_text=_("Select users who are instructors and associated with this instrument."),
        limit_choices_to={"groups__name": "instructor"},
        db_comment="Many-to-many relationship with users who belong to the 'Instructor' group.",
    )

    class Meta:
        """
        Meta options for the Instrument model.
        """

        verbose_name = _("Instrument")
        verbose_name_plural = _("Instruments")
        db_table = "musical_instruments"
        db_table_comment = "Table storing different types of musical instruments."

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        """
        Developer-friendly string representation of the Instrument instance.
        """
        return f"<Instrument: {self.title}>"
