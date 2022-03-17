from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import PostCategory, Post, Comment, Like
from accounts.serializers import AccountSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class PostReadSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(required=False)
    category = CategorySerializer(read_only=True, many=True)
    owner = AccountSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post):
        return Like.objects.filter(post_id=post.id, comment_id=None).count()

    class Meta:
        model = Post
        fields = '__all__'


class PostWriteSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Post
        fields = '__all__'


class CommentReadSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(required=False)
    post_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    owner = AccountSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, comment):
        return Like.objects.filter(post_id=comment.post_id, comment_id=comment.id).count()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentWriteSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(required=False)
    post_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class LikeReadSerializer(ModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    comment_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    owner = AccountSerializer(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class LikeWriteSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
