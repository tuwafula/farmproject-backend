from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author ==  request.user
     
class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

    # Instance must have an attribute named `owner`.
        return obj.owner == request.user
    # def has_object_permission(self, request, view, obj):
        
    #     if request.user == obj.user :
    #         return True
    #     return False