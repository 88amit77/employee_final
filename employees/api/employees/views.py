from rest_framework import viewsets
from rest_framework import generics
import csv
from rest_framework import filters
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import status
import requests
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import (Employee, Education, Documents, FamilyMembers, WorkHistory, LeaveRules, EmpLeaveApplied, EmpLeaveId,
                     Attendance, AttendenceLeaveid, Attendence_rules, MonthlyEmpSalary, Salary)
from .serializers import (
      PersonalSerializer,
      EmployeeSerializer,
      ListEmployeeSerializer,
      EducationSerializer,
      DocumentsSerializer,
      FamilyMembersSerializer,
      WorkHistorySerializer,
      EmployeeColumnModelSerializer,
      DynamicFieldsModelSerializer,
      LeaveRulesSerializer,
      Employee1Serializer,
      ListEmployee1Serializer,
      EmpLeaveAppliedSerializer,
      EmpLogSerializer,
      EmployeenewSerializer,
      Employee2Serializer,
AttendaceSerializer,
    AttendaceLeaveidSerializer,
EnterAttendanceSerializer,
AttendaceRulesSerializer,
UpdateAttendanceLogSerializer,
ListAttendanceLogSerializer,
CreateMonthlyEmpSalarySerializer,
ListMonthlyEmpSalarySerializer,
DynamicFieldsMonthlyEmpSalaryModelSerializer,
SearchAttendanceLogSerializer,
ListAssignedAttendanceRuleSerializer,
ListAssignedRuleSerializer,
Emp1Serializer,
EmpLog2Serializer,
CreateEmpSalarySerializer,
# ListEmpSalarySerializer,
SearchBydateAttendanceLogSerializer,
PayrollRunSerializer,
PayrollSearchSerializer

)

DEFAULT_PAGE = 1


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                                'emp_id',
                                'name',
                                         ],
                'header': {
                             'emp_id': 'Employee Id',
                             'name': 'Employee Name',
                             'permanent_address_line1': "Address",
                             "designation": 'Designation',
                             "gender": "Gender",
                             "official_email": 'Official Email',
                             "date_of_joining": 'Date of Joining',
                             'department': "Department",
                             "official_number": 'Phone',
                             'dob': 'Date of Birth',
                             "work_location_add": 'Work Location',
                           },
                'sortable': [
                              'emp_id',
                           ],
                'date_filters': [
                   'date_of_joining', 'dob'
                                ]
            },
            'results': data
        })


class CustomLeaveRulesPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                               'emp_id',
                               'name',
                                         ],
                'header': {
                              'emp_id': 'Employee Id',
                              'name': 'Employee Name',
                              "designation": 'Designation',
                              'date_of_joining': 'Date Of Joining',
                              "employee_type": 'Employee Type',
                              'work_location_add': 'Work Location Add',
                              'leave_id': 'Leave ID',

                           },
                'sortable': [
                              'emp_id',
                           ],
               'date_filters': [
                   'date_of_joining'
               ]
            },
            'results': data
        })

class CustomLeaveLogsPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                               'emp_id',
                               'name',
                                         ],
                'header': {
                              'emp_id': 'Employee Id',
                              'name': 'Employee Name',
                              "department": 'Department',
                              'leave_id': 'Type',
                              "start_date": 'Start Date',
                              'end_date': 'End Date',
                              "days": 'Days',
                              'status': 'Status',

                           },
                'sortable': [
                              'emp_id',
                           ],
               'date_filters': [
                   'start_date'
                   'end_date'
               ]
            },
            'results': data
        })

class CustomAttendanceLogPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                               'emp_id',
                               'name',
                                         ],
                'header': {
                              'emp_id': 'Employee Id',
                              'name': 'Employee Name',
                              "department": 'Department',
                              "work_location_add": 'Location',
                              "annomaly": 'Outstanding Anomalies',
                              "status": 'Status',
                              'work_date': 'Work Date',
                              "login": 'In Time',
                              "logout": 'Out Time',


                           },
                'sortable': [
                              'emp_id',
                           ],
            },
            'results': data
        })


class CustomAttendanceRulePagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                               'emp_id',
                               'name',
                                         ],
                'header': {
                              'emp_id': 'Employee Id',
                              'name': 'Employee Name',
                              "department": 'Department',
                              "employee_type": 'Type',
                               'attenadance_leaveids':'Attenadance Leave Data',

 },


            },
            'results': data
        })

class CustomPayrollPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                               'emp_id',
                               'name',
                                         ],
                'header': {
                            'emp_id':'Emp ID',
                            'name': 'Employee Name',
                            "department": 'Department',
                            "month": "Month",
                            "lop": 'Lop',
                            "no_of_days": 'No Of Days',
                            "ctc": 'CTC',
                            "basic": 'Basic',
                            "hra": 'HRA',
                            "conveyance_allowances": 'Conveyance Allowances',
                            "medical_allowance": 'Medical Allowance',
                            "cca_allowance": 'CCA Allowance',
                            "pf_employer": 'PF Employer',
                            "pf_employee": 'PF Employee',
                            "pt": 'PT',
                            "esi_employer": 'ESI Employer',
                            "esi_employee": 'ESI Employee',
                            "net_employee_payable": 'Net Employee Payable',
                            "due_date": 'Due Date',
                            "special_allowances": "Special Allowances",
                            "over_time": "Over Time",
                            "deductions": "Deductions",
                            "reimbursements": "Reimbursements",

                           },
                'searchable': [
                    'emp_id',
                    'name',
                    'department',
                    "month",
                    "lop",
                    "no_of_days",
                    "ctc",
                    "basic",
                    "hra",
                    "conveyance_allowances",
                    "medical_allowance",
                    "cca_allowance",
                    "pf_employer",
                    "pf_employee",
                    "pt",
                    "esi_employer",
                    "esi_employee",
                    "net_employee_payable",
                    "due_date",
                    "special_allowances",
                    "over_time",
                    "deductions",
                    "reimbursements",
                ],
                'sortable': [
                              'emp_id',
                              'name',
                              'department',
                              "month",
                              "lop",
                                "no_of_days",
                                "ctc",
                                "basic",
                                "hra",
                                "conveyance_allowances",
                                "medical_allowance",
                                "cca_allowance",
                                "pf_employer",
                                "pf_employee",
                                "pt",
                                "esi_employer",
                                "esi_employee",
                                "net_employee_payable",
                                "due_date",
                                "special_allowances",
                                "over_time",
                                "deductions",
                                "reimbursements",
                           ],
                'date_filters': [
                    'due_date'
                ]

            },
            'results': data
        })



