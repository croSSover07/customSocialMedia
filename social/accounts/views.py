from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Account
from rest_framework.viewsets import ModelViewSet


# Create your views here.
from .serializers import AccountSerializer
from .tasks import send_information_email


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

    def perform_create(self, serializer):
        super().perform_create(serializer)
        send_information_email.delay(self.kwargs.get('email'))


