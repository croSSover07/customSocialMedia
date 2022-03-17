from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CategoryViewSet, CommentViewSet, LikeViewSet

router = SimpleRouter()
router.register('post', PostViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('post/<int:post_id>/comments', CommentViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('post/<int:post_id>/like', LikeViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('post/<int:post_id>/comments/<int:comment_id>/like', LikeViewSet.as_view({'post': 'create', 'get': 'list'})),
]

urlpatterns += router.urls
