from rest_framework import generics,permissions
from rest_framework.views import APIView

from core_apps.results.agents.permissions import IsAgent
from .models import Nicknames
from .serializers import NicknamesListSeriaizer
from .pagination import NicknamePagination


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
    permission_classes = [permissions.IsAuthenticated,IsAgent] 

    def get(self, request, format=None):
        
        nicknames = Nicknames.objects.filter(
            agent__username=request.user
            ).order_by('nickname')

        nicknames_paginate = self.paginate_queryset(nicknames, request, view=self)
        serializer = NicknamesListSeriaizer(nicknames_paginate, many=True)
        return  self.get_paginated_response(serializer.data)

class NicknameDetail(APIView):
    pass
  