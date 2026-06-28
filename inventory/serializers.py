from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Inventory
        fields = ['Inventory_id', 'item_name', 'unit', 'quantity_available', 
                  'minimum_quantity', 'cost_price_per_unit', 'supplier', 'last_restocked']