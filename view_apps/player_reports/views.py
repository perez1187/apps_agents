from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework import generics,permissions,status
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from .pagination import Pagination10000, Pagination100
from .permissions import IsAgentAndOwner
from .serializers import ResultListSerializer

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results


class ResultList(APIView, Pagination100):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):    
        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01')  
        if from_date =="":
            from_date ="2000-03-20"
        if to_date=="":
            to_date =    '2100-01-01'                  

        results = Results.objects.filter(
            Q(nickname_fk__player=request.user),
            Q(report__report_date__range=[from_date,to_date]),
        )

        results_paginate = self.paginate_queryset(results, request, view=self)
        serializer = ResultListSerializer(results_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data) 