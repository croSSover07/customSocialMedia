from django.db import models
from accounts.models import Account


class Subscription(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='author')
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(editable=False)

    class Meta:
        unique_together = (("author", "owner"),)
