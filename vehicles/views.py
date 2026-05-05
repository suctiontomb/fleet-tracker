from django.shortcuts import render
from vehicles.models import Vehicle, Mechanic,MaintenanceJob
from rest_framework import  viewsets
from vehicles.serializers import VehicleSerializer, MechanicSerializer, MaintenanceJobSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class MechanicViewSet(viewsets.ModelViewSet):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceJob.objects.all()
    serializer_class = MaintenanceJobSerializer
