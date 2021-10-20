from rest_framework.routers import DefaultRouter

from project_crudname.apps.crudname.views import CrudnameViewSet

app_name = "crudname"

router = DefaultRouter()
router.register(r'crudname', CrudnameViewSet)

urlpatterns = router.urls
