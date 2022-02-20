from .models import Account
from rest_framework.viewsets import ModelViewSet


# Create your views here.
from .serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
