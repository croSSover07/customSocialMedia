from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SubscriptionViewSet, MySubscriptionViewSet

router = SimpleRouter()

urlpatterns = [
    path('subscription/subscribe/<int:author_id>', SubscriptionViewSet.as_view({'post': 'create',})),
    path('subscription/my', MySubscriptionViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls
