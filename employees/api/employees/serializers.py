from rest_framework import serializers
from .models import (Employee, Documents, Education, WorkHistory, FamilyMembers, LeaveRules, EmpLeaveApplied, EmpLeaveId)
from rest_framework.validators import UniqueValidator
from datetime import datetime


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
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


class EmployeeSerializer(serializers.Serializer):

    emp_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
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
    leave_approval_user_id = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    probation_period = serializers.IntegerField()
    Current_address_line1 = serializers.CharField(max_length=50)
    Current_address_line2 = serializers.CharField(max_length=50)
    current_country = serializers.CharField(max_length=15)
    current_state = serializers.CharField(max_length=10)
    current_pincode = serializers.CharField(max_length=15)
    current_house_type = serializers.CharField(max_length=15)
    Current_staying_since = serializers.DateField()
    Current_city = serializers.CharField(max_length=20)
    Permanent_address_line1 = serializers.CharField(max_length=50)
    Permanentt_address_line2 = serializers.CharField(max_length=50)
    Permanent_country = serializers.CharField(max_length=15)
    Permanent_state = serializers.CharField(max_length=15)
    Permanent_pincode = serializers.CharField(max_length=15)
    Employee_type = serializers.CharField(max_length=15)
    Employee_Status = serializers.BooleanField(default=False)
    Job_title = serializers.CharField(max_length=30)
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
    work_historys_emp = WorkHistorySerializer(many=True)
    family_members_emp = FamilyMembersSerializer(many=True)
    documents_emp = DocumentsSerializer(many=True)
    educations_emp = EducationSerializer(many=True)

    def create(self, validated_data):
        documents_data = validated_data.pop('documents_emp')
        educations_data = validated_data.pop('educations_emp')
        work_historys_data = validated_data.pop('work_historys_emp')
        family_members_data = validated_data.pop('family_members_emp')
        employee = Employee.objects.create(**validated_data)
        for document_data in documents_data:
            Documents.objects.create(documents=employee, **document_data)
        for education_data in educations_data:
            Education.objects.create(educations=employee, **education_data)
        for work_history_data in work_historys_data:
            WorkHistory.objects.create(work_historys=employee, **work_history_data)
        for family_member_data in family_members_data:
            FamilyMembers.objects.create(family_members=employee, **family_member_data)
        return employee

    def update(self, instance, validated_data):
        documents_data = validated_data.pop('documents_emp')
        documents = (instance.documents).all()
        documents = list(documents)
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
        instance.Current_address_line1 = validated_data.get('Current_address_line1', instance.Current_address_line1)
        instance.Current_address_line2 = validated_data.get('Current_address_line2', instance.Current_address_line2)
        instance.current_country = validated_data.get('current_country', instance.current_country)
        instance.current_state = validated_data.get('current_state', instance.current_state)
        instance.current_pincode = validated_data.get('current_pincode', instance.current_pincode)
        instance.current_house_type = validated_data.get('current_house_type', instance.current_house_type)
        instance.Current_staying_since = validated_data.get('Current_staying_since', instance.Current_staying_since)
        instance.Current_city = validated_data.get('Current_city', instance.Current_city)
        instance.Permanent_address_line1 = validated_data.get('Permanent_address_line1',
                                                              instance.Permanent_address_line1)
        instance.Permanent_address_line2 = validated_data.get('Permanent_address_line2',
                                                              instance.Permanent_address_line2)
        instance.Permanent_country = validated_data.get('Permanent_country', instance.Permanent_country)
        instance.Permanent_state = validated_data.get('Permanent_state', instance.Permanent_state)
        instance.Permanent_pincode = validated_data.get('Permanent_pincode', instance.Permanent_pincode)
        instance.Employee_type = validated_data.get('Employee_type', instance.Employee_type)
        instance.Employee_Status = validated_data.get('Employee_Status', instance.Employee_Status)
        instance.Job_title = validated_data.get('Job_title', instance.Job_title)
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
        instance.save()

        for document_data in documents_data:
            document = documents.pop(0)
            document.pan_number = document_data.get('pan_number', document.pan_number)
            document.pan_card = document_data.get('pan_card', document.pan_card)
            document.address_proof = document_data.get('address_proof', document.address_proof)
            document.permanent_proof = document_data.get('permanent_proof', document.permanent_proof)
            document.aadharcard_number = document_data.get('aadharcard_number', document.aadharcard_number)
            document.aadharcard = document_data.get('aadharcard', document.aadharcard)
            document.save()

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
            family_member.family_Member_name = family_member_data.get('family_Member_name', family_member.family_Member_name)
            family_member.relation = family_member_data.get('relation', family_member.relation)
            family_member.contact_number = family_member_data.get('contact_number', family_member.contact_number)
            family_member.save()

        for education_data in educations_data:
            education = educations.pop(0)
            education.institute_name = education_data.get('institute_name', education.institute_name)
            education.course_type = education_data.get('course_type', education.course_type)
            education.Stream = education_data.get('Stream', education.Stream)
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
    Current_address_line1 = serializers.CharField(max_length=50)
    Current_address_line2 = serializers.CharField(max_length=50)
    current_country = serializers.CharField(max_length=15)
    current_state = serializers.CharField(max_length=10)
    current_pincode = serializers.CharField(max_length=15)
    current_house_type = serializers.CharField(max_length=15)
    Current_staying_since = serializers.DateField()
    Current_city = serializers.CharField(max_length=20)
    Permanent_address_line1 = serializers.CharField(max_length=50)
    Permanentt_address_line2 = serializers.CharField(max_length=50)
    Permanent_country = serializers.CharField(max_length=15)
    Permanent_state = serializers.CharField(max_length=15)
    Permanent_pincode = serializers.CharField(max_length=15)
    Employee_type = serializers.CharField(max_length=15)
    Employee_Status = serializers.BooleanField(default=False)
    Job_title = serializers.CharField(max_length=30)
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



# class Employee1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ('emp_id', 'name', 'official_email', 'leave')


class ListEmployee1Serializer(serializers.Serializer):

    emp_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    designation = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=20)
    date_of_joining = serializers.DateField()
    Employee_type = serializers.CharField(max_length=15)
    work_location_add = serializers.CharField(max_length=20)
    leave = serializers.CharField(max_length=100)


class EmpLeaveAppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveApplied
        fields = ('emp_leave_app_id', 'emp_id', 'leave_id', 'start_date', 'end_date', 'reason')
        #fields = '__all__'

class EmpLeaveAppliedNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveApplied
        fields = '__all__'

class Employee1Serializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveId
        fields = '__all__'


#for logs page
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
