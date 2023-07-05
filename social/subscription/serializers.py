from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.serializers import AccountSerializer
from subscription.models import Subscription


class SubscriptionReadSerializer(ModelSerializer):
    author = AccountSerializer(read_only=True)
    owner = AccountSerializer(read_only=True)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionWriteSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = []