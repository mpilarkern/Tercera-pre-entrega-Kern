from django.db import models

# Create your models here
class Genre(models.Model):
    name = models.CharField(max_length=64)

class Movies(models.Model):
    title = models.CharField(max_length=256)
    length = models.DurationField(null=True)
    release_year = models.IntegerField()
    plot = models.TextField(blank=True, null=True)

class Series(models.Model):
    title = models.CharField(max_length=256)
    seasons = models.IntegerField(null=True)
    release_year = models.IntegerField()
    plot = models.TextField(blank=True, null=True)