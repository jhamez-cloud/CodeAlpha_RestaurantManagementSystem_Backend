from rest_framework import serializers
from .models import Reservation
from table.serializers import TableSerializer

class ReservationSerializer(serializers.ModelSerializer):
    table = serializers.ReadOnlyField(source='table.table_id')
    class Meta:
        model = Reservation
        fields = ['reservation_id','table', 'customer_first_name', 'customer_last_name', 'customer_email', 'reservation_date', 'reservation_status', 'number_of_guests', 'special_request', 'created_at', 'updated_at']
        read_only_fields = ['reservation_id', 'created_at', 'updated_at']