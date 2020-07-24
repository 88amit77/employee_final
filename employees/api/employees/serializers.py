from rest_framework import serializers
from .models import (Employee, Documents, Education, WorkHistory, FamilyMembers, LeaveRules, EmpLeaveApplied, EmpLeaveId, Attendance,AttendenceLeaveid, Attendence_rules,MonthlyEmpSalary, Salary)
from rest_framework.validators import UniqueValidator
from datetime import datetime
from django.core.validators import FileExtensionValidator

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'


class FamilyMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMembers
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class EmployeeOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id',
                             'name',
                             'permanent_address_line1',
                             "designation",
                             "gender",
                             "official_email",
                             "date_of_joining",
                             'department',
                             "official_number",
                             'dob',
                             "work_location_add",)

class EmployeeSerializer(serializers.Serializer):

    emp_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    user_id = serializers.CharField(max_length=30)
    dob = serializers.DateField()
    gender = serializers.CharField(max_length=10)
    blood_group = serializers.CharField(max_length=10)
    marital_status = serializers.BooleanField(default=False)
    marriage_anniversary = serializers.DateField()
    official_email = serializers.EmailField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    personal_email = serializers.EmailField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    official_number = serializers.CharField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    personal_number = serializers.CharField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    facebook = serializers.CharField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    instagram = serializers.CharField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    linkedin = serializers.CharField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
    twitter = serializers.CharField(validators=[UniqueValidator(queryset=Employee.objects.all(),message='False')])
   # leave_approval_user_id = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    probation_period = serializers.IntegerField()
    current_address_line1 = serializers.CharField(max_length=50)
    current_address_line2 = serializers.CharField(max_length=50)
    current_country = serializers.CharField(max_length=15)
    current_state = serializers.CharField(max_length=10)
    current_pincode = serializers.CharField(max_length=15)
    current_house_type = serializers.CharField(max_length=50)
    current_staying_since = serializers.DateField()
    current_city = serializers.CharField(max_length=20)
    permanent_address_line1 = serializers.CharField(max_length=50)
    permanentt_address_line2 = serializers.CharField(max_length=50)
    permanent_country = serializers.CharField(max_length=15)
    permanent_state = serializers.CharField(max_length=15)
    permanent_pincode = serializers.CharField(max_length=15)
    employee_type = serializers.CharField(max_length=15)
    employee_status = serializers.BooleanField(default=False)
    job_title = serializers.CharField(max_length=30)
    termination_date = serializers.DateField()
    work_location_add = serializers.CharField(max_length=20)
    designation = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=50)
    resignation_date = serializers.DateField()
    resignation_notes = serializers.CharField(max_length=50)
    notice_date = serializers.DateField()
    notice_period = serializers.IntegerField()
    bank_acc_number = serializers.CharField(max_length=30)
    ifsc_code = serializers.CharField(max_length=15)
    bank_name = serializers.CharField(max_length=30)

    pan_number = serializers.CharField(max_length=20)
    pan_card = serializers.FileField(upload_to='Employees/Documents/', blank=True, null=True, max_length=100, validators=[
        FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm', 'pdf'])])
    address_proof = serializers.FileField(upload_to='Employees/Documents/', blank=True, null=True, max_length=100,
                                     validators=[FileExtensionValidator(
                                         allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm',
                                                             'pdf'])])
    permanent_proof = serializers.FileField(upload_to='Employees/Documents/', blank=True, null=True, max_length=100,
                                       validators=[FileExtensionValidator(
                                           allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm',
                                                               'pdf'])])
    aadharcard_number = serializers.CharField(max_length=20)
    aadharcard = serializers.FileField(upload_to='Employees/Documents/', blank=True, null=True, max_length=100, validators=[
        FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm', 'pdf'])])

    work_historys_emp = WorkHistorySerializer(many=True)
    family_members_emp = FamilyMembersSerializer(many=True)
    educations_emp = EducationSerializer(many=True)

    def create(self, validated_data):

        educations_data = validated_data.pop('educations_emp')
        work_historys_data = validated_data.pop('work_historys_emp')
        family_members_data = validated_data.pop('family_members_emp')
        employee = Employee.objects.create(**validated_data)
        for education_data in educations_data:
            Education.objects.create(educations=employee, **education_data)
        for work_history_data in work_historys_data:
            WorkHistory.objects.create(work_historys=employee, **work_history_data)
        for family_member_data in family_members_data:
            FamilyMembers.objects.create(family_members=employee, **family_member_data)
        return employee

    def update(self, instance, validated_data):
        educations_data = validated_data.pop('educations_emp')
        educations = (instance.educations).all()
        educations = list(educations)
        work_historys_data = validated_data.pop('work_historys_emp')
        work_historys = (instance.work_historys).all()
        work_historys = list(work_historys)
        family_members_data = validated_data.pop('family_members_emp')
        family_members = (instance.family_members).all()
        family_members = list(family_members)
        instance.name = validated_data.get('name', instance.name)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.marriage_anniversary = validated_data.get('marriage_anniversary', instance.marriage_anniversary)
        instance.official_email = validated_data.get('official_email', instance.official_email)
        instance.personal_email = validated_data.get('personal_email', instance.personal_email)
        instance.official_number = validated_data.get('official_number', instance.official_number)
        instance.personal_number = validated_data.get('personal_number', instance.personal_number)
        #instance.leave_approval_user_id = validated_data.get('leave_approval_user_id', instance.leave_approval_user_id)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.date_of_joining = validated_data.get('date_of_joining', instance.date_of_joining)
        instance.probation_period = validated_data.get('probation_period', instance.probation_period)
        instance.current_address_line1 = validated_data.get('current_address_line1', instance.Current_address_line1)
        instance.current_address_line2 = validated_data.get('current_address_line2', instance.Current_address_line2)
        instance.current_country = validated_data.get('current_country', instance.current_country)
        instance.current_state = validated_data.get('current_state', instance.current_state)
        instance.current_pincode = validated_data.get('current_pincode', instance.current_pincode)
        instance.current_house_type = validated_data.get('current_house_type', instance.current_house_type)
        instance.current_staying_since = validated_data.get('current_staying_since', instance.Current_staying_since)
        instance.current_city = validated_data.get('current_city', instance.Current_city)
        instance.permanent_address_line1 = validated_data.get('permanent_address_line1',
                                                              instance.Permanent_address_line1)
        instance.permanent_address_line2 = validated_data.get('permanent_address_line2',
                                                              instance.Permanent_address_line2)
        instance.permanent_country = validated_data.get('permanent_country', instance.Permanent_country)
        instance.permanent_state = validated_data.get('permanent_state', instance.Permanent_state)
        instance.permanent_pincode = validated_data.get('permanent_pincode', instance.Permanent_pincode)
        instance.employee_type = validated_data.get('employee_type', instance.Employee_type)
        instance.employee_Status = validated_data.get('employee_status', instance.Employee_Status)
        instance.job_title = validated_data.get('job_title', instance.Job_title)
        instance.termination_date = validated_data.get('termination_date', instance.termination_date)
        instance.work_location_add = validated_data.get('work_location_add', instance.work_location_add)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.department = validated_data.get('department', instance.department)
        instance.resignation_date = validated_data.get('resignation_date', instance.resignation_date)
        instance.resignation_notes = validated_data.get('resignation_notes', instance.resignation_notes)
        instance.notice_date = validated_data.get('notice_date', instance.notice_date)
        instance.notice_period = validated_data.get('notice_period', instance.notice_period)
        instance.bank_acc_number = validated_data.get('bank_acc_number', instance.bank_acc_number)
        instance.ifsc_code = validated_data.get('ifsc_code', instance.ifsc_code)
        instance.bank_name = validated_data.get('bank_name', instance.bank_name)

        instance.pan_number = validated_data.get('pan_number', instance.pan_number)
        instance.pan_card = validated_data.get('pan_card', instance.pan_card)
        instance.address_proof = validated_data.get('address_proof', instance.address_proof)
        instance.permanent_proof = validated_data.get('permanent_proof', instance.permanent_proof)
        instance.aadharcard_number = validated_data.get('aadharcard_number', instance.aadharcard_number)
        instance.aadharcard = validated_data.get('aadharcard', instance.aadharcard)
        instance.save()


        for work_history_data in work_historys_data:
            work_history = work_historys.pop(0)
            work_history.company_name = work_history_data.get('company_name', work_history.company_name)
            work_history.period_from = work_history_data.get('period_from', work_history.period_from)
            work_history.period_to = work_history_data.get('period_to', work_history.period_to)
            work_history.designation = work_history_data.get('designation', work_history.designation)
            work_history.reason_for_leaving = work_history_data.get('reason_for_leaving', work_history.reason_for_leaving)
            work_history.verified = work_history_data.get('verified', work_history.verified)
            work_history.save()

        for family_member_data in family_members_data:
            family_member = family_members.pop(0)
            family_member.family_Member_name = family_member_data.get('family_member_name', family_member.family_Member_name)
            family_member.relation = family_member_data.get('relation', family_member.relation)
            family_member.contact_number = family_member_data.get('contact_number', family_member.contact_number)
            family_member.save()

        for education_data in educations_data:
            education = educations.pop(0)
            education.institute_name = education_data.get('institute_name', education.institute_name)
            education.course_type = education_data.get('course_type', education.course_type)
            education.Stream = education_data.get('stream', education.Stream)
            education.start_date = education_data.get('start_date', education.start_date)
            education.end_date = education_data.get('end_date', education.end_date)
            education.average_marks = education_data.get('average_marks', education.average_marks)
            education.verified = education_data.get('verified', education.verified)
            education.save()
        return instance

class ListEmployeeSerializer(serializers.Serializer):

    emp_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    dob = serializers.DateField()
    gender = serializers.CharField(max_length=10)
    blood_group = serializers.CharField(max_length=10)
    marital_status = serializers.BooleanField(default=False)
    marriage_anniversary = serializers.DateField()
    official_email = serializers.EmailField()
    personal_email = serializers.EmailField()
    official_number = serializers.CharField(max_length=10)
    personal_number = serializers.CharField(max_length=10)
    facebook = serializers.CharField(max_length=50)
    instagram = serializers.CharField(max_length=50)
    linkedin = serializers.CharField(max_length=50)
    twitter = serializers.CharField(max_length=50)
    #leave_approval_user_id = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    probation_period = serializers.IntegerField()
    current_address_line1 = serializers.CharField(max_length=50)
    current_address_line2 = serializers.CharField(max_length=50)
    current_country = serializers.CharField(max_length=15)
    current_state = serializers.CharField(max_length=10)
    current_pincode = serializers.CharField(max_length=15)
    current_house_type = serializers.CharField(max_length=15)
    current_staying_since = serializers.DateField()
    current_city = serializers.CharField(max_length=20)
    permanent_address_line1 = serializers.CharField(max_length=50)
    permanentt_address_line2 = serializers.CharField(max_length=50)
    permanent_country = serializers.CharField(max_length=15)
    permanent_state = serializers.CharField(max_length=15)
    permanent_pincode = serializers.CharField(max_length=15)
    employee_type = serializers.CharField(max_length=15)
    employee_status = serializers.BooleanField(default=False)
    job_title = serializers.CharField(max_length=30)
    termination_date = serializers.DateField()
    work_location_add = serializers.CharField(max_length=20)
    designation = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=20)
    resignation_date = serializers.DateField()
    resignation_notes = serializers.CharField(max_length=50)
    notice_date = serializers.DateField()
    notice_period = serializers.IntegerField()
    bank_acc_number = serializers.CharField(max_length=30)
    ifsc_code = serializers.CharField(max_length=15)
    bank_name = serializers.CharField(max_length=30)

    pan_number = serializers.CharField(max_length=20)
    pan_card = serializers.FileField()
    address_proof = serializers.FileField()
    permanent_proof = serializers.FileField()
    aadharcard_number = serializers.CharField(max_length=20)
    aadharcard = serializers.FileField()



class EmployeeColumnModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(EmployeeColumnModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Employee
        fields = '__all__'


class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Employee
        fields = '__all__'


class LeaveRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRules
        fields = ('leave_id', 'leave_name', 'interval_months', 'add_value', 'yearly_carry_forward', 'document_required')

class Employee1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'department', 'designation', 'date_of_joining','employee_type', 'work_location_add')

class ListAssignedRuleSerializer(serializers.ModelSerializer):
    emp_id = Employee1Serializer(required=True)

    class Meta:
        model = EmpLeaveId
        fields = ('emp_id','leave_id','emp_leave_id')


class ListEmployee1Serializer(serializers.Serializer):
    empleaves = Employee1Serializer(many=True)

    class Meta:
        model = Employee
        fields = ('empleaves', 'emp_id', 'name', 'designation', 'department', 'date_of_joining', 'employee_type',
                  'work_location_add')


class EmpLeaveAppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveApplied
        fields = ('emp_leave_app_id', 'emp_id', 'leave_id', 'start_date', 'end_date', 'reason')
        #fields = '__all__'

class EmpLeaveAppliedNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveApplied
        fields = '__all__'

#####assigned rules
class leavepolicyAssignedLeaveidSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='emp_id.name', read_only=True)
    designation = serializers.CharField(source='emp_id.designation', read_only=True)
    date_of_joining = serializers.CharField(source='emp_id.date_of_joining', read_only=True)
    work_location_add = serializers.CharField(source='emp_id.work_location_add', read_only=True)
    employee_type = serializers.CharField(source='emp_id.employee_type', read_only=True)

    class Meta:
        model = EmpLeaveId
        fields = ("emp_leave_id", "emp_id", 'name','designation','date_of_joining', 'work_location_add','employee_type','leave_id')

