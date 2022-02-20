from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CategoryViewSet

router = SimpleRouter()
router.register('api/post', PostViewSet)
router.register('api/category', CategoryViewSet)

urlpatterns = [

]

urlpatterns += router.urls
