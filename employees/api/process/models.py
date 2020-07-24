from django.contrib.postgres.fields import JSONField
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Departments(models.Model):
	dept_id = models.AutoField(primary_key=True)
	dept_name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.dept_name
	
# class Templates(models.Model):
# 	template_id = models.AutoField(primary_key=True)
# 	template_name = models.CharField(max_length=50)
# 	depts_template = models.ForeignKey("Departments", related_name="template_depts", on_delete=models.CASCADE, null=True)

# 	def __str__(self):
# 		return self.template_name
	


# Table Process as PP
# {
#   Process_id int
#   Process_name string
#   Process_description string
#   Process_training video
#   process_department int
#   process_time_allocated time
 
 
# }

class Process(models.Model):
	process_id = models.AutoField(primary_key=True)
	process_name = models.CharField(max_length=50)
	process_description = models.CharField(max_length=50, blank=True, null=True)
	process_training = models.FileField(blank=True, null=True, upload_to='process/videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm'])])
	# process_department = models.PositiveSmallIntegerField()  # Fk dept id from employee models
	process_department = models.ForeignKey("Departments", related_name='depts', on_delete=models.CASCADE)
	process_time_allocated = models.DurationField(blank=True)
	
	def __str__(self):
		return self.process_name
	

# Table process_mainid as PMI
# {
#   Process_mainid int
#   Process_id int
#   main_name string
#   offsetx float
#   offsety float
#   main_attachment Videojpeg
#   main_description string
#   main_department int
 
# }

