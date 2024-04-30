""" # tasks/serializers.py

from rest_framework import serializers
from .models import Task, Complaint   

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'severity', 'deadline', 'assignee']

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['completed_at', 'completed_reason']
 """

from rest_framework import serializers
from .models import Task, Complaint   
from django.contrib.auth.models import User

class DateField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            return serializers.DateField().to_internal_value(data)
        except serializers.ValidationError:
            raise serializers.ValidationError("Enter a valid date.")

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'



class TaskCreateSerializer(serializers.ModelSerializer):
    deadline = DateField()
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'severity', 'deadline', 'assignee']

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['completed_at', 'completed_reason']
