from decimal import Decimal

from django.db import transaction
from django.db.models import F

from recipe.models import Recipe


class InventoryService:

    @staticmethod
    @transaction.atomic
    def process_order(order):

        errors = []

        # -------------------------
        # CHECK STOCK
        # -------------------------

        for item in order.orderitem_set.select_related("menu_item"):

            recipes = Recipe.objects.select_related(
                "inventory"
            ).filter(
                menu_item=item.menu_item
            )

            if not recipes.exists():
                errors.append({
                    "menu_item": item.menu_item.name,
                    "message": "Recipe not found."
                })
                continue

            for recipe in recipes:

                required = (
                    Decimal(recipe.quantity_required)
                    * Decimal(item.quantity)
                )

                if recipe.inventory.quantity_available < required:

                    errors.append({
                        "menu_item": item.menu_item.name,
                        "ingredient": recipe.inventory.item_name,
                        "required": required,
                        "available": recipe.inventory.quantity_available
                    })

        if errors:

            return {
                "message": "Insufficient inventory.",
                "details": errors,
                "success": False
            }

        # -------------------------
        # DEDUCT INVENTORY
        # -------------------------

        for item in order.orderitem_set.select_related("menu_item"):

            recipes = Recipe.objects.select_related(
                "inventory"
            ).filter(
                menu_item=item.menu_item
            )

            for recipe in recipes:

                required = (
                    Decimal(recipe.quantity_required)
                    * Decimal(item.quantity)
                )

                recipe.inventory.__class__.objects.filter(
                    pk=recipe.inventory.pk
                ).update(
                    quantity_available=F("quantity_available") - required
                )

        return {
            "success": True
        }