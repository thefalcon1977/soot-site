from django import forms
from django.utils.translation import gettext_lazy as _

from corporate.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name", "email", "phone_number", "subject", "message"]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': _('Full Name'), 'class': 'form-control', 'type': 'text'}),
            'subject': forms.TextInput(attrs={'placeholder': _('Subject'), 'class': 'form-control', 'type': 'text'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"placeholder": _("Email Address"), "class": "form-control"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {"placeholder": _("Phone Number"), "class": "form-control"}
        )
        self.fields["message"].widget.attrs.update(
            {"placeholder": _("Your Message"), "class": "form-control", "rows": 4}
        )
