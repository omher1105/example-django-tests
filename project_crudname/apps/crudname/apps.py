from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CrudnameConfig(AppConfig):
    name = "project_crudname.apps.crudname"
    verbose_name = _("Crudname")

    def ready(self):
        try:
            import project_crudname.apps.crudname.signals  # noqa F401
        except ImportError:
            pass
