from calendar import c
from django.db import models

class Tag(models.Model):
    name = models.CharField()