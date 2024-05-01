import pytest
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tasks.models import Task
from tasks.forms import LodgeComplaintForm
from tasks.views import TaskListCreateAPIView, submission_success, lodge_complaint


@pytest.fixture
def task_data():
    return {
        'title': 'Test Task',
        'description': 'Test Description',
        'priority': 'High',
        'severity': 'Critical',
        'deadline': '2024-05-01',
    }


@pytest.mark.django_db
def test_task_list_create_api_view_get_queryset():
    task = Task.objects.create(title='Test Task', description='Test Description',
                               priority='High', severity='Critical', deadline='2024-05-01')
    view = TaskListCreateAPIView()
    assert view.get_queryset().count() == 1


@pytest.mark.django_db
def test_task_list_create_api_view_post(client, task_data):
    url = reverse('task_list_create')
    response = client.post(url, task_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1


def test_submission_success(client):
    url = reverse('submission_success')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_lodge_complaint_get(client):
    url = reverse('lodge_complaint')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'form' in response.context


@pytest.mark.django_db
def test_lodge_complaint_post_valid(client, task_data):
    url = reverse('lodge_complaint')
    response = client.post(url, task_data)
    assert response.status_code == status.HTTP_302_FOUND
    assert Task.objects.count() == 1
