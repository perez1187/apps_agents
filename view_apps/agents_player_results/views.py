from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery, Sum, Q
from rest_framework import generics,permissions,status

from rest_framework.response import Response

from .pagination import Pagination10000, Pagination100
from .permissions import IsAgentAndOwner
from .serializers import ReportsListSerializer, ResultListSerializer, ResultUpdateSerializer

from core_apps.results.reports.models import Reports
from core_apps.results.results.models import Results


# player lists
# agent_deals.views.py
#  api/views/agents-deals/players-list/