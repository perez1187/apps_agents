from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework.response import Response

from core_apps.settlements.models import Currency
# from core_apps.results.results.models import Results
# from core_apps.results.reports.models import Reports
# from core_apps.results.deals.models import Clubs

# from .pagination import Pagination10000
from .permissions import IsAgentAndOwner
from .serializers import CurrencyListSerializer

#  currency list
# see all settlements
#  filter by date, by player

#  add settlement

class CurrencyList(APIView):
    """
    List all currencies,
    """
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):
        
        currency = Currency.objects.all()

        # reports_paginate = self.paginate_queryset(reports, request, view=self)
        serializer = CurrencyListSerializer(currency, many=True)

        return Response(serializer.data)
        # return  self.get_paginated_response(serializer.data)