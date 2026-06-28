from rest_framework.routers import DefaultRouter
from .api.viewsets import OrderItemViewset,OrderViewset

router = DefaultRouter()
router.register(r'order-item',OrderItemViewset,basename='orderitem')
router.register(r'order',OrderViewset,basename='order')

urlpatterns = router.urls