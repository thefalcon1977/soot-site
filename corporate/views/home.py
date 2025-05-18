"""
Views
"""
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from corporate.models import Banner, Instrument, Gallery
from sage_blog.models import Post

User = get_user_model()


class HomeView(TemplateView):
    """
    Home View
    """

    template_name = "pages/index.html"
    page_title = "Home"
    newsletter_success_url_name = "pages:home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["instructors"] = User.objects.select_related("profile").filter(groups__name='instructor')[:4]
        context["instruments"] = Instrument.objects.all()[:4]
        context["galleries"] = Gallery.objects.all()[:4]
        context["banner"] = Banner.objects.first()
        context["recent_posts"] = Post.objects.join_category().filter_actives().filter_recent_posts(num_posts=4)
        return context


class AboutView(TemplateView):
    """
    About View
    """

    template_name = "pages/about.html"
    page_title = "About"
    newsletter_success_url_name = "pages:about"
