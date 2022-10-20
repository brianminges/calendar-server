from django.db import models
from django.contrib.auth.models import User
from calendarappapi.models.event import Event

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.CharField(max_length=10000)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)