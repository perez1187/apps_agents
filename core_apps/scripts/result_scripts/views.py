# from rest_framework.views import APIView
from django.db import transaction
from rest_framework import generics,permissions,status
from rest_framework.response import Response

from .exceptions import TemplateExcpetion
from .serializers import FileUploadSerializer
from .utils import uploadCSV
from .permissions import IsAgentAndOwner

class CreateResults(generics.CreateAPIView):
    '''
    .csv file.
    Columns:
    - username
    - pass
    - agent

    Permissions:
    - Agent
    '''
    permission_classes = [IsAgentAndOwner]
    serializer_class = FileUploadSerializer
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']

        file_type = str(request.data['file'])[-4:]

        if file_type == '.csv':
            uploadCSV(file, request)
        else:
            raise TemplateExcpetion(
                detail=
                    {"error": "wrong file extension. Upload .csv or .xlsx"}, 
                    status_code=status.HTTP_400_BAD_REQUEST)

        return Response({"status":"file uploaded"},
                        status.HTTP_201_CREATED)    
