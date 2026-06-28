from rest_framework import serializers
from .models import Order,OrderItem
from menu.serializers import MenuItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id','order_number','customer_name', 'order_type', 'order_status', 
                  'payment_status','subtotal', 'tax', 'discount','total_amount', 'created_at', 'updated_at']
        read_only_fields = ['order_id','total_amount','created_at', 'updated_at']

class OrderItemReadSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    menu_item = MenuItemSerializer()
    subtotal = serializers.ReadOnlyField()
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at','subtotal']

class OrderItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'menu_item', 'quantity','subtotal', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at','subtotal']