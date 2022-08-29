from django.db import models

# Create your models here.
class Meetings(models.Model):
    topic = models.CharField(max_length=250)
    duration = models.FloatField()
    starttime = models.DateField()
    passwords = models.CharField(max_length=250)
    url = models.CharField(max_length=250)