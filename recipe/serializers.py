from rest_framework import serializers
from .models import Recipe
from menu.serializers import MenuItemSerializer
from inventory.serializers import InventorySerializer

class RecipeSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    inventory = InventorySerializer()
    class Meta:
        model = Recipe
        fields = ['recipe_id', 'menu_item', 'inventory', 'quantity_required']
        read_only_fields = ['recipe_id']