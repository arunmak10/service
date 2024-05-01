# tests/test_models.py

import pytest
from tasks.models import Task, Complaint
from django.contrib.auth.models import User
from datetime import datetime, timedelta

@pytest.mark.django_db
def test_task_model_creation():
    user = User.objects.create(username='test_user')
    task = Task.objects.create(
        title='Test Task',
        description='This is a test task.',
        priority='High',
        severity='Critical',
        deadline=datetime.now() + timedelta(days=7),
        assignee=user,
        completed=False
    )
    assert task.title == 'Test Task'
    assert task.description == 'This is a test task.'
    assert task.priority == 'High'
    assert task.severity == 'Critical'
    assert task.deadline.date() == (datetime.now() + timedelta(days=7)).date()
    assert task.assignee == user
    assert not task.completed

@pytest.mark.django_db
def test_complaint_model_creation():
    complaint = Complaint.objects.create(
        title='Test Complaint',
        description='This is a test complaint.',
        priority='High',
        severity='Critical',
        deadline=datetime.now() + timedelta(days=7),
    )
    assert complaint.title == 'Test Complaint'
    assert complaint.description == 'This is a test complaint.'
    assert complaint.priority == 'High'
    assert complaint.severity == 'Critical'
    assert complaint.deadline.date() == (datetime.now() + timedelta(days=7)).date()
