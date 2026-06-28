from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['user_id','role', 'first_name', 'last_name', 'email', 'phone','is_active']
    search_fields = ['user_id', 'first_name', 'last_name', 'email', 'phone', 'role', 'is_active']
    list_filter = ['user_id', 'first_name', 'last_name', 'email', 'phone', 'role', 'is_active']