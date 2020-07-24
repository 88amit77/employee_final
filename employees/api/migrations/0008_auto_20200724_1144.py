# Generated by Django 3.0.7 on 2020-07-24 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_attendance_attendence_rules_attendenceleaveid_documents_education_empleaveapplied_empleaveid_employe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendenceleaveid',
            name='ar_id',
        ),
        migrations.RemoveField(
            model_name='attendenceleaveid',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='education',
            name='educations',
        ),
        migrations.RemoveField(
            model_name='empleaveapplied',
            name='action_by',
        ),
        migrations.RemoveField(
            model_name='empleaveapplied',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='empleaveapplied',
            name='leave_id',
        ),
        migrations.RemoveField(
            model_name='empleaveid',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='empleaveid',
            name='leave_id',
        ),
        migrations.RemoveField(
            model_name='familymembers',
            name='family_members',
        ),
        migrations.RemoveField(
            model_name='monthlyempsalary',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='workhistory',
            name='work_historys',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Attendence_rules',
        ),
        migrations.DeleteModel(
            name='AttendenceLeaveid',
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='EmpLeaveApplied',
        ),
        migrations.DeleteModel(
            name='EmpLeaveId',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='FamilyMembers',
        ),
        migrations.DeleteModel(
            name='LeaveRules',
        ),
        migrations.DeleteModel(
            name='MonthlyEmpSalary',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
        migrations.DeleteModel(
            name='WorkHistory',
        ),
    ]
