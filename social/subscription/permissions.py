from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            (obj.owner == request.user or obj.author == request.user)
        )