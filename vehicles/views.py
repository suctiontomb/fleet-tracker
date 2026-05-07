from vehicles.models import Vehicle, Mechanic,MaintenanceJob
from rest_framework import  viewsets
from vehicles.serializers import VehicleSerializer, MechanicSerializer, MaintenanceJobSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from datetime import date, timedelta
from rest_framework.decorators import action
from rest_framework.response import Response

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['registration_number', 'make', 'model']

    @action(detail=False, methods=['get'])
    def due_for_service(self, request):
        today = date.today()
        due_date = today + timedelta(days=30)
        vehicles = Vehicle.objects.filter(next_service_due__lte=due_date)
        serializer = VehicleSerializer(vehicles,many=True)
        return Response(serializer.data)


class MechanicViewSet(viewsets.ModelViewSet):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['first_name', 'last_name']


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceJob.objects.all()
    serializer_class = MaintenanceJobSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['status']
    search_fields = ['description', 'notes']
