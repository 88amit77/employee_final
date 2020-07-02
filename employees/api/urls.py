from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.process.api_v1.rest.views import *

from .employees import views

router = DefaultRouter()

schema_view = get_schema_view(openapi.Info(
      title="Employees API",
      default_version='v1',
      description="Test description",
   ), public=True, permission_classes=(permissions.AllowAny,))



#  DRF-YASG Swagger
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = DefaultRouter()

router.register('employee/list_employee', views.ListEmployeeViewSet, basename="list_employee")
router.register('employee/personal', views.EmployeeViewSet, basename="personal")
router.register('employee/personal_personal', views.PersonalViewSet, basename="personal_personal")
router.register('employee/work', views.WorkHistoryViewSet, basename="work")
router.register('employee/education', views.EducationViewSet, basename="education")
router.register('employee/family', views.FamilyMembersViewSet, basename="family")
router.register('employee/doc', views.DocumentsViewSet, basename="doc")
router.register('employee/employee_search', views.EmployeeSearchViewSet, basename="employee_search")
router.register('employee/employee_column', views.EmployeeColumnViewSet, basename="employee_column")
# router.register('leave_rule', views.LeaveRulesViewSet, basename="leave_rule")
router.register('employee/leave', views.LeaveRulesView, basename="leave")
router.register('employee/assign_employee_leave', views.EmployeeView, basename="'assign_employee_leave")
router.register('employee/list_assigned', views.ListAssignRulesViewSet, basename="list_assigned")
router.register('employee/assigned_search', views.AssignRulesSearchViewSet, basename="assigned_search")
router.register('employee/assigned_column', views.AssignRulesColumnViewSet, basename="assigned_column")
router.register('employee/emp_leave_applied', views.EmpLeaveAppliedView, basename="emp_leave_applied")
router.register('employee/emp_log_approve', views.EmpLogView, basename="emp_log_approve")
router.register('employee/employee_log', views.EmployeeLogView, basename="employee_log")
router.register('employee/list_leave_logs', views.ListLeaveLogsViewSet, basename="list_leave_logs")
router.register('employee/leave_logs_search', views.LeaveLogsSearchViewSet, basename="leave_logs_search")
router.register('employee/list_assigned_rules', views.ListAssignedRuleView, basename="list_assigned_rules")

router.register('employee/employee_log1', views.EmployeeLoggView, basename="employee_log")
router.register('employee/emp_name', views.EmpNameView, basename="emp_name")


router.register('employee/attendance', views.AttendanceViewSet, basename="attendance")
router.register('employee/list_attendance_log', views.ListAttendanceLogViewSet, basename="list_attendance_log")
router.register('employee/update_attendance_log', views.UpdateAttendanceLogViewSet, basename="update_attendance_log")
router.register('employee/create_attendance_rules', views.AttendenceRulesViewSet, basename="create_attendance_rules")
router.register('employee/assign_attendance_rules', views.AttendanceLeaveidViewSet, basename="assign_attendance_rules")
router.register('employee/enter_attendance', views.EnterAttendanceViewSet, basename="enter_attendance")
router.register('list_assigned_attendance_rule', views.ListAssignedAttendanceRuleView, basename="emptest")

router.register('employee/create_payroll', views.CreateMonthlyEmpSalaryViewSet, basename="create_payroll")
router.register('employee/list_payroll', views.ListMonthlyEmpSalaryViewSet, basename="list_payroll")
router.register('employee/payroll_column', views.MonthlyEmpSalaryColumnViewSet, basename="payroll_column")

router.register('employee/testing_names', views.TestingNamesViewSet, basename="testing_names")
router.register('employee/testing_status', views.TestingStatusViewSet, basename="testing_status")



# DRF-YASG Swagger/Redoc
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Employee and Process APIs",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    path('', include(router.urls)),
    path("employee/employees_docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  	path('employee/employee_csv/', views.ExportEmp, name='employee_csv'),
	path('employee/employee_leave_log_csv/', views.ExportEmpLeaveLog, name='employee_leave_log_csv'),
    path('employee/attendance_search/', views.SearchAttendanceLogAPIView.as_view()),
    url('employee/payrollrun', views.PayrollrunList.as_view()),
    path('employee/payroll_search/', views.PayrollSearchAPIView.as_view()),
	path('employee/process/', include('api.process.urls')),
	url('employee/payrollrun', views.PayrollrunList.as_view()),
    path('employee/payroll_search/', views.PayrollSearchAPIView.as_view()),

]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += [
#    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

# ]