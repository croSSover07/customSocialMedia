from django.db import models
from accounts.models import Account


# Create your models here.

class PostCategory(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'title: {self.title} '


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(PostCategory)
    created_at = models.DateTimeField(editable=False)
    owner = models.ForeignKey(Account, on_delete=models.DO_NOTHING, editable=False)

    def __str__(self):
        return f'id:{self.id} - title: {self.title}'


class Comment(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(editable=False)

    def __str__(self):
        return f'id:{self.id} - body: {self.text}'


class Like(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, editable=False)
    post_id = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, default=None)
    comment_id = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, default=None)
