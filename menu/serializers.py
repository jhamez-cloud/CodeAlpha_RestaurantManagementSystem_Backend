from rest_framework import serializers
from .models import MenuItem,MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['menu_category_id', 'name', 'description', 'is_available', 'created_at', 'updated_at']
        read_only_fields = ['menu_category_id','created_at', 'updated_at']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = MenuCategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['menu_item_id', 'category', 'name', 'image', 'description', 'price', 'preparation_time', 'is_available', 'created_at', 'updated_at']
        read_only_fields = ['menu_item_id','created_at', 'updated_at']