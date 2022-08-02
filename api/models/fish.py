from django.db import models

class Fish(models.Model):
        name = models.CharField(max_length=100)
        imgMain = models.URLField(max_length=100)
        family = models.CharField(max_length=100, blank=True)
        # imgGallery =  models.CharField(max_length=100) 
        # color = models.CharField(max_length=100)
        avgLength =  models.CharField(max_length=100, blank=True)
        avgWeight =  models.CharField(max_length=100, blank=True)
        # country =  models.CharField(max_length=100)
        # region = models.CharField(max_length=100)
        diet =  models.CharField(max_length=1000, blank = True)
        habitat = models.CharField(max_length=100, blank=True)
        breedingSeason = models.CharField(max_length=100, blank=True)
        typeOfWater =  models.CharField(max_length=100, blank=True)
        avgLifespan =  models.CharField(max_length=100, blank=True)
        # endangeredRating = models.CharField(max_length=100)
        # generalInfo =  models.CharField(max_length=1000)
        