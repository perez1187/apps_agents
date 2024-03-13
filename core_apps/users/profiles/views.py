from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Profile
from .serializers import UserProfileSeriaizer

class GetUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]   

    def get(self, request, format=None):
        """
        Return a user profile.
        """

        user_profile = Profile.objects.get(user=request.user)

        serializer = UserProfileSeriaizer(user_profile, many=False)
        return Response(serializer.data)        

        # return Response({"profile":data},status=status.HTTP_200_OK)