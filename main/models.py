from django.contrib.auth.models import User
from django.db import models

# class Bus(models.Model):
#     number = models.CharField(max_length=20)
#     model = models.CharField(max_length=100)
#     capacity = models.PositiveIntegerField()
#     last_maintenance_date = models.DateField()

class Route(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    schedule = models.DateTimeField(null=True, default=None)
    price = models.CharField(max_length=6, null=True, default=None)
    status =  models.CharField(max_length=30, default='Ожидает')

# class Passenger(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=10)
#     contact_number = models.CharField(max_length=20)
#     email = models.EmailField()

class Ticket(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    # bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # purchase_date = models.DateTimeField()


# class Station(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     contact_number = models.CharField(max_length=20)
#     email = models.EmailField()
#
# class Schedule(models.Model):
#     route = models.ForeignKey(Route, related_name='routes', on_delete=models.CASCADE)
#     bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
#     day_of_week = models.CharField(max_length=20)
#     departure_time = models.TimeField()
#     arrival_time = models.TimeField()
