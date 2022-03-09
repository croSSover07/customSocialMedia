import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostCategory, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer


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


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['comment_id', 'id']

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.filter(id=post_id).first()
        serializer.save(
            post_id=post,
            created_at=datetime.datetime.now(),
        )

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))
