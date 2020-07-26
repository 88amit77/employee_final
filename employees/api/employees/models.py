from django.db import models
from django.core.validators import FileExtensionValidator


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    user_id = models.CharField(max_length=30, blank=True, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10)
    marital_status = models.BooleanField(default=False)
    marriage_anniversary = models.DateField(blank=True, null=True)
    official_email = models.EmailField()
    personal_email = models.EmailField()
    official_number = models.CharField(max_length=10)
    personal_number = models.CharField(max_length=10)
   # leave_approval_user_id = models.IntegerField()
    facebook = models.CharField(max_length=50,blank=True, null=True)
    instagram = models.CharField(max_length=50,blank=True, null=True)
    linkedin = models.CharField(max_length=50,blank=True, null=True)
    twitter = models.CharField(max_length=50,blank=True, null=True)
    date_of_joining = models.DateField()
    probation_period = models.IntegerField()
    current_address_line1 = models.CharField(max_length=50)
    current_address_line2 = models.CharField(max_length=50)
    current_country = models.CharField(max_length=15)
    current_state = models.CharField(max_length=10)
    current_pincode = models.CharField(max_length=15)
    current_house_type = models.CharField(max_length=50)
    current_staying_since = models.DateField()
    current_city = models.CharField(max_length=25)
    permanent_address_line1 = models.CharField(max_length=50)
    permanentt_address_line2 = models.CharField(max_length=50)
    permanent_country = models.CharField(max_length=15)
    permanent_state = models.CharField(max_length=15)
    permanent_pincode = models.CharField(max_length=15)
    employee_type = models.CharField(max_length=15)
    employee_status = models.BooleanField(default=False)
    job_title = models.CharField(max_length=30)
    termination_date = models.DateField(blank=True, null=True)
    work_location_add = models.CharField(max_length=200)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    resignation_date = models.DateField(blank=True, null=True)
    resignation_notes = models.CharField(max_length=200,blank=True, null=True)
    notice_date = models.DateField(blank=True, null=True)
    notice_period = models.IntegerField(blank=True, null=True)
    bank_acc_number = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=30)

    pan_number = models.CharField(max_length=20)
    pan_card = models.FileField(upload_to='Employees/Documents/', max_length=200, validators=[
        FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm', 'pdf'])])
    address_proof = models.FileField(upload_to='Employees/Documents/', max_length=200,
                                     validators=[FileExtensionValidator(
                                         allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm', 'pdf'])])
    permanent_proof = models.FileField(upload_to='Employees/Documents/', max_length=200,
                                       validators=[FileExtensionValidator(
                                           allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm', 'pdf'])])
    aadharcard_number = models.CharField(max_length=20)
    aadharcard = models.FileField(upload_to='Employees/Documents/', max_length=200, validators=[
        FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm', 'pdf'])])

    def __str__(self):
        return self.name


class Education(models.Model):
    educations = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='educations_emp', null=True, blank=True)
    education_id = models.AutoField(primary_key=True)
    institute_name = models.CharField(max_length=50)
    course_type = models.CharField(max_length=256)
    stream = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    average_marks = models.FloatField()
    verified = models.BooleanField(default=False)


class FamilyMembers(models.Model):
    family_members = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='family_members_emp', null=True,
                                       blank=True)
    family_member_id = models.AutoField(primary_key=True)
    family_member_name = models.CharField(max_length=20)
    relation = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=10)


class WorkHistory(models.Model):
    work_historys = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='work_historys_emp', null=True,
                                      blank=True)
    work_history_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    period_from = models.DateField()
    period_to = models.DateField()
    designation = models.CharField(max_length=100)
    reason_for_leaving = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)



class LeaveRules(models.Model):
    leave_id = models.AutoField(primary_key=True)
    leave_name = models.CharField(max_length=50)
    interval_months = models.PositiveIntegerField()
    add_value = models.FloatField()
    yearly_carry_forward = models.BooleanField(default=False)
    document_required = models.BooleanField(default=False)

    def __str__(self):
        return self.leave_name


class EmpLeaveId(models.Model):
    emp_leave_id = models.AutoField(primary_key=True)
    emp_id = models.OneToOneField(Employee,on_delete=models.CASCADE, default=None, unique=False)
    leave_id = models.ManyToManyField(LeaveRules, blank=True, null=True)


class EmpLeaveApplied(models.Model):
    ACTIVITY_TYPES = (
        ('APPROVED', 'approved'),
        ('PENDING', 'pending'),
        ('REJECT', 'reject'),
    )
    emp_leave_app_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE, default=None, unique=False)
    leave_id = models.ForeignKey(LeaveRules, on_delete=models.CASCADE, default=None, unique=False)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=ACTIVITY_TYPES, default="PENDING")
    reason = models.CharField(max_length=100, null=True, blank=True)
    action_by = models.ForeignKey(Employee, related_name='action_by', on_delete=models.CASCADE,null=True,
                               blank=True, default=None, unique=False)

    def __str__(self):
        return self.reason

#attendance
from .validators import validate_file_extension


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee, related_name='attendances', on_delete=models.CASCADE, default=None, unique=False)
    work_date = models.DateField(null=True, blank=True)
    login = models.TimeField(default="00:00:00")
    login_image = models.FileField(upload_to='Employees/Attendance/', blank=True, null=True, max_length=100,
                                   validators=[FileExtensionValidator(
                                       allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm'])])
    logout_image = models.FileField(upload_to='Employees/Attendance/', blank=True, null=True, max_length=100,
                                    validators=[FileExtensionValidator(
                                        allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm'])])
    logout = models.TimeField(default="00:00:00")
    annomaly = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=30, null=True, blank=True)
    ip_location = models.CharField(max_length=30, null=True, blank=True)


class Attendence_rules(models.Model):

     ar_id = models.AutoField(primary_key=True)
     ar_name = models.CharField(max_length=30)
     ar_description = models.CharField(max_length=50)
     in_time = models.TimeField(default="00:00:00")
     in_grace_mins = models.PositiveIntegerField()
     out_time = models.TimeField(default="00:00:00")
     out_grace_mins = models.PositiveIntegerField()
     work_duration = models.FloatField()
     random_weekly_off = models.BooleanField(default=False)
     sunday_off = models.BooleanField(default=False)
     saturday_sunday_off = models.BooleanField(default=False)

     def __str__(self):
        return self.ar_name
#for assign_attendance_rules page

class AttendenceLeaveid(models.Model):
      attendance_leave_id = models.AutoField(primary_key=True)
      #emp_id = models.ForeignKey(Employee, related_name='attenadance_leaveids', on_delete=models.CASCADE, default=None, unique=False)
      emp_id = models.OneToOneField(Employee,on_delete=models.CASCADE, default=None, unique=False)
      ar_id = models.ForeignKey(Attendence_rules,related_name='ar_attenadance_leaveids', on_delete=models.CASCADE, default=None, unique=False)


#for pay roll
class MonthlyEmpSalary(models.Model):
     emp_id = models.ForeignKey(Employee, related_name='monthlyempsalary', on_delete=models.CASCADE, default=None, unique=False)
     month = models.CharField(max_length=100)
     lop = models.PositiveIntegerField()
     no_of_days = models.PositiveIntegerField()
     ctc = models.FloatField()
     basic = models.FloatField()
     hra = models.FloatField()
     conveyance_allowances = models.FloatField()
     medical_allowance = models.FloatField()
     cca_allowance = models.FloatField(default=0.0)
     pf_employer = models.FloatField(default=0.0)
     pf_employee = models.FloatField(default=0.0)
     pt = models.FloatField(default=0.0)
     esi_employer = models.FloatField(default=0.0)
     esi_employee = models.FloatField(default=0.0)
     net_employee_payable = models.FloatField(default=0.0)
     due_date = models.DateField()
     special_allowances = models.FloatField(default=0.0)
     over_time = models.FloatField(default=0.0)
     deductions = models.FloatField(default=0.0)
     reimbursements = models.FloatField(default=0.0)




class Salary(models.Model):

    emp_id = models.ForeignKey(Employee, related_name='empsalary', on_delete=models.CASCADE, default=None, unique=False)
    ctc = models.FloatField()
    basic = models.FloatField()
    hra = models.FloatField()
    conveyance_allowances = models.FloatField()
    medical_allowance = models.FloatField()
    cca_allowance = models.FloatField()
    pf_employer = models.FloatField()
    pf_employee = models.FloatField()
    pt = models.FloatField()
    esi_employer = models.FloatField()
    esi_employee = models.FloatField()


