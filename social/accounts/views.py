from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Account
from rest_framework.viewsets import ModelViewSet


# Create your views here.
from .serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'POST':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
