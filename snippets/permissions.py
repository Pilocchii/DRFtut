from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an obj to edit
    """

    def has_object_permission(self, request, view, obj):
        #read permissions are allowed to any req, so get head and options req are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions only allowed to owner
        return obj.owner == request.user