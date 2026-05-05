from django.contrib import admin
from vehicles.models import  Vehicle, Mechanic, MaintenanceJob

admin.site.register(Vehicle)
admin.site.register(Mechanic)
admin.site.register(MaintenanceJob)

