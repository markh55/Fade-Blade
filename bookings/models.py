from django.db import models

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
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} with {self.timeslot.barber.name} on {self.timeslot.date} at {self.timeslot.start_time.strftime('%H:%M')}"