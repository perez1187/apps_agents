from rest_framework import permissions

class IsAgent(permissions.BasePermission):

    message = "You are not Agent" 

    def has_permission(self, request, view):

        # if request.user.is_superuser:
        #     return True
        
        return request.user.is_agent



