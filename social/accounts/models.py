from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    last_joined_at = models.DateTimeField()

    def __str__(self):
        return f'id:{self.id} - name: {self.first_name} {self.second_name} '
