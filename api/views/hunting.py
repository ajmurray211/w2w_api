from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.hunting import Hunting
from ..serializers.hunting import HuntingSerializer

class HuntingView(APIView):
    def get(self,request):
        hunting = Hunting.objects.all()
        data = HuntingSerializer(hunting, many = True).data
        return Response(data)
    
    def post(self, request):
        hunting = HuntingSerializer(data = request.data)
        if hunting.is_valid():
            hunting.save()
            return Response(hunting.data, status=status.HTTP_201_CREATED)
        else:
            return Response(hunting.errors, status=status.HTTP_400_BAD_REQUEST)

class HuntView(APIView):
    def get(self, request, pk):
        hunting = get_object_or_404(Hunting, pk=pk)
        data = HuntingSerializer(hunting).data
        return Response(data)
    
    def put(self, request, pk):
        hunting = get_object_or_404(Hunting, pk=pk)
        data = HuntingSerializer(hunting, data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        hunting = get_object_or_404(Hunting, pk=pk)
        hunting.delete()
        hunting = Hunting.objects.all()
        data = HuntingSerializer(hunting, many=True).data
        return Response(data)