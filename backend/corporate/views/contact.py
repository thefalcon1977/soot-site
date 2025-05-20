from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from corporate.forms import ContactForm
from corporate.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "pages/contact.html"
    success_url = reverse_lazy("pages:contact")
    page_title = "Contact"

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")

        if form_type == "contact_form":
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Your message has been sent successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error with your submission. Please correct the errors below.",
        )
        return super().form_invalid(form)
