from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    full_name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=255,
        help_text=_("Please enter your full name."),
        db_comment=_("The full name of the person submitting the contact form."),
    )
    email = models.EmailField(
        verbose_name=_("Email Address"),
        help_text=_("Please enter a valid email address."),
        db_comment=_("The email address of the person submitting the contact form."),
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        blank=True,
        region="IR",
        help_text=_("Please enter a valid phone number."),
        db_comment=_("The phone number of the person submitting the contact form."),
    )
    subject = models.CharField(
        verbose_name=_("Subject"),
        max_length=255,
        help_text=_("Please enter the subject of your message."),
        db_comment=_("The subject of the contact request."),
    )
    message = models.TextField(
        verbose_name=_("Message"),
        help_text=_("Please enter your message."),
        db_comment=_("The main body of the contact request."),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Date Created"),
        auto_now_add=True,
        help_text=_("The date and time when the contact form was submitted."),
        db_comment=_("Timestamp when the contact form was submitted."),
    )

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        ordering = ["-created_at"]
        db_table = "contact_messages"
        db_table_comment = _(
            "Table storing contact messages submitted via the website."
        )

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    def __repr__(self):
        return f"<Contact(full_name='{self.full_name}', email='{self.email}', subject='{self.subject}')>"
