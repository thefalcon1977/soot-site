from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
from django_ckeditor_5.fields import CKEditor5Field

try:
    from sorl.thumbnail.fields import ImageField
except ImportError:
    raise ImportError(
        "Install `sorl-thumbnail` package. Run `pip install sorl-thumbnail`."
    )

from sage_tools.mixins.models.abstract import PictureOperationAbstract
from sage_tools.mixins.models.base import TimeStampMixin, TitleSlugDescriptionMixin


class LiveStream(TitleSlugDescriptionMixin, PictureOperationAbstract, TimeStampMixin):
    """
    Model representing a live stream event with metadata and scheduling.
    """
    description = CKEditor5Field(
        verbose_name=_("Description"),
        help_text=_("Detailed description of the live stream."),
        config_name="default",
        blank=True,
        db_comment="Rich-text description of the live stream."
    )

    if ImageField is not None:
        image = ImageField(
            verbose_name=_("Stream Image"),
            upload_to="live_streams/%Y/%m/",
            help_text=_("Upload a representative image or thumbnail for the live stream."),
            blank=True,
            null=True,
            db_comment="Image or thumbnail representing the live stream."
        )
    else:
        # Fallback for missing sorl-thumbnail
        image = models.ImageField(
            verbose_name=_("Stream Image"),
            upload_to="live_streams/%Y/%m/",
            help_text=_("Upload a representative image or thumbnail for the live stream."),
            blank=True,
            null=True,
            db_comment="Image or thumbnail representing the live stream."
        )

    stream_url = models.URLField(
        verbose_name=_("Stream URL"),
        max_length=255,
        validators=[URLValidator()],
        help_text=_("URL for accessing the live stream (e.g., YouTube, Twitch, or custom platform)."),
        blank=True,
        db_comment="URL where the live stream can be accessed."
    )

    visit = models.PositiveIntegerField(
        _("Visit"),
        default=0,
        db_comment="Number of times the live stream has been visited.",
        blank=True,
        null=True,
        help_text=_("Number of times the live stream has been visited.")
    )

    is_active = models.BooleanField(
        verbose_name=_("Is Active"),
        default=False,
        help_text=_("Indicates whether the live stream is currently active."),
        db_comment="Flag indicating if the live stream is currently active."
    )

    scheduled_at = models.DateTimeField(
        verbose_name=_("Scheduled Time"),
        null=True,
        blank=True,
        help_text=_("Optional scheduled start time for the live stream."),
        db_comment="Date and time when the live stream is scheduled to start."
    )

    alternate_text = models.CharField(
        verbose_name=_("Alternate Text"),
        max_length=255,
        blank=True,
        help_text=_("Alternative text for the live stream image, used for accessibility."),
        db_comment="Alternative text for the live stream image."
    )

    class Meta:
        verbose_name = _("live stream")
        verbose_name_plural = _("live streams")
        db_table = "live_streams"
        db_table_comment = "Table storing live stream records."
        ordering = ["-scheduled_at", "title"]
        indexes = [
            models.Index(fields=["slug"], name="live_stream_slug_idx"),
            models.Index(fields=["is_active"], name="live_stream_active_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.title} ({'Active' if self.is_active else 'Inactive'})"

    def __repr__(self) -> str:
        return f"<LiveStream: {self.title} (ID: {self.pk})>"

    def is_scheduled(self) -> bool:
        from django.utils import timezone
        return bool(self.scheduled_at and self.scheduled_at > timezone.now())

    @property
    def status(self) -> str:
        if self.is_active:
            return "Active"
        if self.is_scheduled():
            return "Scheduled"
        return "Inactive"
        