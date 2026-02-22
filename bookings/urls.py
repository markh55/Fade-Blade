from rest_framework.routers import DefaultRouter
from .views import BarberViewSet, TimeSlotViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'barbers', BarberViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'bookings', BookingViewSet)
urlpatterns = router.urls