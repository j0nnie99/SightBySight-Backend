from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http.response import HttpResponse 
from .models import Seat
from .serializers import SeatSerializer


# Create your views here.
@api_view(['GET'])
def seatList(request):
    seats = Seat.objects.all()
    serailized_posts= SeatSerializer(seats, many=True)
    return Response(serailized_posts.data) 
    