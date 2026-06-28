from django.db import models

# Create your models here.
class User(models.Model):
    class UserRole(models.TextChoices):
        ADMIN = 'ADMIN','Admin'
        CASHIER = 'CASHIER','Cashier'
        WAITER = 'WAITER','Waiter'
        KITCHEN_STAFF = 'KITCHEN_STAFF','Kitchen Staff'

    user_id = models.CharField(
        max_length=100,
        unique=True,
        editable=False
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100,
                            choices=UserRole.choices
                            )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.user_id:
            self.user_id = f"USR-{self.pk:03d}"
            User.objects.filter(pk=self.pk).update(user_id=self.user_id)

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"