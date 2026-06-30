from config.viewsets import StandardViewset
from rest_framework.permissions import AllowAny
from reservation.serializers import ReservationSerializer
from reservation.models import Reservation

class ReservationViewset(StandardViewset):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (AllowAny,)