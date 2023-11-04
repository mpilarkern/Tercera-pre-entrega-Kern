from django.db import models

# Create your models here
class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.DurationField(blank=True, null=True)
    release_year = models.IntegerField()
    plot = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

class Serie(models.Model):
    title = models.CharField(max_length=256)
    seasons = models.IntegerField(null=True)
    release_year = models.IntegerField()
    plot = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'