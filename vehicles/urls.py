from rest_framework.routers import DefaultRouter
from vehicles.views import VehicleViewSet, MechanicViewSet, MaintenanceViewSet

router = DefaultRouter()
router.register('vehicles', VehicleViewSet)
router.register('mechanics', MechanicViewSet )
router.register('jobs', MaintenanceViewSet)

urlpatterns = router.urls