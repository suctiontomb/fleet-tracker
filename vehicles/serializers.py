from rest_framework import serializers
from vehicles.models import Vehicle, Mechanic,MaintenanceJob

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'

class MaintenanceJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJob
        fields=  '__all__'

