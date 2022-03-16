from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CategoryViewSet, CommentViewSet

router = SimpleRouter()
router.register('post', PostViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('post/<int:post_id>/comments', CommentViewSet.as_view({'post': 'create', 'get': 'list'})),
]

urlpatterns += router.urls
