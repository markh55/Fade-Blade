from rest_framework.routers import DefaultRouter
from .views import BarberViewSet, BusinessHoursViewSet, TimeSlotViewSet, BookingViewSet, MediaViewSet

router = DefaultRouter()
router.register(r'barbers', BarberViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'business-hours', BusinessHoursViewSet)
router.register(r'media', MediaViewSet)
urlpatterns = router.urls