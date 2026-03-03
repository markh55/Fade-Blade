from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta, datetime
from bookings.models import Barber, TimeSlot, BusinessHours

class Command(BaseCommand):
    help = 'Generate timeslots for the next 2 weeks'

    def handle(self, *args, **kwargs):
        barbers = Barber.objects.all()
        today = timezone.now().date()
        business_hours = {bh.day: bh for bh in BusinessHours.objects.all()}

        for day_offset in range(14):
            date = today + timedelta(days=day_offset)
            weekday = date.weekday()

            if weekday not in business_hours:
                continue

            bh = business_hours[weekday]

            if not bh.is_open:
                continue

            for barber in barbers:
                current = datetime.combine(date, bh.open_time)
                end_dt = datetime.combine(date, bh.close_time)

                while current < end_dt:
                    TimeSlot.objects.get_or_create(
                        barber=barber,
                        date=date,
                        start_time=current.time(),
                        defaults={'is_available': True}
                    )
                    current += timedelta(minutes=15)

        self.stdout.write(self.style.SUCCESS('Timeslots generated successfully'))