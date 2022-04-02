from django.apps import AppConfig


class PollsConfig(AppConfig):  # type: ignore
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "polls"
