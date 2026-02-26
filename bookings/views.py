from .models import Barber, BusinessHours, TimeSlot, Booking
from .serializers import BarberSerializer, BusinessHoursSerializer, TimeSlotSerializer, BookingSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import resend
import os

resend.api_key = os.getenv('RESEND_API_KEY')

class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated]

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['barber', 'date', 'is_available']

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['timeslot__barber', 'timeslot__date']

    def perform_create(self, serializer):
        booking = serializer.save()
        timeslot = booking.timeslot
        timeslot.is_available = False
        timeslot.save()

        resend.Emails.send({
            "from": "Fade & Blade <bookings@yourdomain.com>",
            "to": booking.customer_email,
            "subject": "Booking Request Received - Fade & Blade",
            "html": f"""
                <h2>Booking Request Received</h2>
                <p>Hi {booking.customer_name},</p>
                <p>We've received your booking request with {timeslot.barber.name} on {timeslot.date} at {timeslot.start_time}.</p>
                <p>You'll receive a confirmation email once the barber has approved it.</p>
                <p>Fade & Blade</p>
            """
        })

        resend.Emails.send({
            "from": "Fade & Blade <bookings@yourdomain.com>",
            "to": timeslot.barber.email,
            "subject": "New Booking Request",
            "html": f"""
                <h2>New Booking Request</h2>
                <p>You have a new booking request from {booking.customer_name} on {timeslot.date} at {timeslot.start_time}.</p>
                <p>Phone: {booking.phone}</p>
                <p>Email: {booking.customer_email}</p>
            """
        })

    def perform_update(self, serializer):
        booking = serializer.save()
        if booking.status == 'confirmed':
            resend.Emails.send({
                "from": "Fade & Blade <bookings@yourdomain.com>",
                "to": booking.customer_email,
                "subject": "Booking Confirmed - Fade & Blade",
                "html": f"""
                    <h2>Booking Confirmed!</h2>
                    <p>Hi {booking.customer_name},</p>
                    <p>Your booking with {booking.timeslot.barber.name} on {booking.timeslot.date} at {booking.timeslot.start_time} has been confirmed.</p>
                    <p>See you soon!</p>
                    <p>Fade & Blade</p>
                """
            })
        elif booking.status == 'rejected':
            resend.Emails.send({
                "from": "Fade & Blade <bookings@yourdomain.com>",
                "to": booking.customer_email,
                "subject": "Booking Update - Fade & Blade",
                "html": f"""
                    <h2>Booking Update</h2>
                    <p>Hi {booking.customer_name},</p>
                    <p>Unfortunately your booking request for {booking.timeslot.date} at {booking.timeslot.start_time} could not be confirmed.</p>
                    <p>Please get in touch to rearrange.</p>
                    <p>Fade & Blade</p>
                """
            })

class BusinessHoursViewSet(viewsets.ModelViewSet):
    queryset = BusinessHours.objects.all()
    serializer_class = BusinessHoursSerializer
    permission_classes = [IsAuthenticated]