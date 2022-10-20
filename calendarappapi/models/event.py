from django.db import models
from django.contrib.auth.models import User
from calendarappapi.models.state import State

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField(blank=True)
    time_start = models.TimeField()
    time_end = models.TimeField(blank=True)
    cost = models.CharField(max_length=100)
    about = models.CharField(max_length=1000, null=False, blank=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip = models.IntegerField()
    social_one = models.CharField(max_length=25, null=False, blank=True)
    social_two = models.CharField(max_length=25, null=False, blank=True)
    tags = models.ManyToManyField("calendarappapi.Tag", related_name="events")
    