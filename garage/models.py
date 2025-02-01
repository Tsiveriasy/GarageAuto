from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Voiture'),
        ('motorcycle', 'Moto'),
        ('truck', 'Camion'),
        ('van', 'Utilitaire'),
    ]

    type = models.CharField(max_length=20, choices=VEHICLE_TYPES, default='car')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_type_display()} - {self.year} {self.make} {self.model} ({self.license_plate})"
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  # Augmentons max_digits pour accommoder les grands nombres en Ariary
    icon = models.CharField(max_length=50, default='wrench')

    def __str__(self):
        return f"{self.name} - {self.price} Ar"


class Appointment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle} - {self.service} - {self.date}"
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"

