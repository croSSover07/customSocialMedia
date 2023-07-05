from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AccountViewSet

router = SimpleRouter()

urlpatterns = [
    path('account/', AccountViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('account/<int:id>', AccountViewSet.as_view({'DELETE': 'destroy'})),
]

urlpatterns += router.urls
