from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Inventory

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(ModelAdmin):
    list_display = ['item_name', 'quantity_available', 'minimum_quantity', 'cost_price_per_unit', 'supplier', 'last_restocked']
    search_fields = ['item_name', 'quantity_available', 'minimum_quantity', 'cost_price_per_unit', 'supplier', 'last_restocked']
    list_filter = ['item_name', 'quantity_available', 'minimum_quantity', 'cost_price_per_unit', 'supplier', 'last_restocked']