class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = PersonalSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ListEmployeeViewSet(viewsets.ViewSet):
    pagination_class = CustomPagination
    def create(self, request):
        queryset = Employee.objects.all()
        serializer = ListEmployeeSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListEmployeeSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class EmployeeSearchViewSet(viewsets.ModelViewSet):

    serializer_class = ListEmployeeSerializer
    pagination_class = CustomPagination
    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.all()
        query = self.request.GET.get("keyword")

        if query:
            qs = qs.filter(Q(name__contains=query) | Q(emp_id__contains=query) | Q(official_email__contains=query)
                           | Q(permanent_address_line1__contains=query) | Q(designation__contains=query)
                           | Q(gender__contains=query) | Q(official_email__contains=query) | Q(date_of_joining__contains=query)
                           | Q(department__contains=query) | Q(official_number__contains=query)
                           | Q(dob__contains=query) | Q(work_location_add__contains=query))
        query = self.request.GET.get("emp_id")
        if query:
            emp_id = query.split(',')
            qs = qs.filter(emp_id__in=emp_id)
        query = self.request.GET.get("name")
        if query:
            name = query.split(',')
            qs = qs.filter(name__in=name)
        query = self.request.GET.get("permanent_address_line1")
        if query:
            Permanent_address_line1 = query.split(',')
            qs = qs.filter(Permanent_address_line1__in=Permanent_address_line1)
        query = self.request.GET.get("designation")
        if query:
            designation = query.split(',')
            qs = qs.filter(designation__in=designation)
        query = self.request.GET.get("gender")
        if query:
            gender = query.split(',')
            qs = qs.filter(gender__in=gender)
        query = self.request.GET.get("official_email")
        if query:
            official_email = query.split(',')
            qs = qs.filter(official_email__in=official_email)
        query = self.request.GET.get("date_of_joining")
        if query:
            date_of_joining = query.split(',')
            qs = qs.filter(date_of_joining__in=date_of_joining)
        query = self.request.GET.get("department")
        if query:
            department = query.split(',')
            qs = qs.filter(department__in=department)
        query = self.request.GET.get("official_number")
        if query:
            official_number = query.split(',')
            qs = qs.filter(official_number__in=official_number)
        query = self.request.GET.get("dob")
        if query:
            dob = query.split(',')
            qs = qs.filter(dob__in=dob)
        query = self.request.GET.get("work_location_add")
        if query:
            work_location_add = query.split(',')
            qs = qs.filter(work_location_add__in=work_location_add)
        query = self.request.GET.get("sort_by")
        if query:
            sort_key = query
            if sort_key == 'emp_id':
                sort_key = 'emp_id'
            sort_by = ''
            if 'sort_order' in self.request.data and self.request.data['sort_order'] == 'desc':
                sort_by = '-'
            sort_by += sort_key
            qs = qs.order_by(sort_by)

        return qs






class EmployeeColumnViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeColumnModelSerializer
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.all()
        query = self.request.GET.get("fields")
        if query:
            return qs
        else:
            return qs


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    pagination_class = CustomPagination


class FamilyMembersViewSet(viewsets.ModelViewSet):
    queryset = FamilyMembers.objects.all()
    serializer_class = FamilyMembersSerializer
    pagination_class = CustomPagination


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    pagination_class = CustomPagination


class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    pagination_class = CustomPagination


class LeaveRulesView(viewsets.ModelViewSet):
    queryset = LeaveRules.objects.all()
    serializer_class = LeaveRulesSerializer


class EmployeeView(viewsets.ModelViewSet):
    queryset = EmpLeaveId.objects.all()
    serializer_class = Employee1Serializer
    pagination_class = CustomLeaveRulesPagination

class AssignRulesSearchViewSet(viewsets.ModelViewSet):

    serializer_class = Employee1Serializer
    pagination_class = CustomLeaveRulesPagination

    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.all()
        query = self.request.GET.get("keyword")
        if query:
            qs = qs.filter(Q(name__contains=query) | Q(emp_id__contains=query) | Q(official_email__contains=query))
        query = self.request.GET.get("emp_id")
        if query:
            emp_id = query.split(',')
            qs = qs.filter(emp_id__in=emp_id)

        query = self.request.GET.get("name")
        if query:
            name = query.split(',')
            qs = qs.filter(name__in=name)
        query = self.request.GET.get("official_email")
        if query:
            official_email = query.split(',')
            qs = qs.filter(official_email__in=official_email)
        query = self.request.GET.get("sort_by")
        if query:
            sort_key = query
            if sort_key == 'emp_id':
                sort_key = 'emp_id'
            sort_by = ''
            if 'sort_order' in self.request.data and self.request.data['sort_order'] == 'desc':
                sort_by = '-'
            sort_by += sort_key
            qs = qs.order_by(sort_by)

        return qs


class AssignRulesColumnViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    serializer_class = DynamicFieldsModelSerializer
    pagination_class = CustomLeaveRulesPagination

    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.all()
        query = self.request.GET.get("fields")
        if query:
            return qs
        else:
            return qs


class ListAssignRulesViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = Employee.objects.all()
        serializer = ListEmployee1Serializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomLeaveRulesPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListEmployee1Serializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomLeaveRulesPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)
#list assigned rule page
class ListAssignedRuleView(viewsets.ViewSet):

    def create(self, request):
        queryset = EmpLeaveId.objects.all()
        serializer = ListAssignedRuleSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomLeaveRulesPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListAssignedRuleSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomLeaveRulesPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)
