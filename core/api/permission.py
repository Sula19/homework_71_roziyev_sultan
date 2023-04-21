from rest_framework.permissions import BasePermission
from instagram.models import Post


class IsCurrentUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
