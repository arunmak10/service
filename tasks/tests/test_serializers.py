# tests/test_serializers.py

import pytest
from tasks.models import Task, Complaint
from tasks.serializers import TaskSerializer, ComplaintSerializer, TaskCreateSerializer, TaskUpdateSerializer
from datetime import datetime, timedelta
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create(username='test_user')

@pytest.fixture
def task_data(user):
    return {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'priority': 'High',
        'severity': 'Critical',
        'deadline': (datetime.now() + timedelta(days=7)).date(),
        'assignee': user.id
    }

@pytest.fixture
def complaint_data():
    return {
        'title': 'Test Complaint',
        'description': 'This is a test complaint.',
        'priority': 'High',
        'severity': 'Critical',
        'deadline': (datetime.now() + timedelta(days=7)).date(),
    }

@pytest.mark.django_db
def test_task_serializer(task_data):
    serializer = TaskSerializer(data=task_data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_complaint_serializer(complaint_data):
    serializer = ComplaintSerializer(data=complaint_data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_task_create_serializer(task_data):
    serializer = TaskCreateSerializer(data=task_data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_task_update_serializer():
    task = Task.objects.create(
        title='Test Task',
        description='This is a test task.',
        priority='',
        severity='Critical',
        deadline=datetime.now(),
    )
    serializer = TaskUpdateSerializer(instance=task, data={'completed_at': datetime.now(), 'completed_reason': 'Completed successfully'})
    assert not serializer.is_valid()
