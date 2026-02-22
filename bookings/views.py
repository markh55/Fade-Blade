from .models import Barber, TimeSlot, Booking
from .serializers import BarberSerializer, TimeSlotSerializer, BookingSerializer
from rest_framework import viewsets

# Create your views here.
class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer