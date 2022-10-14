from django.db import models
from django.contrib.auth.models import User
from calendarappapi.models.state import State
from calendarappapi.models.photo import Photo
from calendarappapi.models.comment import Comment
from calendarappapi.models.tag import Tag

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField(blank=True)
    time_start = models.TimeField()
    time_end = models.TimeField(blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    about = models.CharField(max_length=1000, null=False, blank=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip = models.IntegerField(max_length=5)
    social_one = models.CharField(max_length=25, null=False, blank=True)
    social_two = models.CharField(max_length=25, null=False, blank=True)
    tags = models.ManyToManyRel(Tag, related_name="events")
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True)
    