""" # test_task_admin.py

import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import RequestFactory
from mixer.backend.django import mixer  # You can use Mixer for creating test data
from myapp.admin import TaskAdmin
from myapp.models import Task
from myapp.models import Worker  # Adjust import based on your app structure


@pytest.fixture
def admin_site():
    return AdminSite()


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def task_admin(admin_site):
    return TaskAdmin(Task, admin_site)


@pytest.mark.django_db
def test_task_admin_formfield_for_foreignkey(task_admin):
    # Create a mock user with worker profile
    user = mixer.blend(User)
    worker = mixer.blend(Worker, user=user, is_available=True)

    # Create a mock task object
    task = mixer.blend(Task)

    # Mock database query
    queryset = task_admin.formfield_for_foreignkey(None, None)['queryset']

    # Assertion
    assert worker in queryset


@pytest.mark.django_db
def test_task_admin_changelist_view(task_admin, request_factory):
    # Create mock tasks
    mixer.cycle(5).blend(Task)

    # Create a mock request
    request = request_factory.get('/admin/tasks/task/')
    request.user = mixer.blend(User)

    # Get changelist view response
    response = task_admin.changelist_view(request)

    # Assertion for total created tasks count
    assert response.context_data['total_created_tasks'] == 5

    # Assertion for total completed tasks count
    assert response.context_data['total_completed_tasks'] == 0
 """