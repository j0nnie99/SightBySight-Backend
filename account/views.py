from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http.response import HttpResponse 

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serailized_posts= UserSerializer(users, many=True)
    return Response(serailized_posts.data) 