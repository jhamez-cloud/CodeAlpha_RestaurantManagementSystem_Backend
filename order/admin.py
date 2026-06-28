from django.contrib import admin
from unfold.admin import ModelAdmin,TabularInline
from .models import Order,OrderItem

# Register your models here.
class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 0
    max_num = 1
    readonly_fields = ['price']

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity','subtotal', 'notes']
    search_fields = ['order', 'menu_item', 'quantity','subtotal', 'notes']
    readonly_fields = ['price']

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    inlines = [OrderItemInline]

    list_display = ['order_id', 'order_number', 'customer_name', 'order_type', 'order_status', 'subtotal', 'tax', 'discount', 'payment_status', 'total_amount', 'created_at', 'updated_at']
    search_fields = ['order_id', 'order_number', 'customer_name', 'order_type', 'order_status', 'subtotal', 'tax', 'discount', 'payment_status', 'total_amount', 'created_at', 'updated_at']
