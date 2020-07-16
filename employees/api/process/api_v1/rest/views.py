import datetime
import math

import psycopg2
import requests
from django.db import connection
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render
from django_filters import rest_framework as dfilters
from rest_framework import filters, generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.process.api_v1.rest.serializers import *
from api.process.models import *

# import django_filters



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
			# response.data['sticky_header'] = self.sticky_header if hasattr(self, 'sticky_header') else{}
			response.data['dropdowns'] = self.dropdowns if hasattr(self, 'dropdowns') else{}
			# response.data['filter_results_dropdown'] = self.filter_results_dropdown if hasattr(self, 'filter_results_dropdown') else {}

			# Move results to end
			response.data.move_to_end('results') if 'results' in response.data else response.data

		return super().finalize_response(request, response, *args, **kwargs)

class ProcessViewset(CustomModelViewSet):
	lookup_field = 'process_id'
	queryset = Process.objects.all().order_by('-process_id')
	serializer_class = ProcessSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'process_id': 'Process ID',
	# 	'process_name': 'Process Name',
	# 	'process_description': 'Process Description',
	# 	'process_training': 'Process Training',
	# 	'process_department': 'Process Department',
	# 	'process_time_allocated': 'Process Time Allocated'
	# }
	test1 = []
	test2 = []
	test3 = []
	test4 = []

	query = Process.objects.filter().prefetch_related('process_department__dept_name').values('process_name', 'process_department__dept_name', 'process_id').order_by('-process_id')

	# url = 'https://buymore2api.sellerbuymore.com/employee/process/process_list/'
	# resultant = requests.get(url)
	# response = resultant.json()['results']

	for j in query:
		if j['process_department__dept_name'] == 'HR':
			test1.append({'process_name': j['process_name'], 'process_id': j['process_id']})
		elif j['process_department__dept_name'] == 'Software':
			test2.append({'process_name': j['process_name'], 'process_id': j['process_id']})
		elif j['process_department__dept_name'] == 'Managerial':
			test3.append({'process_name': j['process_name'], 'process_id': j['process_id']})
		elif j['process_department__dept_name'] == 'Warehouse':
			test4.append({'process_name': j['process_name'], 'process_id': j['process_id']})
		else:
			pass
	# parse data from API to populate dropdowns
	# for j in response:
	# 	if j['process_department'] == 'HR':
	# 		test1.append({'process_name': j['process_name'], 'process_id': j['process_id']})
	# 	elif j['process_department'] == 'Software':
	# 		test2.append({'process_name': j['process_name'], 'process_id': j['process_id']})
	# 	elif j['process_department'] == 'Managerial':
	# 		test3.append({'process_name': j['process_name'], 'process_id': j['process_id']})
	# 	elif j['process_department'] == 'Warehouse':
	# 		test4.append({'process_name': j['process_name'], 'process_id': j['process_id']})
	# 	else:
	# 		pass

	dropdowns = {'HR': test1, 'Software': test2, 'Managerial': test3, 'Warehouse': test4}


class ProcessMainidViewset(CustomModelViewSet):

	lookup_field = 'process_mainid'
	queryset = ProcessMainid.objects.all().order_by('-process_mainid')
	serializer_class = ProcessMainidSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'process_mainid': 'Process Main ID',
	# 	'process_id': 'Process ID',
	# 	'main_name': 'Main Name',
	# 	'offsetx': 'Offset X',
	# 	'offsety': 'Offset Y',
	# 	'main_description': 'Main Description',
	# 	'main_department': 'Main Department'
	# }
	filter_backends = (dfilters.DjangoFilterBackend,)
	filterset_fields = ('process_id',)
	q1 = Process.objects.all().order_by('-process_id')
	test = []

	for i in q1:
		test.append({'process_id': i.process_id, 'process_name': i.process_name})

	dropdowns = {'process': test}


class ProcessSubpointViewset(CustomModelViewSet):
	lookup_field = 'process_subpointid'
	queryset = ProcessSubpoint.objects.all().order_by('-process_subpointid')
	serializer_class = ProcessSubpointSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'process_subpointid': 'Process Subpoint ID',
	# 	'pmain_id': 'Main Process ID',
	# 	'subpoint_name': 'Subpoint Name',
	# 	'subpoint_attachment': 'Subpoint Attachment',
	# 	'subpoint_description': 'Subpoint Description',
	# }
	filter_backends = (dfilters.DjangoFilterBackend,)
	filterset_fields = ('pmain_id',)
	q1 = ProcessMainid.objects.all().order_by('-process_mainid')
	test = []

	for i in q1:
		test.append({'process_mainid': i.process_mainid, 'main_name': i.main_name})

	dropdowns = {'process_main': test}

class ConnectionsViewset(CustomModelViewSet):
	lookup_field = 'connector_id'
	queryset = Connections.objects.all().order_by('-connector_id')
	serializer_class = ConnectionsSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'connector_id': 'Connector ID',
	# 	'connection_process': 'Process',
	# 	'start_mainpoint_id': 'Start Point',
	# 	'end_mainpoint_id': 'End Point',
	# 	'connector_text':'Connector Text',
	# }

	filter_backends = (dfilters.DjangoFilterBackend,)
	filterset_fields = ('connection_process',)

	q1 = Process.objects.all().order_by('-process_id')
	test = []

	for i in q1:
		test.append({'process_id': i.process_id, 'process_name': i.process_name})

	dropdowns = {'process': test}

