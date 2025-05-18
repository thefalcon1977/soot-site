from django.views.generic import DetailView, ListView
from corporate.models import Instrument


class InstrumentListView(ListView):
    model = Instrument
    template_name = "instrument/list.html"
    context_object_name = "instruments"
    page_title = "Instruments"


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "instrument/detail.html"
    context_object_name = "instrument"
    page_title = "Instruments"

