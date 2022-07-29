from rest_framework import serializers
from ..models.hunting import Hunting 

class HuntingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunting
        fields = ('id', 'name', 'imgMain')