# tasks/models.py

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=20)
    severity = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    deadline = models.DateField() 
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    COMPLETION_REASON_CHOICES = [
        ('reason1', 'Reason 1'),
        ('reason2', 'Reason 2'),
        ('reason3', 'Reason 3'),
        # can add more choices as per need
    ]
    completed_reason = models.CharField(max_length=100, choices=COMPLETION_REASON_CHOICES, null=True, blank=True)
    notes = models.TextField(blank=True)

class Complaint(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=50)
    severity = models.CharField(max_length=50)
    deadline = models.DateField()

    def __str__(self):
        return self.title
class Meta:
        app_label = 'tasks'