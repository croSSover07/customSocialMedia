from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from .models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)