##assigned attendance rule leavePolicy assign page
class ForEmployeeIdSearchForleavePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id','name', 'designation', 'date_of_joining','employee_type','work_location_add')

#for logs page

class DynamicFieldsLeaveLogModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(DynamicFieldsLeaveLogModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)
    days = serializers.SerializerMethodField(method_name='get_days')

    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)
    days = serializers.SerializerMethodField(method_name='get_days')

    class Meta:
        model = EmpLeaveApplied
        fields = (
            'emp_id', 'name', 'department', 'leave_id', 'start_date', 'end_date', 'days', 'reason', 'status')

    def get_days(self, obj):
        date_format = "%Y-%m-%d"
        b = datetime.strptime(str(obj.end_date), date_format)
        a = datetime.strptime(str(obj.start_date), date_format)
        c = b - a
        return c.days

class EmpLogSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField(method_name='get_days')

    class Meta:
        model = EmpLeaveApplied
        fields = ('emp_leave_app_id', 'leave_id', 'start_date', 'end_date', 'status', 'action_by', 'reason', 'days')

    def get_days(self, obj):
        date_format = "%Y-%m-%d"
        b = datetime.strptime(str(obj.end_date), date_format)
        a = datetime.strptime(str(obj.start_date), date_format)
        c = b - a
        return c.days

