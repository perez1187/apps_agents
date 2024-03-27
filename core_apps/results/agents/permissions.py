from rest_framework import permissions

class IsAgent(permissions.BasePermission):

    message = "You are not Agent" 

    def has_permission(self, request, view):

        # if request.user.is_superuser:
        #     return True
        
        return request.user.is_agent

class IsAgentAndOwner(permissions.BasePermission):

    message = "You dont have permissions" 

    def has_permission(self, request, view):
        
        return request.user.is_agent

    def has_object_permission(self, request, view, obj):

        # Instance must have an attribute named `owner`.
        return obj.agent == request.user




