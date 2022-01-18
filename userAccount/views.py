#userAccount/views.py
from django.shortcuts import render
from .serializers import UserSerializer
from .models import User, isLogin
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import generics, status
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import exceptions
from post.models import Post



@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 회원가입
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.filter(nickname = serializer.data["nickname"])
        return Response(user[0].id)     
    return Response(serializer.errors)

# 로그인
@api_view(['POST'])
def login(request):
    user = User.objects.filter(userID = request.data["userID"])
    #isLogin DB에 userID 저장
    #isLogin.save(user)
    print("Login Success!")
    #
    if len(user)==1:
        if check_password(request.data['password'], user[0].password): 
            return Response(user[0].id)     
        return Response("wrong password")     
    return Response("wrong userID")          
