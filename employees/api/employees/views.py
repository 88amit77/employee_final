from rest_framework import viewsets
import csv
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import status
import requests
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import (Employee, Education, Documents, FamilyMembers, WorkHistory, LeaveRules, EmpLeaveApplied, EmpLeaveId,
                     Attendance, AttendenceLeaveid, Attendence_rules, MonthlyEmpSalary)
from .serializers import (
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
EmployeePayrollSerializer,
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
                             'Permanent_address_line1': "Address",
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
                              "official_email": 'Official Email',
                              'leave': 'Leave'
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
                              "action_by": 'Actions',
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
                              "login": 'In Time',
                              "logout": 'Out Time',


                           },
                'sortable': [
                              'emp_id',
                           ],

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
                              'name': 'Employee Name',
                              "month": 'Department',
                              "lop": 'Lop',
                              "No_of_days": 'No Of Days',
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

                           },
                'sortable': [
                              'emp_id',
                           ],
                'date_filters': [
                    'due_date'
                ]

            },
            'results': data
        })
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
                           | Q(Permanent_address_line1__contains=query) | Q(designation__contains=query)
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
        query = self.request.GET.get("Permanent_address_line1")
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


def ExportEmp(request):
    response = HttpResponse(content_type='text/csv')
    write = csv.writer(response)
    write.writerow(['Employee Id', 'Employee Name', 'Date of Birth', 'Gender', 'Official Email', 'Phone', 'Date of Joining',
                    'Address', 'Work Location', 'Designation', 'Department'])
    for employee in Employee.objects.all().values('emp_id', 'name', 'dob', 'gender', 'official_email', 'official_number', 'date_of_joining', 'Permanent_address_line1', 'work_location_add', 'designation', 'department'):
       write.writerow(employee)

    response['Content-Disposition'] ='attachment; filename="employee.csv"'
    return response


def ExportEmpLeaveLog(request):
    response = HttpResponse(content_type='text/csv')
    write = csv.writer(response)
    write.writerow(['emp_leave_app_id','emp_id', 'leave_id', 'start_date', 'end_date', 'status', 'reason', 'action_by'])
    for employee in EmpLeaveApplied.objects.all().values('emp_leave_app_id', 'emp_id', 'leave_id', 'start_date', 'end_date', 'status', 'reason', 'action_by'):
        write.writerow(employee)

    response['Content-Disposition'] = 'attachment; filename="employeeLeaveLog.csv"'
    return response


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

#attendance
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendaceSerializer

class AttendanceLeaveidViewSet(viewsets.ModelViewSet):
    queryset = AttendenceLeaveid.objects.all()
    serializer_class = AttendaceLeaveidSerializer

class AttendenceRulesViewSet(viewsets.ModelViewSet):
    queryset = Attendence_rules.objects.all()
    serializer_class = AttendaceRulesSerializer

class EnterAttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = EnterAttendanceSerializer

class UpdateAttendanceLogViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = UpdateAttendanceLogSerializer

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

class MonthlyEmpSalarySearchViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeePayrollSerializer
    pagination_class = CustomPayrollPagination

    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.all()
        query = self.request.GET.get("keyword")
        if query:
            qs = qs.filter(Q(name__contains=query) | Q(emp_id__contains=query))
        query = self.request.GET.get("emp_id")
        if query:
            emp_id = query.split(',')
            qs = qs.filter(emp_id__in=emp_id)

        query = self.request.GET.get("name")
        if query:
            name = query.split(',')
            qs = qs.filter(name__in=name)
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