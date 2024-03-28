from rest_framework.views import APIView


from .pagination import Pagination10000
from .permissions import IsAgentAndOwner

class ReportList(APIView, Pagination10000):
    """
    List all reports belongs to Agent,
    """
    permission_classes = [IsAgentAndOwner] 

    def get(self, request, format=None):

        # agents earnings by report
        #  player earnings by report

        
        reports = Reports.objects.filter(agent=request.user)

        reports_paginate = self.paginate_queryset(reports, request, view=self)
        serializer = AgentReportsListSeriaizer(reports_paginate, many=True)

        # return Response(serializer.data)
        return  self.get_paginated_response(serializer.data)