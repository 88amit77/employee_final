from rest_framework import serializers
from api.process.models import *

##############################################
######  Serializers for process api ##########
##############################################

# Process
class ProcessSerializer(serializers.ModelSerializer):

	class Meta:
		model = Process
		fields = '__all__'
		depth = 1

# ProcessMainid
class ProcessMainidSerializer(serializers.ModelSerializer):
	process_id = ProcessSerializer()

	def to_internal_value(self, data):
		 self.fields['process_id'] = serializers.PrimaryKeyRelatedField(
			 queryset=Process.objects.all())
		 return super(ProcessSerializer, self).to_internal_value(data)
	
	class Meta:
		model = ProcessMainid
		fields = '__all__'
		depth = 1


# ProcessSubpoint
class ProcessSubpointSerializer(serializers.ModelSerializer):
	pmain_id = ProcessMainidSerializer()

	def to_internal_value(self, data):
		self.fields['pmain_id'] = serializers.PrimaryKeyRelatedField(
			queryset=ProcessMainid.objects.all())
		return super(ProcessMainidSerializer, self).to_internal_value(data)
	
	class Meta:
		model = ProcessSubpoint
		fields = '__all__'
		depth = 1

# Connections
class ConnectionsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Connections
		fields = '__all__'

# RepeatTask
class RepeatTaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = RepeatTask
		fields = '__all__'

# RegularTask
class RegularTaskSerializer(serializers.ModelSerializer):
	prc_id = ProcessSerializer()
	repeat_id = RepeatTaskSerializer()

	def to_internal_value(self, data):
		self.fields['prc_id'] = serializers.PrimaryKeyRelatedField(queryset=Process.objects.all())
		self.fields['repeat_id'] = serializers.PrimaryKeyRelatedField(queryset=RepeatTask.objects.all())
		return (super(ProcessSerializer, self).to_internal_value(data), super(RepeatTaskSerializer, self).to_internal_value(data))

		# self.fields['repeat_id'] = serializers.PrimaryKeyRelatedField(queryset=RepeatTask.objects.all())
		# return super(RepeatTaskSerializer, self).to_internal_value(data)
	
	class Meta:
		model = RegularTask
		fields = '__all__'