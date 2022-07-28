from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from ..models.fish import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('name', 'imgMain')