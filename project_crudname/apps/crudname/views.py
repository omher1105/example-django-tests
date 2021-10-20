from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from project_crudname.apps.crudname.models import Crudname
from project_crudname.apps.crudname.serializers import CrudnameSerializer


class CrudnameViewSet(ModelViewSet):
    """
        Viewset CrudnameViewSet
    """
    queryset = Crudname.objects.actives()
    serializer_class = CrudnameSerializer
    permission_classes = (AllowAny,)
