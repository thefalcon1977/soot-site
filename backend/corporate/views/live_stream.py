from django.views.generic import DetailView, ListView
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.utils import timezone
from corporate.models import LiveStream


class LiveStreamListView(ListView):
    """
    Displays a list of live streams, optionally filtered by active or scheduled status.
    """
    model = LiveStream
    template_name = "pages/live_stream/list.html"
    context_object_name = "liveStreams"
    paginate_by = 12  # Number of streams per page
    page_title = _("Live Streams")

    def get_queryset(self):
        """
        Returns live streams that are either active or scheduled, ordered by status and schedule.
        """
        now = timezone.now()
        return LiveStream.objects.filter(
            Q(is_active=True) | Q(scheduled_at__gt=now)
        ).order_by('-is_active', '-scheduled_at', 'title')

    def get_context_data(self, **kwargs):
        """
        Adds page title and meta description to the context for SEO.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['meta_description'] = _(
            "Explore our collection of live streams, including upcoming and currently active broadcasts."
        )
        return context


class LiveStreamDetailView(DetailView):
    model = LiveStream
    template_name = "pages/live_stream/detail.html"
    context_object_name = "liveStream"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        live_stream = self.get_object()
        context['page_title'] = f"{live_stream.title} - {_('Live Stream')}"
        context['meta_description'] = (
            live_stream.description.plain_text()[:160]
            if hasattr(live_stream.description, 'plain_text')
            else _("Watch this live stream and stay updated with the latest content.")
        )
        context['live_stream_count'] = LiveStream.objects.filter(
            Q(is_active=True) | Q(scheduled_at__gt=timezone.now())
        ).count()
        return context