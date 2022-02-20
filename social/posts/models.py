from django.db import models
from accounts.models import Account


# Create your models here.

class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return f'title: {self.title} '


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()
    owner = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'id:{self.id} - title: {self.title}'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'id:{self.id} - body: {self.text}'
