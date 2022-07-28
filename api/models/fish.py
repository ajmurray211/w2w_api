from django.db import models

class Fish(models.Model):
        name = models.CharField(max_length=100)
        imgMain = models.URLField(max_length=100)
        # imgGallery =  models.CharField(max_length=100)
        # color = models.CharField(max_length=100)
        # size =  models.IntegerField(max_length=100)
        # country =  models.CharField(max_length=100)
        # region = models.CharField(max_length=100)
        # diet =  models.CharField(max_length=100)
        # habitat = models.CharField(max_length=100)
        # breedingSeason = models.CharField(max_length=100)
        # typeOfWater =  models.CharField(max_length=100)
        # lifespan =  models.CharField(max_length=100)
        # endangeredRating = models.CharField(max_length=100)
        # generalInfo =  models.CharField(max_length=1000)
        