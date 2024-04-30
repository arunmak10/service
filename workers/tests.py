# workers/tests.py

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Worker

class WorkerModelTests(TestCase):
    def test_worker_creation(self):
        user = User.objects.create(username="test_worker")
        worker = Worker.objects.create(user=user, expertise="Test Expertise")
        self.assertEqual(worker.user.username, "test_worker")
        self.assertEqual(worker.expertise, "Test Expertise")
        self.assertTrue(worker.is_available)

# Add more tests for views if needed
