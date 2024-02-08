from django.db import models


class FlightForm(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    booking_number = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
