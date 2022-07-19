from rest_framework import serializers
from ..models.Fish import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        # fields = ('name','imgMain','imgGallery','color','size','country','region','diet','habitat','breedingSeason','typeOfWater','lifespan','endangeredRating','generalInfo')
        fields = ('name','imgMain')