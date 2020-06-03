from django.contrib.postgres.fields import JSONField
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

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
	process_description = models.CharField(max_length=50)
	process_training = models.FileField(upload_to='dropbox/videos', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'log', 'mp4', 'png', 'jpeg', 'jpg', 'webm'])])
	process_department = models.PositiveSmallIntegerField() # Fk dept id from employee models
	process_time_allocated = models.TimeField(blank=True)
	
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
	main_name = models.CharField(max_length=50)
	offsetx = models.FloatField()
	offsety = models.FloatField()
	main_attachment = models.FileField(upload_to='dropbox/videos_main', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])])
	main_description = models.TextField(max_length=200, editable=True, blank=True)
	main_department = models.SmallIntegerField()  # Fk dept id from employee models

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
	subpoint_name = models.CharField(max_length=50)
	subpoint_attachment = models.FileField(upload_to='dropbox/videos_subprocess', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'png', 'jpeg', 'jpg'])])
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
	start_mainpoint_id = models.IntegerField()
	end_mainpoint_id = models.IntegerField()
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
	task_description = models.TextField(max_length=100)
	task_files = JSONField()
	task_duedate = models.DateField()
	repeat_id = models.ForeignKey("RepeatTask", related_name='repeats', on_delete=models.CASCADE)