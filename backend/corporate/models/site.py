from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

try:
    from sorl.thumbnail.fields import ImageField
except ImportError:
    raise ImportError(
        "Install `sorl-thumbnail` package. Run `pip install sorl-thumbnail`."
    )

from sage_tools.mixins.models.base import TimeStampMixin
from sage_tools.mixins.models.abstract import PictureOperationAbstract


class SiteContent(PictureOperationAbstract, TimeStampMixin):
    """
    Represents the general site content, including contact details and footer information.
    """

    phone_number = models.CharField(
        max_length=20,
        verbose_name=_("Phone Number"),
        help_text=_("Enter the contact phone number."),
        db_comment="Stores the site's contact phone number."
    )

    email = models.EmailField(
        verbose_name=_("Email"),
        help_text=_("Enter the contact email address."),
        db_comment="Stores the site's contact email address."
    )

    footer_description = CKEditor5Field(
        _( "Footer Description"),
        help_text=_("Provide a description or additional information for the footer."),
        db_comment="Stores the footer description content."
    )

    footer_copyright = models.CharField(
        max_length=255,
        verbose_name=_("Footer Copyright"),
        help_text=_("Enter the copyright text to be displayed in the footer."),
        db_comment="Stores the copyright information displayed in the site footer."
    )

    brand_name = models.CharField(
        max_length=100,
        verbose_name=_("Brand Name"),
        help_text=_("Enter the brand or company name."),
        db_comment="Stores the site's brand or company name."
    )

    site_logo = ImageField(
        _( "Site Logo"),
        upload_to="site/logos/",
        help_text=_("Upload the logo of the site."),
        db_comment="Stores the site's logo image."
    )

    class Meta:
        """
        Meta options for the SiteContent model.
        """
        verbose_name = _( "Site Content")
        verbose_name_plural = _( "Site Contents")
        db_table = "site_content"
        db_table_comment = "Table storing general site content details such as contact information, footer text, and logo."

    def __str__(self):
        return f"{self.brand_name} - {self.phone_number}"

    def __repr__(self):
        """
        Developer-friendly string representation of the SiteContent instance.
        """
        return f"<SiteContent: {self.brand_name}>"
