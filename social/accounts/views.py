from django.http import Http404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

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
        elif self.request.method == 'DELETE':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def delete(self, request, id):
        account = Account.objects.filter(id=id).first()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        print(id)
        if request.user != account:
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data="You cannot delete yourself")

    def perform_create(self, serializer):
        super().perform_create(serializer)
        send_information_email.delay(self.kwargs.get('email'))

    def destroy(self, request, *args, **kwargs):
        account_id = kwargs.get('id')
        return self.delete(self, request, id=account_id)
