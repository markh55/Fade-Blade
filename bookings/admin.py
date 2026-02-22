from django.contrib import admin
from .models import Barber, TimeSlot, Booking

# Register your models here.
admin.site.register(Barber)
admin.site.register(TimeSlot)
admin.site.register(Booking)
