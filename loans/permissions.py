from rest_framework import permissions
from users.models import User
from rest_framework.views import View, Request


class IsBlocked(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_blocked == False


class IsActive(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.data.is_active


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return obj == request.user or request.user.is_superuser and request.user.user_loans.is_active == False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
