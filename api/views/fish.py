from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.fish import Fish
from django.shortcuts import get_object_or_404
from ..serializers.fish import FishSerializer

class FishingView(APIView):
    def get(self, request):
        fish = Fish.objects.all()
        data = FishSerializer(fish, many=True).data
        return Response(data)
    
    def post(self, request):
        fish = FishSerializer(data = request.data)
        if fish.is_valid():
            fish.save()
            return Response(fish.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fish.errors, status=status.HTTP_400_BAD_REQUEST)

class FishView(APIView):
    def get(self,request, pk):
        fish = get_object_or_404(Fish, pk=pk)
        data = FishSerializer(fish).data
        return Response(data)

    def put(self, request, pk):
        fish = get_object_or_404(Fish, pk=pk)
        data = FishSerializer(fish, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        fish = get_object_or_404(Fish, pk=pk)
        fish.delete()
        fish = Fish.objects.all()
        data = FishSerializer(fish, many=True).data
        return Response(data)
