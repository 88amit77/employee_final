from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
from .employees import views
from api.process.api_v1.rest.views import *

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

router.register('list_employee', views.ListEmployeeViewSet, basename="list_employee")
router.register('personal', views.EmployeeViewSet, basename="personal")
router.register('work', views.WorkHistoryViewSet, basename="work")
router.register('education', views.EducationViewSet, basename="education")
router.register('family', views.FamilyMembersViewSet, basename="family")
router.register('doc', views.DocumentsViewSet, basename="doc")
router.register('employee_search', views.EmployeeSearchViewSet, basename="employee_search")
router.register('employee_column', views.EmployeeColumnViewSet, basename="employee_column")
# router.register('leave_rule', views.LeaveRulesViewSet, basename="leave_rule")
router.register('leave', views.LeaveRulesView, basename="leave")
router.register('assign_employee_leave', views.EmployeeView, basename="'assign_employee_leave")
router.register('list_assigned', views.ListAssignRulesViewSet, basename="list_assigned")
router.register('assigned_search', views.AssignRulesSearchViewSet, basename="assigned_search")
router.register('assigned_column', views.AssignRulesColumnViewSet, basename="assigned_column")
router.register('emp_leave_applied', views.EmpLeaveAppliedView, basename="emp_leave_applied")
router.register('emp_log_approve', views.EmpLogView, basename="emp_log_approve")
router.register('employee_log', views.EmployeeLogView, basename="employee_log")
router.register('list_leave_logs', views.ListLeaveLogsViewSet, basename="list_leave_logs")
router.register('leave_logs_search', views.LeaveLogsSearchViewSet, basename="leave_logs_search")
router.register('list_assigned_rules', views.ListAssignedRuleView, basename="list_assigned_rules")

router.register('attendance', views.AttendanceViewSet, basename="attendance")
router.register('list_attendance_log', views.ListAttendanceLogViewSet, basename="list_attendance_log")
router.register('update_attendance_log', views.UpdateAttendanceLogViewSet, basename="update_attendance_log")
router.register('create_attendance_rules', views.AttendenceRulesViewSet, basename="create_attendance_rules")
router.register('assign_attendance_rules', views.AttendanceLeaveidViewSet, basename="assign_attendance_rules")
router.register('enter_attendance', views.EnterAttendanceViewSet, basename="enter_attendance")

router.register('attendance', views.AttendanceViewSet, basename="attendance")
router.register('list_attendance_log', views.ListAttendanceLogViewSet, basename="list_attendance_log")
router.register('update_attendance_log', views.UpdateAttendanceLogViewSet, basename="update_attendance_log")
router.register('create_attendance_rules', views.AttendenceRulesViewSet, basename="create_attendance_rules")
router.register('assign_attendance_rules', views.AttendanceLeaveidViewSet, basename="assign_attendance_rules")
router.register('enter_attendance', views.EnterAttendanceViewSet, basename="enter_attendance")
router.register('list_assigned_attendance_rule', views.ListAssignedAttendanceRuleView, basename="emptest")

router.register('create_payroll', views.CreateMonthlyEmpSalaryViewSet, basename="create_payroll")
router.register('list_payroll', views.ListMonthlyEmpSalaryViewSet, basename="list_payroll")
router.register('payroll_column', views.MonthlyEmpSalaryColumnViewSet, basename="payroll_column")

schema_view = get_swagger_view(title='Micromerce API')




schema_view = get_schema_view(
   openapi.Info(
      title="Employee and Process APIs",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    path("employees/docs/", schema_view),
    path('employee_csv/', views.ExportEmp, name='employee_csv'),
    path('employee_leave_log_csv/', views.ExportEmpLeaveLog, name='employee_leave_log_csv'),
    path('attendance_search/', views.SearchAttendanceLogAPIView.as_view()),
    url('payrollrun', views.PayrollrunList.as_view()),
    path('payroll_search/', views.PayrollSearchAPIView.as_view()),
	path('process/', include('api.process.urls'))

]

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


