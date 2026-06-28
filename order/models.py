from django.db import models

# Create your models here.
class Order(models.Model):
    class OrderType(models.TextChoices):
        DINE_IN = 'DINE_IN', 'Dine In'
        TAKE_AWAY = 'TAKE_AWAY', 'Take Away'
        DELIVERY = 'DELIVERY', 'Delivery'

    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PREPARING = 'PREPARING', 'Preparing'
        SERVED = 'SERVED', 'Served'
        READY = 'READY', 'Ready'

    class PaymentStatus(models.TextChoices):
        PENDING = 'PENDING','Pending'
        PAID = 'PAID','Paid'
        REFUNDED = 'REFUNDED','Refunded'
    
    order_id = models.CharField(max_length=100,unique=True,editable=False)
    order_number = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey('table.Table', on_delete=models.CASCADE,null=True)
    waiter = models.ForeignKey('user.User', on_delete=models.CASCADE,null=True)
    order_type = models.CharField(max_length=100,choices=OrderType.choices)
    order_status = models.CharField(max_length=100,choices=OrderStatus.choices)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=100,choices=PaymentStatus.choices)
    #total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_amount(self):
        return float(self.subtotal + self.tax - self.discount)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.order_id:
            self.order_id = f"ORD-{self.pk:03d}"
            Order.objects.filter(pk=self.pk).update(order_id=self.order_id)

    def __str__(self):
        return f"{self.customer_name}'s Order--{self.order_number}"
    

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if self.menu_item and self._state.adding:
            self.price = self.menu_item.price
        super().save(*args,**kwargs)

    @property
    def subtotal(self):
        return self.quantity * self.price
    
    def __str__(self):
        item_name = self.menu_item.name.upper()
        return f"{item_name} : {self.quantity}"
    