from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsUserPermission(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: User):
        return (
            req.user == obj
            and req.user.is_authenticated
            or req.user.is_superuser
            and req.user.is_authenticated
        )
