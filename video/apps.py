from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'

    def ready(self):
        import video.signals
