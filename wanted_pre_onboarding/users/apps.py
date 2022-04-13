from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "wanted_pre_onboarding.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import wanted_pre_onboarding.users.signals  # noqa F401
        except ImportError:
            pass
