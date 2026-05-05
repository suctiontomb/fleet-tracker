from django.db import models

# Create your models here.
class Vehicle(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    total_flight_hours = models.IntegerField()
    last_maintenance = models.DateField()
    next_service_due = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.registration_number} - {self.make} - {self.model}"

class Mechanic(models.Model):
    id_number = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self)-> str:
        return f"{self.id_number} - {self.first_name} - {self.last_name}"

class MaintenanceJob(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default= 'pending')
    scheduled_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self)-> str:
        return f"Job: {self.description[:30]} - {self.vehicle} - {self.mechanic}"


