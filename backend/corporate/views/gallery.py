from django.views.generic import DetailView, ListView
from corporate.models import Gallery


class GalleryListView(ListView):
    model = Gallery
    template_name = "pages/gallery.html"
    context_object_name = "galleries"
    page_title = "Gallery"
