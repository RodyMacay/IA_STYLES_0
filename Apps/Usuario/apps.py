from django.apps import AppConfig


class RegistroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.Usuario'

    def ready(self):
        import Apps.Usuario.signals
