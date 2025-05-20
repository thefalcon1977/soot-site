from django.urls import path
from django.contrib.auth.views import LogoutView
from corporate import views

app_name = "pages"

urlpatterns = [
    # Home
    path("", views.HomeView.as_view(), name="home"),
    
    # Authentication
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
    # Blog
    path("blog/", views.PostListView.as_view(), name="blog-post-list"),
    path("blog/<slug:slug>/", views.PostDetailView.as_view(), name="blog-post-detail"),
    
    # Instruments
    path("instruments/", views.InstrumentListView.as_view(), name="instruments-list"),
    path("instruments/<slug:slug>/", views.InstrumentDetailView.as_view(), name="instrument-detail"),
    
    # Live Streams
    path("live-streams/", views.LiveStreamListView.as_view(), name="live-stream-list"),
    path("live-streams/<slug:slug>/", views.LiveStreamDetailView.as_view(), name="live-stream-detail"),
    
    # Gallery
    path("gallery/", views.GalleryListView.as_view(), name="gallery-list"),
    
    # Contact
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
    
    # Instructors
    path("instructors/", views.InstructorList.as_view(), name="instructor-list"),
    path("instructors/<int:id>/", views.InstructorDetail.as_view(), name="instructor-detail"),
]