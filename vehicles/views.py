from django.shortcuts import render
from vehicles.models import Vehicle, Mechanic,MaintenanceJob
from rest_framework import  viewsets
from vehicles.serializers import VehicleSerializer, MechanicSerializer, MaintenanceJobSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class MechanicViewSet(viewsets.ModelViewSet):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceJob.objects.all()
    serializer_class = MaintenanceJobSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
