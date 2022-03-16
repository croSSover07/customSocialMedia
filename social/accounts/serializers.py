from rest_framework.serializers import ModelSerializer

from .models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'