class EmpLeaveAppliedView(viewsets.ModelViewSet):
    queryset = EmpLeaveApplied.objects.all()
    serializer_class = EmpLeaveAppliedSerializer


class EmpLogView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeenewSerializer


class EmployeeLogView(viewsets.ModelViewSet):
    queryset = EmpLeaveApplied.objects.all()
    serializer_class = EmpLogSerializer


class ListLeaveLogsViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeenewSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomLeaveLogsPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = EmployeenewSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomLeaveLogsPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class LeaveLogsSearchViewSet(viewsets.ModelViewSet):

    serializer_class = Employee2Serializer
    pagination_class = CustomLeaveLogsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.all()
        query = self.request.GET.get("keyword")
        if query:
            qs = qs.filter(Q(name__contains=query) | Q(emp_id__contains=query) | Q(department__contains=query))
        query = self.request.GET.get("emp_id")
        if query:
            emp_id = query.split(',')
            qs = qs.filter(emp_id__in=emp_id)

        query = self.request.GET.get("name")
        if query:
            name = query.split(',')
            qs = qs.filter(name__in=name)
        query = self.request.GET.get("department")
        if query:
            department = query.split(',')
            qs = qs.filter(department__in=department)
        query = self.request.GET.get("sort_by")
        if query:
            sort_key = query
            if sort_key == 'emp_id':
                sort_key = 'emp_id'
            sort_by = ''
            if 'sort_order' in self.request.data and self.request.data['sort_order'] == 'desc':
                sort_by = '-'
            sort_by += sort_key
            qs = qs.order_by(sort_by)

        return qs
