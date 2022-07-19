from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=50)
    imgMain = models.URLField(max_length=300)
    # imgGallery = []
    # color = models.CharField(max_length=50)
    # size = models.IntegerField()
    # country = models.CharField(max_length=100)
    # region = models.CharField(max_length=100)
    # diet = models.CharField(max_length=500)
    # habitat = models.CharField(max_length=500)
    # breedingSeason = models.CharField(max_length=50)
    # typeOfWater = models.CharField(max_length=50)
    # lifeSpan = models.CharField(max_length=200)
    # endangeredRating = models.CharField(max_length=50)
    # generalInfo = models.CharField(max_length=500)