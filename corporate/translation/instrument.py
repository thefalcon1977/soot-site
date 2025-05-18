"""
Instrument Translation Option
"""
from modeltranslation.translator import TranslationOptions, register

from corporate.models import Instrument


@register(Instrument)
class InstrumentTranslationOptions(TranslationOptions):
    """
    Instrument Translation
    """

    fields = (
        "title",
        "description",
    )
