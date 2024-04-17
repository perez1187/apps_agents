from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from core_apps.settlements.models import Currency, Settlement
# from core_apps.results.results.models import Results
# from core_apps.results.reports.models import Reports
# from core_apps.results.deals.models import Clubs

# from .pagination import Pagination10000
from .permissions import IsAgentAndOwner
from .serializers import CurrencyListSerializer, SettlementListCreateSerializer

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




class CreateSettlement(APIView):
    """
    List all agent settlements, or create a new.
    """
    permission_classes = [IsAgentAndOwner] 
    # def get(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):

        serializer = SettlementListCreateSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            obj = Settlement.objects.create(
                agent = request.user,
                player_id=request.data['player'],
                date=request.data['date'],
                transactionUSD= request.data["transactionUSD"],
                transactionValue=request.data["transactionValue"],
                currency_id=request.data["currency"],
                exchangeRate=request.data["exchangeRate"],
                description=request.data["description"]
            )            
            # print("valid")

            return Response({"status":"settlement create"}, status=status.HTTP_201_CREATED)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

class SettlementList(APIView):
    """
    List all agent settlements, or create a new.
    """
    permission_classes = [IsAgentAndOwner] 
    def get(self, request, format=None):
        settlements = Settlement.objects.filter(
            agent=request.user
        )
        serializer = SettlementListCreateSerializer(settlements, many=True)
        return Response(serializer.data)

class DeleteSettlement(APIView):
    permission_classes = [IsAgentAndOwner]
    def get_object(self, pk):
        try:
            obj =  Settlement.objects.get(pk=pk)
        except Reports.DoesNotExist:
            raise Http404
        
        #  call has object permissions
        self.check_object_permissions(self.request, obj)  
        return obj                

    def delete(self, request, pk, format=None):
        settlement = self.get_object(pk)
        settlement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        