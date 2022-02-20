from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AccountViewSet

router = SimpleRouter()
router.register('api/account', AccountViewSet)

urlpatterns = [

]

urlpatterns += router.urls
