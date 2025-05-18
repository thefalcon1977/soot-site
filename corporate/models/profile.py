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
from sage_tools.mixins.models.base import TimeStampMixin


class Profile(PictureOperationAbstract, TimeStampMixin):
    """
    Represents a user profile in the system.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="profile",
        help_text=_("The user associated with this profile."),
        db_comment="One-to-one relationship with the user model.",
    )

    description = CKEditor5Field(
        _("Description"),
        blank=True,
        help_text=_(
            "Provide a short biography or other relevant information about the user."
        ),
        db_comment="Stores the user's profile description.",
    )

    picture = ImageField(
        _("Profile Picture"),
        upload_to="profiles/pictures/",
        help_text=_("Upload a profile picture."),
        db_comment="Profile image representing the user.",
    )

    class Meta:
        """
        Meta options for the Profile model.
        """

        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        db_table = "user_profiles"
        db_table_comment = "Table storing user profile information."

    def __str__(self):
        return str(self.user.get_full_name() or self.user.username)

    def __repr__(self):
        """
        Developer-friendly string representation of the Profile instance.
        """
        return f"<Profile: {self.user.username}>"
