from typing import Any

from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView


User = get_user_model()


class InstructorList(ListView):

    template_name = "teachers/list.html"
    model = User
    context_object_name = "instructors"
    page_title = "Instructors"
    queryset = User.objects.filter(groups__name='instructor').select_related('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InstructorDetail(DetailView):

    template_name = "teachers/detail.html"
    model = User
    page_title = "Instructors"
    context_object_name = "instructor"
    queryset = (
        User.objects.filter(groups__name='instructor')
        .select_related('profile')
        )
    slug_field = 'id'
    slug_url_kwarg = 'id'

