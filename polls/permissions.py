from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
        
        
        
class IsSession(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        """
        Если установленна сессия то разрешаем доступ
        Если пользователь анонимный проверяем соответвует ли сессия в запросе сесси под которой сохранен объект
        Если пользователь не анонимный проверяем пользователя который указан на соответвие.
        """
        return obj.owner == request.user
