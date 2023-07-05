import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.models import Account
from subscription.models import Subscription
from subscription.permissions import IsOwnerOrAuthor
from subscription.serializers import SubscriptionReadSerializer, SubscriptionWriteSerializer


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAuthor]

    def perform_create(self, serializer):
        author_id = self.kwargs.get('author_id')

        serializer.save(
            created_at=datetime.datetime.now(),
            owner=self.request.user,
            author=Account.objects.filter(id=author_id).first()
        )

    def create(self, request, *args, **kwargs):
        author_id = self.kwargs.get('author_id')
        owner = self.request.user
        author = Account.objects.filter(id=author_id).first()

        if author_id == owner.id:
            return Response(f'You cannot subscribe to yourself', status=status.HTTP_400_BAD_REQUEST)
        if author_id is None or author is None:
            return Response(f'Error, author_id is empty', status=status.HTTP_400_BAD_REQUEST)

        return super().create(request=request, args=args, kwargs=kwargs)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SubscriptionReadSerializer
        else:
            return SubscriptionWriteSerializer


class MySubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAuthor]
    serializer_class = SubscriptionReadSerializer

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


