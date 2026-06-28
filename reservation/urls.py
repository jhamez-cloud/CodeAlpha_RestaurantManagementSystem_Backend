from rest_framework.routers import DefaultRouter
from .api.viewsets import ReservationViewset

router = DefaultRouter()
router.register(r'reservation',ReservationViewset,basename='reservations')

urlpatterns = router.urls