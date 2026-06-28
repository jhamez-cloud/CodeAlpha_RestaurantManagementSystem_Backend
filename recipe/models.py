from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.CharField(max_length=20,unique=True,editable=False)
    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE)
    quantity_required = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.recipe_id:
            self.recipe_id = f"REC-{self.pk:03d}"
            Recipe.objects.filter(pk=self.pk).update(recipe_id=self.recipe_id)

    def __str__(self):
        return f"{self.recipe_id}--{self.menu_item.name}--{self.inventory.item_name}"