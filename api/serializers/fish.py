from rest_framework import serializers
from ..models.fish import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('id', 'name', 'imgMain', 'typeOfWater', 'avgLifespan', 'avgLength', 'avgWeight')