from django.db import models


# Create your models here.

class Restaurant(models.Model):
    """Restaurant object"""
    name = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    ingredients = models.CharField(max_length=255)

    # display an instance of the model when necessary
    def __str__(self):
        return self.name
