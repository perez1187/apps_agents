from django.http import Http404

from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Nicknames
from .serializers import NicknamesListSeriaizer, NicknameSeriaizer, NicknameUpdateSeriaizer
from .pagination import NicknamePagination
from .permissions import IsAgentAndOwner


# class NicknamesListView(generics.ListAPIView):
#     '''
#     Nickanmes list
#     '''
#     permission_classes = [permissions.IsAuthenticated,IsAgent]    
#     serializer_class = NicknamesListSeriaizer
#     # pagination_class = [NicknamePagination,]

#     # overwriting query set
#     def get_queryset(self):
#         # https://www.django-rest-framework.org/api-guide/filtering/
#         username = self.request.user
#         queryset = Nicknames.objects.filter(agent__username=username)

#         return queryset

class NicknamesListView(APIView, NicknamePagination):
    """
    List all nicknames belongs to Agent,
    """
    permission_classes = [permissions.IsAuthenticated,IsAgentAndOwner] 

    def get(self, request, format=None):
        
        nicknames = Nicknames.objects.filter(
            agent__username=request.user
            ).order_by('nickname')

        nicknames_paginate = self.paginate_queryset(nicknames, request, view=self)
        serializer = NicknamesListSeriaizer(nicknames_paginate, many=True)
        return  self.get_paginated_response(serializer.data)

class NicknameDetail(APIView):
    """
    Retrieve, update or delete a nickname instance.
    """
    permission_classes = [permissions.IsAuthenticated,IsAgentAndOwner] 

    def get_object(self, pk):

        # print(request.data["id"])
        try:
            obj =  Nicknames.objects.get(pk=pk)
        except Nicknames.DoesNotExist:
            raise Http404
        
        #  call has object permissions
        self.check_object_permissions(self.request, obj)  
        return obj   

    def get(self, request, pk, format=None):
        nickname = self.get_object(pk)
        serializer = NicknameSeriaizer(nickname)
        return Response(serializer.data)        

    def put(self, request, pk, format=None):
        nickname = self.get_object(pk)
        serializer = NicknameUpdateSeriaizer(nickname, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  