import datetime

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostCategory
from .serializers import PostSerializer, CategorySerializer


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_at=datetime.datetime.now(),
        )


class CategoryViewSet(ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer
