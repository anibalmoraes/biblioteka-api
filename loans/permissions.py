from rest_framework import permissions
from users.models import User
from rest_framework.views import View, Request


class IsBlocked(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        user_not_Is_Blocked = not request.user.is_blocked
        return user_not_Is_Blocked or request.user.is_superuser


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsActive(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_active or request.user.is_superuser


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return obj == request.user or request.user.is_superuser


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.is_superuser


class IsDependecies(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user_not_Is_Blocked = not request.user.user_loans.all()
        return user_not_Is_Blocked or obj == request.user
