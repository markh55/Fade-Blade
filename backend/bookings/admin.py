from django.contrib import admin
from .models import Barber, BusinessHours, TimeSlot, Booking, Media

# Register your models here.
admin.site.register(Barber)
admin.site.register(TimeSlot)
admin.site.register(Booking)
admin.site.register(BusinessHours)
admin.site.register(Media)