#for logs page search


class Employee2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'department')

#for logs listing
class EmployeenewSerializer(serializers.ModelSerializer):

    employee = EmpLogSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('employee', 'emp_id', 'name')

class EmpLog1Serializer(serializers.ModelSerializer):

    class Meta:
        model = EmpLeaveApplied
        fields = ('emp_leave_app_id', 'leave_id',  'status')

#for graph represention
class EmpLeaveDataSerializer(serializers.ModelSerializer):

    status1 = EmpLog1Serializer(many=True)

    class Meta:
        model = EmpLeaveId
        fields = ('status1', 'emp_id', 'leave_id')
#test
class EmpLog2Serializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField(method_name='get_days')


    class Meta:
        model = EmpLeaveApplied
        fields = ('emp_leave_app_id', 'leave_id', 'start_date', 'end_date', 'status', 'action_by', 'days','emp_id','reason')

    def get_days(self, obj):
        date_format = "%Y-%m-%d"
        b = datetime.strptime(str(obj.end_date), date_format)
        a = datetime.strptime(str(obj.start_date), date_format)
        # return obj.b - obj.b
        c = b - a
        return c.days

class ListleaveLogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)
    days = serializers.SerializerMethodField(method_name='get_days')


    class Meta:
        model = EmpLeaveApplied
        fields = ("emp_leave_app_id",
        'emp_id','name', 'department','leave_id', 'start_date', 'end_date', 'days', 'reason','status', 'action_by')

    def get_days(self, obj):
        date_format = "%Y-%m-%d"
        b = datetime.strptime(str(obj.end_date), date_format)
        a = datetime.strptime(str(obj.start_date), date_format)
        c = b - a
        return c.days
