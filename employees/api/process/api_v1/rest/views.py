from django.http import Http404
from django.shortcuts import render
# from django_filters import rest_framework as dfilters
# import django_filters
# from django_filters.fields import BaseCSVField, BaseCSVWidget
# from django_filters.widgets import BooleanWidget, CSVWidget
from rest_framework import filters, generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.process.api_v1.rest.serializers import *
from api.process.models import *

# from rest_framework.views import APIView


# Create your views here.

# Custom Pagination for front_end
class CustomPageNumberPagination(PageNumberPagination):
	page_size_query_param = 'size'  # items per page


class CustomModelViewSet(viewsets.ModelViewSet):

	def finalize_response(self, request, response, *args, **kwargs):
		"""
		Returns the final response object.
		Customize response for header and sticky header notes
		"""

		if request.method == "GET":
			response.data['fields_headers'] = self.fields_headers if hasattr(self,'fields_headers') else {}
			# response.data['sticky_header'] = self.sticky_header if hasattr(self, 'sticky_header') else {}
			response.data['dropdowns'] = self.dropdowns if hasattr(self, 'dropdowns') else {}
			# response.data['filter_results_dropdown'] = self.filter_results_dropdown if hasattr(self, 'filter_results_dropdown') else {}
			# Move results to end
			response.data.move_to_end('results') if 'results' in response.data else  response.data
		return super().finalize_response(request, response, *args, **kwargs)

class ProcessViewset(CustomModelViewSet):
	queryset = Process.objects.all().order_by('-process_id')
	serializer_class = ProcessSerializer
	pagination_class = CustomPageNumberPagination
	fields_headers = {
		'process_id': 'Process ID',
		'process_name': 'Process Name',
		'process_description': 'Process Description',
		'process_training': 'Process Training',
		'process_department': 'Process Department',
		'process_time_allocated': 'Process Time Allocated'
		}

class ProcessMainidViewset(CustomModelViewSet):
	
	lookup_field = 'process_id'
	queryset = ProcessMainid.objects.all().order_by('-process_mainid')
	serializer_class = ProcessMainidSerializer
	pagination_class = CustomPageNumberPagination
	fields_headers = {
		'process_mainid': 'Process Main ID',
		'process_id': 'Process ID',
		'main_name': 'Main Name',
		'offsetx': 'Offset X',
		'offsety': 'Offset Y',
		'main_description': 'Main Description',
		'main_department': 'Main Department'
		}
	q1 = Process.objects.all().order_by('-process_id')
	test = []

	for i in q1:
		test.append({'process_id': i.process_id, 'process_name': i.process_name})
	dropdowns = {'process': test}

class ProcessSubpointViewset(CustomModelViewSet):
	queryset = ProcessSubpoint.objects.all().order_by('-process_subpointid')
	serializer_class = ProcessSubpointSerializer
	pagination_class = CustomPageNumberPagination
	fields_headers = {
		'process_subpointid': 'Process Subpoint ID',
		'pmain_id': 'Main Process ID',
		'subpoint_name': 'Subpoint Name',
		'subpoint_attachment': 'Subpoint Attachment',
		'subpoint_description': 'Subpoint Description',
		}
	q1 = ProcessMainid.objects.all().order_by('-process_mainid')
	test = []

	for i in q1:
		test.append({'process_mainid': i.process_mainid, 'main_name': i.main_name})
	dropdowns = {'process_main': test}

class ConnectionsViewset(CustomModelViewSet):
	queryset = Connections.objects.all().order_by('-connector_id')
	serializer_class = ConnectionsSerializer
	pagination_class = CustomPageNumberPagination

	fields_headers = {
		'connector_id': 'Connector ID',
		'start_mainpoint_id': 'Start Point',
		'end_mainpoint_id': 'End Point',
		'connector_text':'Connector Text',
		}

class RepeatTaskViewset(CustomModelViewSet):
	queryset = RepeatTask.objects.all().order_by('-repeat_id')
	serializer_class = RepeatTaskSerializer
	pagination_class = CustomPageNumberPagination
	fields_headers = {
		'repeat_id': 'Repeat ID',
		'repeat_type': 'Repeat Type',
		'interval_repeat': 'Interval Repeat',
		'end_date': 'End Date',
		'weekly_days': 'Weekly Days',
		'monthly_date': 'Monthly Date',
		'yearly_date': 'Yearly Date',
		'yearly_month': 'Yearly Month',
		}

class RegularTaskViewset(CustomModelViewSet):
	queryset = RegularTask.objects.all().order_by('-regular_task_id')
	serializer_class = RegularTaskSerializer
	pagination_class = CustomPageNumberPagination
	fields_headers = {
		'regular_task_id': 'regular task ID',
		'prc_id': 'Process ID',
		'repeat_id': 'Repeat ID',
		'task_name': 'Task Name',
		'task_deptname': 'Task Dept Name',
		'task_type': 'Task Type',
		'members': 'Members',
		'task_description': 'Task Description',
		'task_files': 'Task Files',
		'task_duedate': 'Task Due Date'
		}

	q1 = Process.objects.all().order_by('-process_id')
	q2 = RepeatTask.objects.all().order_by('-repeat_id')
	test = []
	test1 = []

	for i in q1:
		test.append({'process_id': i.process_id, 'process_name': i.process_name})

	for j in q2:
		test1.append({'repeat_id': j.repeat_id, 'repeat_type': j.repeat_type})
	
	dropdowns = {'process_main': test, 'repeat_tasks': test1}