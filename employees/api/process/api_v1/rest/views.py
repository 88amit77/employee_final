from django.http import Http404
from django.shortcuts import render
from django_filters import rest_framework as dfilters
import django_filters
from django_filters.fields import BaseCSVField, BaseCSVWidget
from django_filters.widgets import BooleanWidget, CSVWidget
from rest_framework import filters, generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api.process.api_v1.rest.serializers import *
from api.process.models import *

# Create your views here.

# Custom Pagination for front_end
class CustomPageNumberPagination(PageNumberPagination):
	page_size_query_param = 'size'  # items per page
	

class ProcessViewset(viewsets.ModelViewSet):
	queryset = Process.objects.all().order_by('-process_id')
	serializer_class = ProcessSerializer
	pagination_class = CustomPageNumberPagination

class ProcessMainidViewset(viewsets.ModelViewSet):
	queryset = ProcessMainid.objects.all().order_by('-process_mainid')
	serializer_class = ProcessMainidSerializer
	pagination_class = CustomPageNumberPagination

class ProcessSubpointViewset(viewsets.ModelViewSet):
	queryset = ProcessSubpoint.objects.all().order_by('-process_subpointid')
	serializer_class = ProcessSubpointSerializer
	pagination_class = CustomPageNumberPagination

class ConnectionsViewset(viewsets.ModelViewSet):
	queryset = Connections.objects.all().order_by('-connector_id')
	serializer_class = ConnectionsSerializer
	pagination_class = CustomPageNumberPagination

class RepeatTaskViewset(viewsets.ModelViewSet):
	queryset = RepeatTask.objects.all().order_by('-repeat_id')
	serializer_class = RepeatTaskSerializer
	pagination_class = CustomPageNumberPagination

class RegularTaskViewset(viewsets.ModelViewSet):
	queryset = RegularTask.objects.all().order_by('-regular_task_id')
	serializer_class = RegularTaskSerializer
	pagination_class = CustomPageNumberPagination

