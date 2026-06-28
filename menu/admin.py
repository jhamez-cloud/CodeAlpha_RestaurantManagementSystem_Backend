from django.contrib import admin
from .models import MenuItem,MenuCategory
from unfold.admin import ModelAdmin,StackedInline

# Register your models here.
class MenuItemInline(StackedInline):
    model = MenuItem
    extra = 0
    max_num = 1

@admin.register(MenuCategory)
class MenuCategoryAdmin(ModelAdmin):
    inlines = [MenuItemInline]

    list_display = ["menu_category_id", "name", "description"]
    search_fields = ["menu_category_id", "name"]


@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ["menu_item_id", "name", "description", "price"]
    search_fields = ["menu_item_id", "name", "description"]
    list_filter = ["category"]