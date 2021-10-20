from django.db import models
from django.utils.translation import gettext_lazy as _

# Let models be here
from project_crudname.core.models import AbstractChoice


class Crudname(AbstractChoice):
    """
        Model Crudname
    """

    class Meta:
        db_table = 'crudname'
        verbose_name = _('crudname')
        verbose_name_plural = _('crudnames')
        ordering = ['id']

    def __str__(self):
        return self.name
