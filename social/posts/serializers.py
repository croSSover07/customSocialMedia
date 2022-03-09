from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import PostCategory, Post, Comment


class PostSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'
