import pytest
from django.contrib.auth.models import User
from django.test import Client
from workers.forms import WorkerLoginForm, WorkerSignupForm
from workers.models import Worker
from tasks.models import Task
from django.urls import reverse
from tasks.forms import TaskNoteForm, TaskCompletionForm


@pytest.mark.django_db
def test_worker_login_view():
    client = Client()
    url = reverse('worker_login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context
    assert isinstance(response.context['form'], WorkerLoginForm)

@pytest.mark.django_db
def test_worker_signup_view():
    client = Client()
    url = reverse('worker_signup')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context
    assert isinstance(response.context['form'], WorkerSignupForm)

@pytest.mark.django_db
def test_view_assigned_tasks_view():
    user = User.objects.create(username='testuser')
    worker = Worker.objects.create(user=user, expertise='Test Expertise', is_available=True)
    client = Client()
    client.force_login(user)
    url = reverse('view_assigned_tasks')
    response = client.get(url)
    assert response.status_code == 200
    assert 'assigned_tasks' in response.context
    assert 'note_form' in response.context
    assert 'completion_form' in response.context

@pytest.mark.django_db
def test_fail_task_note_view():
    user = User.objects.create(username='testuser')
    worker = Worker.objects.create(user=user, expertise='Test Expertise', is_available=True)
    task = Task.objects.create(title='Test Task', description='Test Description', priority='High', severity='Critical', deadline='2024-05-01', assignee=user)
    client = Client()
    client.force_login(user)
    url = reverse('add_task_note', kwargs={'task_id': task.id})
    response = client.get(url)
    assert response.status_code != 200

