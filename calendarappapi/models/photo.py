from django.db import models
from calendarappapi.models.event import Event

class Photo(models.Model):
    data = models.CharField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)