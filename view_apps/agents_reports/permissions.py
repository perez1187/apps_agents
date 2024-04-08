from rest_framework import permissions

class IsAgentAndOwner(permissions.BasePermission):

    message = "You dont have permissions" 

    def has_permission(self, request, view):
        
        return request.user.is_agent

    def has_object_permission(self, request, view, obj):

        # Instance must have an attribute named `owner`.
        return obj.nickname_fk.agent == request.user



