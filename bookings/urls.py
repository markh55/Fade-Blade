from rest_framework.routers import DefaultRouter
from .views import BarberViewSet, BusinessHoursViewSet, TimeSlotViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'barbers', BarberViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'business-hours', BusinessHoursViewSet)
urlpatterns = router.urls