from django.core import serializers
from rest_framework import serializers 
from .models import Post
from userAccount.models import User


class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.nickname')
    theater = serializers.CharField(source='theater.name')
    class Meta:
        model = Post 
        fields = '__all__'



