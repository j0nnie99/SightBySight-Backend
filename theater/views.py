from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http.response import HttpResponse 
from .models import Theater
from .serializers import TheaterSerializer



# Create your views here.
@api_view(['GET'])
def theaterList(request):
    theaters = Theater.objects.all()
    serailized_posts= TheaterSerializer(theaters, many=True)
    return Response(serailized_posts.data) 
    