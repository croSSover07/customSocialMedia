import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Post, PostCategory, Comment, Like
from .permissions import IsOwnerOrReadOnly
from .serializers import PostWriteSerializer, CategorySerializer, CommentReadSerializer, CommentWriteSerializer, \
    PostReadSerializer, LikeReadSerializer, LikeWriteSerializer


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            created_at=datetime.datetime.now(),
            owner=self.request.user
        )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostReadSerializer
        else:
            return PostWriteSerializer


class CategoryViewSet(ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['comment_id', 'id']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.filter(id=post_id).first()
        serializer.save(
            post_id=post,
            created_at=datetime.datetime.now(),
            owner=self.request.user
        )

    def create(self, request, *args, **kwargs):
        comment_id = request.data.get('comment_id')
        post_id = self.kwargs.get('post_id')
        check_comment = Comment.objects.filter(id=comment_id, post_id=post_id).first()
        if check_comment is None and comment_id is not None:
            return Response(f'Error, comment_id={comment_id} doesnt belong to post_id={post_id} ', status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request=request, args=args, kwargs=kwargs)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentReadSerializer
        else:
            return CommentWriteSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        post = Post.objects.filter(id=post_id).first()
        comment = Comment.objects.filter(id=comment_id).first()
        serializer.save(
            post_id=post,
            comment_id=comment,
            owner=self.request.user
        )

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        a = Like.objects.filter(post_id=post_id, comment_id=comment_id, owner=self.request.user).first()
        if a is None:
            return super().create(request=request, args=args, kwargs=kwargs)
        else:
            a.delete()
            return Response([], status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LikeReadSerializer
        else:
            return LikeWriteSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'),
                                             comment_id=self.kwargs.get('comment_id'))
