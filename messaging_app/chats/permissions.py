from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of a message or conversation to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
