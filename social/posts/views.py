import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostCategory, Comment
from .serializers import PostWriteSerializer, CategorySerializer, CommentSerializer, PostReadSerializer


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            created_at=datetime.datetime.now(),
        )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostReadSerializer
        else:
            return PostWriteSerializer


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
