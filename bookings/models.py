from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Barber (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.barber.name} - {self.date} {self.start_time.strftime('%H:%M')}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} with {self.timeslot.barber.name} on {self.timeslot.date} at {self.timeslot.start_time.strftime('%H:%M')}"

class BusinessHours(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    day = models.IntegerField(choices=DAY_CHOICES, unique=True)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    is_open = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Business Hours"

    def __str__(self):
        return f"{self.get_day_display()} {self.open_time} - {self.close_time}"
    

class Media(models.Model):
    file = CloudinaryField('file')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media {self.id} - {self.file.public_id}"