from config.viewsets import StandardViewset
from reservation.serializers import ReservationSerializer
from reservation.models import Reservation

class ReservationViewset(StandardViewset):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer