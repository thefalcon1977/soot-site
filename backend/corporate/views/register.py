from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect

from corporate.forms.user import UserCreationForm


class RegisterView(CreateView):
    template_name = "pages/auth/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("pages:login")

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())