#test
class EmployeeLoggView(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = EmpLeaveApplied.objects.all()
        serializer = EmpLog2Serializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomLeaveLogsPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = EmpLog2Serializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomLeaveLogsPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class EmpNameView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Emp1Serializer

#attendance
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendaceSerializer
    pagination_class = CustomAttendanceLogPagination


class AttendanceLeaveidViewSet(viewsets.ModelViewSet):
    queryset = AttendenceLeaveid.objects.all()
    serializer_class = AttendaceLeaveidSerializer
    pagination_class = CustomAttendanceLogPagination
class AttendenceRulesViewSet(viewsets.ModelViewSet):
    queryset = Attendence_rules.objects.all()
    serializer_class = AttendaceRulesSerializer
    pagination_class = CustomAttendanceLogPagination

class EnterAttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = EnterAttendanceSerializer
    pagination_class = CustomAttendanceLogPagination


class ListAssignedAttendanceRuleView(viewsets.ViewSet):

    def create(self, request):
        queryset = AttendenceLeaveid.objects.all()
        serializer = ListAssignedAttendanceRuleSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomAttendanceRulePagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListAssignedAttendanceRuleSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomAttendanceRulePagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class SearchAttendanceLogAPIView(viewsets.generics.ListCreateAPIView):
    search_fields = ['name', 'emp_id', 'department', 'work_location_add']
    ordering_fields = ['emp_id']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Employee.objects.all()
    serializer_class = SearchAttendanceLogSerializer
    pagination_class = CustomAttendanceLogPagination

###for search by date
# class SearchByDateAttendanceLogViewSet(viewsets.ModelViewSet):
#         search_fields = [
#             'attendances__work_date',
#         ]
#         filter_backends = (filters.SearchFilter,)
#         queryset = Employee.objects.all()
#         serializer_class = SearchBydateAttendanceLogSerializer
#         pagination_class = CustomAttendanceLogPagination

##test attendance search date between for attendance log

from dateutil.parser import parse
from rest_framework import generics

# class SearchByDateBetweenAttendanceLog(generics.ListAPIView):
#     serializer_class = SearchBydateAttendanceLogSerializer
#     pagination_class = CustomAttendanceLogPagination
#
#     def get_queryset(self):
#         filter = {}
#         """
#         Optionally restricts the returned data to a given date,
#         by filtering against a `start_date` query parameter in the URL(?start_date=01-01-2021).
#         """
#         queryset = Employee.objects.all()
#         start_date = self.request.query_params.get('start_date', None)
#         end_date = self.request.query_params.get('end_date', None)
#         if start_date is not None:
#             filter['attendances__work_date__gte'] = parse(start_date)
#         if end_date is not None:
#            filter['attendances__work_date__lte'] = parse(end_date)
#
#         queryset = queryset.filter(**filter)
#         return queryset

class SearchByDateBetweenAttendanceLog(generics.ListAPIView):
    serializer_class = AttendaceSerializer
    pagination_class = CustomAttendanceLogPagination

    def get_queryset(self):
        filter = {}
        """
        Optionally restricts the returned data to a given date,
        by filtering against a `start_date` query parameter in the URL(?start_date=01-01-2021).
        """
        queryset = Attendance.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date is not None:
            filter['work_date__gte'] = parse(start_date)
        if end_date is not None:
           filter['work_date__lte'] = parse(end_date)

        queryset = queryset.filter(**filter)
        return queryset

class UpdateAttendanceLogViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = UpdateAttendanceLogSerializer
    pagination_class = CustomAttendanceLogPagination

class ListAttendanceLogViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Employee.objects.all()
        serializer = ListAttendanceLogSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomAttendanceLogPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListAttendanceLogSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomAttendanceLogPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


#payroll page
class CreateMonthlyEmpSalaryViewSet(viewsets.ModelViewSet):
    queryset = MonthlyEmpSalary.objects.all()
    serializer_class = CreateMonthlyEmpSalarySerializer
    pagination_class = CustomPayrollPagination

class ListMonthlyEmpSalaryViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Employee.objects.all()
        serializer = ListMonthlyEmpSalarySerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomPayrollPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListMonthlyEmpSalarySerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomPayrollPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class MonthlyEmpSalaryColumnViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    serializer_class = DynamicFieldsMonthlyEmpSalaryModelSerializer
    pagination_class = CustomPayrollPagination

    def get_queryset(self, *args, **kwargs):
        qs = MonthlyEmpSalary.objects.all()
        query = self.request.GET.get("fields")
        if query:
            return qs
        else:
            return qs


class PayrollSearchViewSet(viewsets.ModelViewSet):
    search_fields = [         'emp_id__emp_id',
                              'emp_id__name',
                              "emp_id__department",
                               "month",
                               "lop",
                                "no_of_days",
                                "ctc",
                                "basic",
                                "hra",
                                "conveyance_allowances",
                                "medical_allowance",
                                "cca_allowance",
                                "pf_employer",
                                "pf_employee",
                                "pt",
                                "esi_employer",
                                "esi_employee",
                                "net_employee_payable",
                                "due_date",
                                "special_allowances",
                                "over_time",
                                "deductions",
                                "reimbursements",]

    ordering_fields = [        'emp_id__emp_id',
                                'emp_id__name',
                                "emp_id__department",
                               "month",
                               "lop",
                                "no_of_days",
                                "ctc",
                                "basic",
                                "hra",
                                "conveyance_allowances",
                                "medical_allowance",
                                "cca_allowance",
                                "pf_employer",
                                "pf_employee",
                                "pt",
                                "esi_employer",
                                "esi_employee",
                                "net_employee_payable",
                                "due_date",
                                "special_allowances",
                                "over_time",
                                "deductions",
                                "reimbursements",]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = MonthlyEmpSalary.objects.all()
    serializer_class = PayrollSearchSerializer
    pagination_class = CustomPayrollPagination

class PayrollRunViewSet(viewsets.ModelViewSet):
    search_fields = [
        '=month',
        # 'emp_id__name',
    ]
    filter_backends = (filters.SearchFilter,)
    queryset = MonthlyEmpSalary.objects.all()
    serializer_class = PayrollRunSerializer
    pagination_class = CustomPayrollPagination
#salary
class CreateEmpSalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = CreateEmpSalarySerializer



