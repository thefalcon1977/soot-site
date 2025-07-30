from django.apps import AppConfig


class CorporateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'corporate'
    verbose_name = 'Corporate'
    label = 'corporate'

    def ready(self):
        import corporate.signals
