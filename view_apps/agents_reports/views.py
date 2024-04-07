from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework import generics,permissions,status

from rest_framework.response import Response

from .pagination import Pagination10000, Pagination100
from .permissions import IsAgentAndOwner
from .serializers import ReportsListSerializer, ResultListSerializer, ResultUpdateSerializer

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results

class ReportList(APIView,Pagination10000):
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):
        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01')  
        if from_date =="":
            from_date ="2000-03-20"
        if to_date=="":
            to_date =    '2100-01-01'                 

        # clubs = Clubs.objects.all()
        reports = Reports.objects.filter(
            Q(agent=request.user),
            Q(report_date__range=[from_date,to_date]),
        )
        # .values("club").distinct()
        
        reports_paginate = self.paginate_queryset(reports, request, view=self)
        serializer = ReportsListSerializer(reports_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data) 

class ResultList(APIView, Pagination100):
    permission_classes = [IsAgentAndOwner] 
    def get(self, request, format=None):    
        from_date = request.GET.get('from_date','2000-03-20')
        to_date = request.GET.get('to_date','2100-01-01')  
        if from_date =="":
            from_date ="2000-03-20"
        if to_date=="":
            to_date =    '2100-01-01'                  

        results = Results.objects.filter(
            Q(report__agent=request.user),
            Q(report__report_date__range=[from_date,to_date]),
        )

        results_paginate = self.paginate_queryset(results, request, view=self)
        serializer = ResultListSerializer(results_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data) 

class ResultUpdateView(APIView):
    """
    Retrieve, update or delete a nickname instance.
    """
    permission_classes = [IsAgentAndOwner] 

    def get_object(self, pk):

        # print(request.data["id"])
        try:
            obj =  Results.objects.get(pk=pk)
        except Results.DoesNotExist:
            raise Http404
        
        #  call has object permissions
        self.check_object_permissions(self.request, obj)  
        return obj   

    # def get(self, request, pk, format=None):
    #     result = self.get_object(pk)
    #     #########
    #     serializer = NicknameSeriaizer(nickname)
    #     return Response(serializer.data)        

    def put(self, request, pk, format=None):
        result = self.get_object(pk)

        serializer = ResultUpdateSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        