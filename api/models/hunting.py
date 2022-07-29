from django.db import models

class Hunting(models.Model):
    name = models.CharField(max_length=100)
    imgMain = models.URLField(max_length=200)
    # imgGallery : models.CharField(max_length=100)
    # color = models.CharField(max_length=100)
    # size = models.CharField(max_length=100)
    # weight = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    # region = models.CharField(max_length=100)
    # diet = models.CharField(max_length=100)
    # habitat = models.CharField(max_length=100)
    # breedingSeason = models.CharField(max_length=100)
    # lifespan = models.CharField(max_length=100)
    # endangeredRating = models.CharField(max_length=100)
    # generalInfo = models.CharField(max_length=100)