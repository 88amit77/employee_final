from rest_framework import serializers
from api.process.models import *

##############################################
######  Serializers for process api ##########
##############################################


class DeptSerializer(serializers.ModelSerializer):
	class Meta:
		model = Departments
		fields = '__all__'

class DeptRelatedField(serializers.RelatedField):

	def display_value(self, instance):
		return instance

	def to_representation(self, value):
		return str(value)

	def to_internal_value(self, data):
		return Departments.objects.get(dept_name=data)


# class TemplateSerializer(serializers.ModelSerializer):

# 	depts_template = DeptRelatedField(queryset=Departments.objects.all())
# 	class Meta:
# 		model = Templates
# 		fields = '__all__'


# Process
class ProcessSerializer(serializers.ModelSerializer):

	process_department = DeptRelatedField(queryset=Departments.objects.all())
	class Meta:
		model = Process
		fields = '__all__'
		depth = 1

class ProcessRelatedField(serializers.RelatedField):

	def display_value(self, instance):
		return instance

	def to_representation(self, value):
		return str(value)

	def to_internal_value(self, data):
		return Process.objects.get(process_name=data)

# ProcessMainid
class ProcessMainidSerializer(serializers.ModelSerializer):

	process_id = ProcessRelatedField(queryset=Process.objects.all())
	main_department = DeptRelatedField(queryset=Departments.objects.all())

	class Meta:
		model = ProcessMainid
		fields = '__all__'
		depth = 1



class ProcessSubpointRelatedField(serializers.RelatedField):

	def display_value(self, instance):
		return instance

	def to_representation(self, value):
		return str(value)

	def to_internal_value(self, data):
		return ProcessMainid.objects.get(main_name=data)


# ProcessSubpoint
class ProcessSubpointSerializer(serializers.ModelSerializer):

	pmain_id = ProcessSubpointRelatedField(queryset=ProcessMainid.objects.all())

	class Meta:
		model = ProcessSubpoint
		fields = '__all__'
		depth = 1

# Connections

# class ConnectionsRelatedField(serializers.RelatedField):

# 	def display_value(self, instance):
# 		return instance

# 	def to_representation(self, value):
# 		return str(value)

# 	def to_internal_value(self, data):
# 		return ProcessMainid.objects.get(main_name=data)

class ConnectionsSerializer(serializers.ModelSerializer):
	connection_process = ProcessRelatedField(queryset=Process.objects.all())
	# start_mainpoint_id = ConnectionsRelatedField(queryset=ProcessMainid.objects.all())
	# end_mainpoint_id = ConnectionsRelatedField(queryset=ProcessMainid.objects.all())

	class Meta:
		model = Connections
		fields = '__all__'


# RepeatTask
class RepeatTaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = RepeatTask
		fields = '__all__'


# class RegularTaskRelatedField(serializers.RelatedField):

# 	def display_value(self, instance):
# 		return instance

# 	def to_representation(self, value):
# 		return str(value)

# 	def to_internal_value(self, data):
# 		return ProcessMainid.objects.get(main_name=data)

# class RepeatTasksRelatedField(serializers.RelatedField):

# 	def display_value(self, instance):
# 		return instance

# 	def to_representation(self, value):
# 		return str(value)

# 	def to_internal_value(self, data):
# 		return RepeatTask.objects.get(repeat_type=data)

# RegularTask
class RegularTaskSerializer(serializers.ModelSerializer):

	prc_id = ProcessRelatedField(queryset=Process.objects.all())

	class Meta:
		model = RegularTask
		fields = '__all__'