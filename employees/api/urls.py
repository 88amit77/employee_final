from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
from .employees import views

from django.urls import path, include

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

router.register('attendance', views.AttendanceViewSet, basename="attendance")
router.register('list_attendance_log', views.ListAttendanceLogViewSet, basename="list_attendance_log")
router.register('update_attendance_log', views.UpdateAttendanceLogViewSet, basename="update_attendance_log")
router.register('create_attendance_rules', views.AttendenceRulesViewSet, basename="create_attendance_rules")
router.register('assign_attendance_rules', views.AttendanceLeaveidViewSet, basename="assign_attendance_rules")
router.register('enter_attendance', views.EnterAttendanceViewSet, basename="enter_attendance")

router.register('create_payroll', views.CreateMonthlyEmpSalaryViewSet, basename="create_payroll")
router.register('list_payroll', views.ListMonthlyEmpSalaryViewSet, basename="list_payroll")
router.register('payroll_search', views.MonthlyEmpSalarySearchViewSet, basename="payroll_search")


schema_view = get_swagger_view(title='Micromerce API')

urlpatterns = [
    path('', include(router.urls)),
    path("employees/docs/", schema_view),
    path('employee_csv/', views.ExportEmp, name='employee_csv'),
    path('employee_leave_log_csv/', views.ExportEmpLeaveLog, name='employee_leave_log_csv'),

]