class Emp1Serializer(serializers.Serializer):
    emp_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    department = serializers.CharField(max_length=50)
class AttendaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'

##assigned attendance rule
class ForEmployeeIdSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id','name', 'department','employee_type')

class AttendaceLeaveidSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)
    employee_type = serializers.CharField(source='emp_id.employee_type', read_only=True)

    class Meta:
        model = AttendenceLeaveid
        fields = ("attendance_leave_id", "emp_id", 'name', 'department','employee_type','ar_id')

class AttendaceRulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendence_rules
        fields = '__all__'
class EmployeeListAttendance(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'department', 'employee_type')

class ListAssignedAttendanceRuleSerializer(serializers.ModelSerializer):
    emp_id = EmployeeListAttendance(required=True)

    class Meta:
        model = AttendenceLeaveid
        fields = ('attendance_leave_id', 'ar_id','emp_id')

##attendance column filter
class DynamicFieldsAttendenceModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(DynamicFieldsAttendenceModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)
    work_location_add = serializers.CharField(source='emp_id.work_location_add', read_only=True)

    class Meta:
        model = Attendance
        fields = ('emp_id', 'name', 'department', 'work_location_add', 'attendance_id', 'login', 'logout', 'annomaly',
                  'work_date')


#for attendance search
class SearchAttendanceLogSerializer(serializers.Serializer):

    emp_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    department = serializers.CharField(max_length=30)
    work_location_add = serializers.CharField(max_length=30)
    attendances = AttendaceSerializer(many=True)

