from django.urls import reverse_lazy, reverse

from django.contrib.auth.views import LoginView as DjangoLoginView


class LoginView(DjangoLoginView):
    template_name = "pages/auth/login.html"
    success_url = reverse_lazy("pages:home")
    redirect_authenticated_user = False

    def get_success_url(self):
        return self.success_url