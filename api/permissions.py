from rest_framework.permissions import BasePermission


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

        return bool(request.method in SAFE_METHODS or request.user.is_authenticated)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
