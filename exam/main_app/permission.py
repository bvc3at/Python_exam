from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class HasAuth(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_anonymous == True