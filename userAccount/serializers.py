from .models import User
from post.models import Post
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    def create(self, validated_data):
        user = User.objects.create_user(
            userID = validated_data['userID'],
            nickname = validated_data['nickname'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['userID','nickname','password']