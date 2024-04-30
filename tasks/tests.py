# tasks/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTests(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", description="Test Description", priority="High", severity="Low", deadline="2024-04-30T12:00:00Z")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.severity, "Low")
        self.assertEqual(str(task.deadline), "2024-04-30 12:00:00+00:00")

# Add more tests for views if needed
