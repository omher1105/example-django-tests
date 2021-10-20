from django.contrib import admin

# Register your models here.
from project_crudname.apps.crudname.models import Crudname
from project_crudname.core.admin import AuditAdminMixin


@admin.register(Crudname)
class CrudnameAdmin(AuditAdminMixin, admin.ModelAdmin):
    """
    Admin options for Learning model.
    """
    list_display = ['name']
