from django.core import serializers
from rest_framework import serializers 
from .models import Post 


class PostSerializer(serializers.ModelSerializer): 
    #user_id = serializers.CharField(source='user_id.nickname')
    #theater = serializers.CharField(source='theater.name')
    class Meta:
        model = Post 
        fields = '__all__'
    


#class PostSerializer(serializers.ModelSerializer):
#    user_id = serializers.CharField(source='user_id.nickname')
#    theater = serializers.CharField(source='theater.name')
#    class Meta:
#        model = Post 
#        fields = '__all__'



