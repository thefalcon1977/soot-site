from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib import messages

from corporate.models import Profile

User = get_user_model()


class ProfileDetailView(DetailView):
    """
    Display a user's profile information.
    """
    model = Profile
    template_name = "pages/profile/detail.html"
    context_object_name = "profile"
    
    def get_object(self, queryset=None):
        """
        Get the profile by username.
        """
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        profile, created = Profile.objects.get_or_create(user=user)
        return profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['page_title'] = f"{profile.user.get_full_name() or profile.user.username} - {_('Profile')}"
        context['meta_description'] = (
            profile.description.plain_text()[:160] if hasattr(profile.description, 'plain_text') and profile.description
            else _("View user profile and information.")
        )
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allow users to update their own profile.
    """
    model = Profile
    template_name = "pages/profile/edit.html"
    fields = ['description', 'picture']
    context_object_name = "profile"
    
    def get_object(self, queryset=None):
        """
        Get the current user's profile.
        """
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
    def get_success_url(self):
        """
        Redirect to the user's profile page after successful update.
        """
        return reverse_lazy('pages:profile-detail', kwargs={'username': self.request.user.username})
    
    def form_valid(self, form):
        """
        Add success message when profile is updated.
        """
        messages.success(self.request, _('Your profile has been updated successfully.'))
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Edit Profile')
        context['meta_description'] = _('Update your profile information and settings.')
        return context