from django.db import models

# Create your models here.
class Inventory(models.Model):
    Inventory_id = models.CharField(max_length=100,unique=True,editable=False)
    item_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=5)
    quantity_available = models.PositiveIntegerField()
    minimum_quantity = models.PositiveIntegerField()
    cost_price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)
    last_restocked = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.Inventory_id:
            self.Inventory_id = f"INV-{self.pk:03d}"
            Inventory.objects.filter(pk=self.pk).update(Inventory_id=self.Inventory_id)

    def __str__(self):
        return f"{self.Inventory_id}--{self.item_name}"