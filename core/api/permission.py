from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCurrentUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
