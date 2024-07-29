from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="vehicles"
    )

    def __str__(self):
        return f"{self.brand} - {self.license_plate}"


class Officer(models.Model):
    name = models.CharField(max_length=255)
    badge_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Violation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    comments = models.TextField()

    def __str__(self):
        return f"{self.vehicle} - {self.timestamp}"
