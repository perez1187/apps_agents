from django.http import Http404

from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from core_apps.results.agents.permissions import IsAgent
from .models import Reports
from .serializers import AgentReportsListSeriaizer
from .permissions import IsAgentAndOwner


class ReportList(APIView):
    """
    List all reports belongs to Agent,
    """

    permission_classes = [permissions.IsAuthenticated,IsAgentAndOwner] 

    def get(self, request, format=None):
        reports = Reports.objects.filter(agent=request.user)
        serializer = AgentReportsListSeriaizer(reports, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = AgentReportsListSeriaizer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




class ReportView(APIView):
    """
    Retrieve, update or delete a report instance.
    """
    permission_classes = [permissions.IsAuthenticated,IsAgentAndOwner] 

    def get_object(self, pk):
        try:
            obj =  Reports.objects.get(pk=pk)
        except Reports.DoesNotExist:
            raise Http404
        
        #  call has object permissions
        self.check_object_permissions(self.request, obj)  
        return obj          

    def get(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = AgentReportsListSeriaizer(report)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = AgentReportsListSeriaizer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)