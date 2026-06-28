from rest_framework.routers import DefaultRouter
from .api.viewsets import TableViewset

router = DefaultRouter()
router.register(r'table',TableViewset,basename='tables')

urlpatterns = router.urls