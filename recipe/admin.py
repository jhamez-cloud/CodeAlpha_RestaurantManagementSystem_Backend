from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Recipe

# Register your models here.
    
@admin.register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ['recipe_id', 'menu_item','inventory','quantity_required']
    search_fields = ['recipe_id', 'menu_item','inventory','quantity_required']
    list_filter = ['recipe_id', 'menu_item','quantity_required']