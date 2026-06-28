from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Table

# Register your models here.
@admin.register(Table)
class TableAdmin(ModelAdmin):
    list_display = ['table_id', 'table_number', 'table_status', 'capacity', 'location']
    search_fields = ['table_id', 'table_number', 'table_status', 'capacity', 'location']
    list_filter = ['table_id', 'table_number', 'table_status', 'capacity', 'location']