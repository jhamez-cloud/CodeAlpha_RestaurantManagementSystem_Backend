from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_id', 'table_number', 'table_status', 'capacity', 'location', 'created_at', 'updated_at']
        read_only_fields = ['table_id','created_at', 'updated_at']