#for SearchBydate attendance search


class SearchByDateAttendaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)
    work_location_add = serializers.CharField(source='emp_id.work_location_add', read_only=True)

    class Meta:
        model = Attendance
        fields = ('emp_id','name','department','work_location_add','attendance_id','login','logout','annomaly','work_date')

###for last attendance page emp wise data
class LastAttendaceLogSerializer(serializers.ModelSerializer):
    work_duration = serializers.SerializerMethodField(method_name='get_time')
    class Meta:
        model = Attendance
        fields = ('emp_id','login','logout','work_date', 'work_duration')

    def get_time(self, obj):

        b = datetime.strptime(str(obj.logout), '%H:%M:%S')
        a = datetime.strptime(str(obj.login), '%H:%M:%S')
        if a >= b:
            return 0
        else:
            c = b - a
            # d = (c / (60 ** 2))
            d = c.total_seconds() / 3600
            e = str(d)
            return e[0:5]
            # return e


class SearchBydateAttendanceLogSerializer(serializers.ModelSerializer):
    attendances = SearchByDateAttendaceSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'department', 'work_location_add',  'attendances')

class EnterAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("attendance_id", 'emp_id', 'login', "logout", 'login_image', 'logout_image', 'work_date')


class ListAttendanceLogSerializer(serializers.ModelSerializer):

    attendances = AttendaceSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('attendances', 'emp_id', 'name', 'department', 'work_location_add')


class UpdateAttendanceLogSerializer(serializers.Serializer):

    emp_id = serializers.IntegerField(read_only=True)
    attendances = AttendaceSerializer(many=True)


    def update(self, instance, validated_data):
        attendances_data = validated_data.pop('attendances')
        emp_id = (instance.emp_id).all()
        emp_id = list(emp_id)
        instance.save()
        for attendancess_data in attendances_data:
            emp = emp_id.pop(0)
            emp.login = attendancess_data.get('login', emp.login)
            emp.logout = attendancess_data.get('logout', emp.logout)
            emp.save()
        return instance



#payroll
class DynamicFieldsMonthlyEmpSalaryModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(DynamicFieldsMonthlyEmpSalaryModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)

    class Meta:
        model = MonthlyEmpSalary
        fields = ('emp_id', 'name', 'department',
                  'month', 'lop', 'no_of_days', 'ctc', 'basic', 'hra', 'conveyance_allowances', 'medical_allowance',
                  'cca_allowance', 'pf_employer', 'pf_employee', 'pt', 'esi_employer', 'esi_employee',
                  'net_employee_payable',
                  'due_date', 'special_allowances', 'over_time', 'deductions', 'reimbursements'
                  )

class CreateMonthlyEmpSalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthlyEmpSalary
        fields = '__all__'

class ListMonthlyEmpSalarySerializer(serializers.ModelSerializer):
    monthlyempsalary = CreateMonthlyEmpSalarySerializer(many=True)

    class Meta:
        model = Employee
        fields = ('monthlyempsalary', 'emp_id', 'name','department')


class PayrollSearchSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)

    class Meta:
        model = MonthlyEmpSalary
        fields = ('emp_id','name','department',
                  'month','lop','no_of_days','ctc','basic','hra','conveyance_allowances','medical_allowance',
                  'cca_allowance','pf_employer','pf_employee','pt','esi_employer','esi_employee','net_employee_payable',
                  'due_date','special_allowances','over_time','deductions','reimbursements'
                  )

class PayrollRunSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='emp_id.name', read_only=True)
    department = serializers.CharField(source='emp_id.department', read_only=True)

    class Meta:
        model = MonthlyEmpSalary
        fields = ('emp_id','name','department',
                  'month','lop','no_of_days','ctc','basic','hra','conveyance_allowances','medical_allowance',
                  'cca_allowance','pf_employer','pf_employee','pt','esi_employer','esi_employee','net_employee_payable',
                  'due_date','special_allowances','over_time','deductions','reimbursements'
                  )

#salary
class CreateEmpSalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = '__all__'

class ListEmpSalarySerializer(serializers.ModelSerializer):
    empsalary = CreateEmpSalarySerializer(many=True)

    class Meta:
        model = Employee
        fields = ('empsalary', 'emp_id', 'name')

