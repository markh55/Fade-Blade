from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime, time
from bookings.models import Barber, TimeSlot

class Command(BaseCommand):
    help = 'Generate timeslots for the next 2 weeks'

    def handle(self, *args, **kwargs):
        
        barbers = Barber.objects.all()
        today = timezone.now().date()

        for day_offset in range(14):
            date = today + timedelta(days=day_offset)
            weekday = date.weekday()  # 0 = Monday, 6 = Sunday

            if weekday == 6:  # Skip Sunday
                continue

            if weekday == 5:  # Saturday
                start = time(10, 0)
                end = time(15, 0)
            else:  # Monday to Friday
                start = time(9, 0)
                end = time(17, 0)

            for barber in barbers:
                current = datetime.combine(date, start)
                end_dt = datetime.combine(date, end)

                while current < end_dt:
                    TimeSlot.objects.get_or_create(
                        barber=barber,
                        date=date,
                        start_time=current.time(),
                        defaults={'is_available': True}
                    )
                    current += timedelta(minutes=15)

        self.stdout.write(self.style.SUCCESS('Timeslots generated successfully'))