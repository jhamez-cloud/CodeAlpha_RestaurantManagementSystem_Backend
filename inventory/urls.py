from rest_framework.routers import DefaultRouter
from .api.viewsets import InventoryViewset

router = DefaultRouter()
router.register(r'inventory',InventoryViewset,basename='inventory')

urlpatterns = router.urls