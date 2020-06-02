# Generated by Django 3.0.6 on 2020-06-02 12:03

import api.employees.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_rules',
            fields=[
                ('ar_id', models.AutoField(primary_key=True, serialize=False)),
                ('ar_name', models.CharField(max_length=30)),
                ('ar_description', models.CharField(max_length=50)),
                ('in_time', models.TimeField(default='00:00:00')),
                ('out_time', models.TimeField(default='00:00:00')),
                ('work_duration', models.FloatField()),
                ('random_weekly_off', models.BooleanField(default=False)),
                ('sunday_off', models.BooleanField(default=False)),
                ('saturday_sunday_off', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=10)),
                ('marital_status', models.BooleanField(default=False)),
                ('marriage_anniversary', models.DateField()),
                ('official_email', models.EmailField(max_length=254)),
                ('personal_email', models.EmailField(max_length=254)),
                ('official_number', models.CharField(max_length=10)),
                ('personal_number', models.CharField(max_length=10)),
                ('facebook', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField()),
                ('probation_period', models.IntegerField()),
                ('current_address_line1', models.CharField(max_length=50)),
                ('current_address_line2', models.CharField(max_length=50)),
                ('current_country', models.CharField(max_length=15)),
                ('current_state', models.CharField(max_length=10)),
                ('current_pincode', models.CharField(max_length=15)),
                ('current_house_type', models.CharField(max_length=50)),
                ('current_staying_since', models.DateField()),
                ('current_city', models.CharField(max_length=25)),
                ('permanent_address_line1', models.CharField(max_length=50)),
                ('permanentt_address_line2', models.CharField(max_length=50)),
                ('permanent_country', models.CharField(max_length=15)),
                ('permanent_state', models.CharField(max_length=15)),
                ('permanent_pincode', models.CharField(max_length=15)),
                ('employee_type', models.CharField(max_length=15)),
                ('employee_status', models.BooleanField(default=False)),
                ('job_title', models.CharField(max_length=30)),
                ('termination_date', models.DateField()),
                ('work_location_add', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('resignation_date', models.DateField()),
                ('resignation_notes', models.CharField(max_length=50)),
                ('notice_date', models.DateField()),
                ('notice_period', models.IntegerField()),
                ('bank_acc_number', models.CharField(max_length=30)),
                ('ifsc_code', models.CharField(max_length=15)),
                ('bank_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRules',
            fields=[
                ('leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_name', models.CharField(max_length=50)),
                ('interval_months', models.PositiveIntegerField()),
                ('add_value', models.FloatField()),
                ('yearly_carry_forward', models.BooleanField(default=False)),
                ('document_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('work_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=30)),
                ('period_from', models.DateField()),
                ('period_to', models.DateField()),
                ('designation', models.CharField(max_length=20)),
                ('reason_for_leaving', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('work_historys', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_historys_emp', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyEmpSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('lop', models.PositiveIntegerField()),
                ('No_of_days', models.PositiveIntegerField()),
                ('ctc', models.FloatField()),
                ('basic', models.FloatField()),
                ('hra', models.FloatField()),
                ('conveyance_allowances', models.FloatField()),
                ('medical_allowance', models.FloatField()),
                ('cca_allowance', models.FloatField()),
                ('pf_employer', models.FloatField()),
                ('pf_employee', models.FloatField()),
                ('pt', models.FloatField()),
                ('esi_employer', models.FloatField()),
                ('esi_employee', models.FloatField()),
                ('net_employee_payable', models.FloatField()),
                ('due_date', models.DateField()),
                ('emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='monthlyempsalary', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMembers',
            fields=[
                ('family_member_id', models.AutoField(primary_key=True, serialize=False)),
                ('family_Member_name', models.CharField(max_length=20)),
                ('relation', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=10)),
                ('family_members', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family_members_emp', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmpLeaveId',
            fields=[
                ('emp_leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='empleaves', to='employees.Employee')),
                ('leave_id', models.ManyToManyField(to='employees.LeaveRules')),
            ],
        ),
        migrations.CreateModel(
            name='EmpLeaveApplied',
            fields=[
                ('emp_leave_app_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('APPROVED', 'approved'), ('PENDING', 'pending'), ('REJECT', 'reject')], default='PENDING', max_length=10)),
                ('reason', models.CharField(blank=True, max_length=50, null=True)),
                ('action_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='action_by', to='employees.Employee')),
                ('emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employees.Employee')),
                ('leave_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employees.LeaveRules')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('education_id', models.AutoField(primary_key=True, serialize=False)),
                ('institute_name', models.CharField(max_length=50)),
                ('course_type', models.CharField(max_length=30)),
                ('stream', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('average_marks', models.FloatField()),
                ('verified', models.BooleanField(default=False)),
                ('educations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educations_emp', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('pan_number', models.CharField(max_length=20)),
                ('pan_card', models.FileField(blank=True, null=True, upload_to='')),
                ('address_proof', models.FileField(blank=True, null=True, upload_to='')),
                ('permanent_proof', models.FileField(blank=True, null=True, upload_to='')),
                ('aadharcard_number', models.CharField(max_length=20)),
                ('aadharcard', models.FileField(blank=True, null=True, upload_to='')),
                ('documents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_emp', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='AttendenceLeaveid',
            fields=[
                ('attendance_leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('ar_id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='employees.Attendence_rules')),
                ('emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='attenadance_leaveids', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_date', models.DateField(blank=True, null=True)),
                ('login', models.TimeField(default='00:00:00')),
                ('login_image', models.FileField(upload_to='uploads/%Y/%m/%d', validators=[api.employees.validators.validate_file_extension])),
                ('logout_image', models.FileField(upload_to='uploads/%Y/%m/%d', validators=[api.employees.validators.validate_file_extension])),
                ('logout', models.TimeField(default='00:00:00')),
                ('annomaly', models.BooleanField(default=False)),
                ('ip_address', models.CharField(blank=True, max_length=30, null=True)),
                ('ip_location', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='employees.Employee')),
            ],
        ),
    ]