class ProcessMainid(models.Model):
	process_mainid = models.AutoField(primary_key=True)
	process_id = models.ForeignKey("Process", related_name='processes', on_delete=models.CASCADE)
	main_name = models.CharField(max_length=50, blank=True, null=True)
	offsetx = models.FloatField()
	offsety = models.FloatField()
	main_attachment = models.FileField(blank=True, null=True, upload_to='process_main/videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])])
	main_description = models.TextField(max_length=200, editable=True, blank=True)
	# main_department = models.SmallIntegerField()  # Fk dept id from employee models
	main_department = models.ForeignKey("Departments", related_name='mdepts', on_delete=models.CASCADE)

	def __str__(self):
		return self.main_name

# Table Process_subpoint as PSI
# {
#   Process_subpointid int
#   Process_mainid int
#   subpoint_name string
#   subpoint_attachment Videojpeg
#   subpoint_description string
 
# }

class ProcessSubpoint(models.Model):
	process_subpointid = models.AutoField(primary_key=True)
	pmain_id = models.ForeignKey("ProcessMainid", related_name='mainprocess', on_delete=models.CASCADE)
	subpoint_name = models.CharField(max_length=50, blank=True, null=True)
	subpoint_attachment = models.FileField(blank=True, null=True, upload_to='process_subpoint/videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])])
	subpoint_description = models.TextField(max_length=100, editable=True, blank=True)

	def __str__(self):
		return self.subpoint_name

# Table connections as CC
# {

#    Connector_id int
#    Start_mainpoint_id int
#    End_mainpoint_id int
#    Connector_text string
   
# }

class Connections(models.Model):
	connector_id = models.AutoField(primary_key=True)
	connection_process = models.ForeignKey("Process", related_name='connectors', on_delete=models.CASCADE, null=True)
	# start_mainpoint_id = models.IntegerField()  # FK to mainid
	start_mainpoint_id = models.ForeignKey("ProcessMainid", related_name='mainconnect', on_delete=models.CASCADE)
	# end_mainpoint_id = models.IntegerField()  # FK to mainid
	end_mainpoint_id = models.ForeignKey("ProcessMainid", related_name='mainconnector', on_delete=models.CASCADE)
	connector_text = models.CharField(max_length=50)

	def __str__(self):
		return self.connector_text



# table Repeat_task as RT
# {
# repeat_id int
# Repeat_type string
# interval_repeat int
# end_date date
# weekly_days jsonstring
# monthly_date int
# Yearly_date date
# Yearly_month string

# }

class RepeatTask(models.Model):
	repeat_id = models.AutoField(primary_key=True)
	repeat_type = models.CharField(max_length=50)
	interval_repeat = models.IntegerField()
	end_date = models.DateField()
	weekly_days = JSONField()
	monthly_date = models.IntegerField()
	yearly_date = models.DateField()
	yearly_month = models.CharField(max_length=50)

	def __str__(self):
		return self.repeat_type


# Table Regular_Task as RGT
# {
#   Regular_Task_id int
#   Task_name String
#   Task_departname String
#   Process_id int
#   task_type string
#   members json
#   Task_description String
#   Task_files json
#   task_duedate datetime
#   repeat_id int
 
# }

class RegularTask(models.Model):
	regular_task_id = models.AutoField(primary_key=True)
	task_name = models.CharField(max_length=50)
	task_deptname = models.CharField(max_length=50)
	prc_id = models.ForeignKey("Process", related_name='regularprocess', on_delete=models.CASCADE)
	task_type = models.CharField(max_length=50)
	members = JSONField()
	task_description = models.TextField(max_length=100, blank=True, null=True)
	task_files = JSONField()
	task_duedate = models.DateField()
	# repeat_id = models.ForeignKey("RepeatTask", related_name='repeats', on_delete=models.CASCADE)
	cron = models.CharField(max_length=50, default='')

	def __str__(self):
		return self.task_name
	


# Table Flow as ff

# {
#   flow_id int
#   regular_task_id int
#   percentage_complete float
# }

class Flow(models.Model):
	flow_id = models.AutoField(primary_key=True)
	regular_task = models.ForeignKey("RegularTask", related_name='taskflow', on_delete=models.CASCADE)
	percentage_complete = models.FloatField()

	def __str__(self):
		return self.flow_id
	

# Table flow_main_checklist as fmc

# {
 
#   flow_main_id int
#   flow_id int
#   process_mainid int
#   files_main Videojpeg
#   is_checked boolean
 
# }
class FlowMainChecklist(models.Model):

	flow_main_id = models.AutoField(primary_key=True)
	flow = models.ForeignKey("Flow", related_name='flows', on_delete=models.CASCADE)
	mprocess = models.ForeignKey("ProcessMainid", related_name='mainprocessflow', on_delete=models.CASCADE)
	files_main = models.FileField(blank=True, null=True, upload_to='flow_main_chklist/videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])])
	is_checked = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return self.flow_main_id


# Table flow_subpoint_checklist as fsc
# {
#   flow_subpoint_id int
#   flow_main_id int
#   flow_id int
#   process_subpointid int
#   files_main Videojpeg
#   is_checked boolean
 
# }

class FlowSubpointChecklist(models.Model):

	flow_subpoint_id = models.AutoField(primary_key=True)
	flow_main = models.ForeignKey("FlowMainChecklist", related_name='mainflow', on_delete=models.CASCADE)
	flowpt = models.ForeignKey("Flow", related_name='flowss', on_delete=models.CASCADE)
	subpoint = models.ForeignKey("ProcessSubpoint", related_name='subs', on_delete=models.CASCADE)
	files_main = models.FileField(blank=True, null=True, upload_to='flow_subpt_chklist/videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])])

	def __str__(self):
		return self.flow_subpoint_id



# ref: ff.regular_task_id - RGT.Regular_Task_id
# ref: fmc.flow_id - ff.flow_id
# ref: fmc.process_mainid - PMI.Process_mainid
# ref: fsc.flow_id - ff.flow_id
# ref: fsc.flow_subpoint_id - PSI.Process_subpointid


#  Table time as tt
 
#  {
#     flow_time_id int
#     flow_id int
#     user_id int
#     main_point_id int
#     subpoint_id int
#     starttime datetime
#     stoptime datetime
#     total_time time
 
 
#  }

#  ref: tt.flow_id - ff.flow_id
#  ref: tt.main_point_id - PMI.Process_mainid
#  ref: tt.subpoint_id - PSI.Process_subpointid

class Time(models.Model):

	flow_time_id = models.AutoField(primary_key=True)
	tflow = models.ForeignKey("Flow", related_name='timeflows', on_delete=models.CASCADE)
	user_id = models.IntegerField()
	mainpoints = models.ForeignKey("ProcessMainid", related_name='maintime', on_delete=models.CASCADE)
	subpoints = models.ForeignKey("ProcessSubpoint", related_name='subtime', on_delete=models.CASCADE)
	starttime = models.DurationField(blank=True)
	stoptime = models.DurationField(blank=True)
	total_time = models.DurationField(blank=True)

	def __str__(self):
		return self.flow_time_id