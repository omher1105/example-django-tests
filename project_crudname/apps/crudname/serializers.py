from rest_framework import serializers
from .models import Crudname
from ...core.serializers import AuditSerializerMixin


class CrudnameSerializer(serializers.ModelSerializer):
    """
        Serializer crudname
    """
    class Meta(AuditSerializerMixin.Meta):
        model = Crudname