class RepeatTaskViewset(CustomModelViewSet):
	lookup_field = 'repeat_id'
	queryset = RepeatTask.objects.all().order_by('-repeat_id')
	serializer_class = RepeatTaskSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'repeat_id': 'Repeat ID',
	# 	'repeat_type': 'Repeat Type',
	# 	'interval_repeat': 'Interval Repeat',
	# 	'end_date': 'End Date',
	# 	'weekly_days': 'Weekly Days',
	# 	'monthly_date': 'Monthly Date',
	# 	'yearly_date': 'Yearly Date',
	# 	'yearly_month': 'Yearly Month',
	# }

class RegularTaskViewset(CustomModelViewSet):
	lookup_field = 'regular_task_id'
	queryset = RegularTask.objects.all().order_by('-regular_task_id')
	serializer_class = RegularTaskSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'regular_task_id': 'regular task ID',
	# 	'prc_id': 'Process ID',
	# 	'task_name': 'Task Name',
	# 	'task_deptname': 'Task Dept Name',
	# 	'task_type': 'Task Type',
	# 	'members': 'Members',
	# 	'task_description': 'Task Description',
	# 	'task_files': 'Task Files',
	# 	'task_duedate': 'Task Due Date',
	# 	'cron': 'Cron Expression'
	# }

	q1 = Process.objects.all().order_by('-process_id')
	# q2 = RepeatTask.objects.all().order_by('-repeat_id')
	test = []
	# test1 = []

	for i in q1:
		test.append({'process_id': i.process_id, 'process_name': i.process_name})

	# for j in q2:
	# 	test1.append({'repeat_id': j.repeat_id, 'repeat_type': j.repeat_type})

	dropdowns = {'process_main': test}


class DeptViewset(CustomModelViewSet):
	lookup_field = 'dept_id'
	queryset = Departments.objects.all().order_by('-dept_id')
	serializer_class = DeptSerializer
	pagination_class = CustomPageNumberPagination
	# fields_headers = {
	# 	'dept_id': 'Department ID',
	# 	'dept_name': 'Department Name'
	# }


# class TemplateViewset(CustomModelViewSet):
# 	lookup_field = 'template_id'
# 	queryset = Templates.objects.all().order_by('-template_id')
# 	serializer_class = TemplateSerializer
# 	pagination_class = CustomPageNumberPagination
# 	fields_headers = {
# 		'template_id': 'Template ID',
# 		'template_name': 'Template Name',
# 		'depts_template': 'Department'
# 	}
# 	test1 = []
# 	test2 = []
# 	test3 = []
# 	test4 = []

# 	# ORM Query
# 	# query = Templates.objects.filter().prefetch_related('depts_template__dept_name').values('template_name', 'depts_template__dept_name', 'template_id').order_by('-template_id')

# 	# for j in query:
# 	# 	if j['depts_template__dept_name'] == 'HR':
# 	# 		test1.append({'template_name': j['template_name'], 'template_id': j['template_id']})
# 	# 	elif j['depts_template__dept_name'] == 'Software':
# 	# 		test2.append({'template_name': j['template_name'], 'template_id': j['template_id']})
# 	# 	elif j['depts_template__dept_name'] == 'Managerial':
# 	# 		test3.append({'template_name': j['template_name'], 'template_id': j['template_id']})
# 	# 	elif j['depts_template__dept_name'] == 'Warehouse':
# 	# 		test4.append({'template_name': j['template_name'], 'template_id': j['template_id']})
# 	# 	else:
# 	# 		pass

# 	# Raw query
# 	cursor = connection.cursor()
# 	rquery = "SELECT process_departments.dept_name, process_templates.template_name, process_templates.template_id FROM public.process_templates, public.process_departments WHERE process_templates.depts_template_id = process_departments.dept_id ORDER BY process_departments.dept_name"
# 	cursor.execute(rquery)
# 	res = cursor.fetchall()
# 	column_names = [desc[0] for desc in cursor.description]
# 	results_data = []
# 	if res is not None:
# 		for single_record in res:
# 			results_data.append(dict(zip(column_names, single_record)))

# 	for i in results_data:
# 		if i['dept_name'] == 'HR':
# 			test1.append({'template_name': i['template_name'], 'template_id': i['template_id']})
# 		elif i['dept_name'] == 'Software':
# 			test2.append({'template_name': i['template_name'], 'template_id': i['template_id']})
# 		elif i['dept_name'] == 'Managerial':
# 			test3.append({'template_name': i['template_name'], 'template_id': i['template_id']})
# 		elif i['dept_name'] == 'Warehouse':
# 			test4.append({'template_name': i['template_name'], 'template_id': i['template_id']})
# 		else:
# 			pass

# 	dropdowns = {'HR': test1, 'Software': test2, 'Managerial': test3, 'Warehouse': test4}
