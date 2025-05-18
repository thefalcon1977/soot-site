from django.urls import path, re_path
from corporate import views
from django.contrib.auth.views import LogoutView

app_name = "pages"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    re_path(
        r"^$",
        views.HomeView.as_view(),
        name="home"
    ),
    re_path(
        r"^blog/(?P<slug>[-\w]+)/$",
        views.PostDetailView.as_view(),
        name="blog-post-detail"
    ),
    re_path(
        r"^blog/$",
        views.PostListView.as_view(),
        name="blog-post-list"
    ),
    re_path(
        r"^instruments/(?P<slug>[-\w]+)/$",
        views.InstrumentDetailView.as_view(),
        name="instrument-detail"
    ),
    re_path(
        r"^instruments/$",
        views.InstrumentListView.as_view(),
        name="instruments-list"
    ),
    re_path(
        r"^gallery/$",
        views.GalleryListView.as_view(),
        name="gallery-list"
    ),
    re_path(
        r"^contact/$",
        views.ContactCreateView.as_view(),
        name="contact"
    ),
    re_path(
        r"^instructors/$",
        views.InstructorList.as_view(),
        name="instructor-list"
    ),
    re_path(
        r'^instructors/(?P<id>\d+)/$',
        views.InstructorDetail.as_view(),
        name='instructor-detail'
    ),
]
