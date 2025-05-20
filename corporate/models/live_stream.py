from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.core.validators import URLValidator

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
    Represents a live stream entity in the system.
    
    This model stores information about live streams, including their title, description,
    image, and streaming URL. It inherits common functionality from mixins for timestamps,
    title/slug/description, and image operations.
    """

    description = CKEditor5Field(
        verbose_name=_("Description"),
        help_text=_(
            "Detailed description of the live stream, including content, features, and schedule."
        ),
        config_name="default",
        blank=True,
        db_comment="Stores the detailed rich-text description of the live stream."
    )

    image = ImageField(
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

    def __str__(self):
        """User-friendly string representation of the live stream."""
        return f"{self.title} ({'Active' if self.is_active else 'Inactive'})"

    def __repr__(self):
        """Developer-friendly string representation of the live stream."""
        return f"<LiveStream: {self.title} (ID: {self.pk})>"

    def is_scheduled(self):
        """Check if the live stream is scheduled for a future time."""
        from django.utils import timezone
        if self.scheduled_at:
            return self.scheduled_at > timezone.now()
        return False

    @property
    def status(self):
        """Return the current status of the live stream."""
        if self.is_active:
            return "Active"
        elif self.is_scheduled():
            return "Scheduled"
        return "Inactive"