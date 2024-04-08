from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.http import Http404

from core_apps.settlements.models import Currency, Settlement
# from core_apps.results.results.models import Results
# from core_apps.results.reports.models import Reports
# from core_apps.results.deals.models import Clubs

# from .pagination import Pagination10000
from .permissions import IsAgentAndOwner
from .serializers import  SettlementListCreateSerializer


class SettlementList(APIView):
    """
    List all agent settlements, or create a new.
    """
    permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        settlements = Settlement.objects.filter(
            player=request.user
        )
        serializer = SettlementListCreateSerializer(settlements, many=True)
        return Response(serializer.data)