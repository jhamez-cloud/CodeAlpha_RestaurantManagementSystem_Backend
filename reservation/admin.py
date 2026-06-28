from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = ['reservation_id', 'customer_full_name','customer_email','reservation_date','reservation_status', 'number_of_guests']