from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_id = models.CharField(max_length=100,unique=True,editable=False)
    name =  models.CharField(max_length=100,unique=True)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.menu_category_id:
            self.menu_category_id = f"MENU-C-{self.pk:03d}"
            MenuCategory.objects.filter(pk=self.pk).update(menu_category_id=self.menu_category_id)

    def __str__(self):
        return f"{self.menu_category_id}--{self.name.capitalize()}"
    

class MenuItem(models.Model):
    menu_item_id = models.CharField(max_length=100,unique=True,editable=False)
    category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/',null=True,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.menu_item_id:
            self.menu_item_id = f"MENU-I-{self.pk:03d}"
            MenuItem.objects.filter(pk=self.pk).update(menu_item_id=self.menu_item_id)

    def __str__(self):
        return f"{self.category.name.capitalize()}--{self.name.capitalize()}"