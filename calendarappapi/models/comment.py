from django.db import models
from django.contrib.auth.models import User
from calendarappapi.models.event import Event

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    