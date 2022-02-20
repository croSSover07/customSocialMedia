from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostCategory
from .serializers import PostSerializer, CategorySerializer


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer
