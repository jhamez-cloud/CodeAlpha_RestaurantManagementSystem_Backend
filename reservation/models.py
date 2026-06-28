from django.db import models

# Create your models here.
class Reservation(models.Model):
    class ReservationStatus(models.TextChoices):
        PENDING = 'PENDING','Pending'
        CONFIRMED = 'CONFIRMED','Confirmed'
        CANCELLED = 'CANCELLED','Cancelled'
        COMPLETED = 'COMPLETED','Completed'

    reservation_id = models.CharField(
        max_length=100,
        unique=True,
        editable=False
        )
    table = models.ForeignKey('table.Table', on_delete=models.CASCADE)
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_status = models.CharField(max_length=100,choices=ReservationStatus.choices)
    number_of_guests = models.PositiveIntegerField()
    special_request = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def customer_full_name(self):
        return f"{self.customer_first_name} {self.customer_last_name}"

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.reservation_id:
            self.reservation_id = f"RES-{self.pk:03d}"
            Reservation.objects.filter(pk=self.pk).update(reservation_id=self.reservation_id)

    def __str__(self):
        return f"{self.reservation_id}--{self.customer_first_name} {self.customer_last_name}"