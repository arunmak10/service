import pytest
from django.contrib.auth.models import User
from workers.forms import WorkerLoginForm, WorkerSignupForm
from tasks.forms import TaskNoteForm, TaskCompletionForm


@pytest.mark.django_db
def test_worker_login_form():
    form_data = {'username': 'testuser', 'password': 'testpassword'}
    form = WorkerLoginForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_worker_signup_form():
    form_data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword', 'availability': 'True'}
    form = WorkerSignupForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_task_note_form():
    user = User.objects.create_user(username='testuser', password='testpassword')
    form_data = {'notes': 'Test note for the task.'}
    form = TaskNoteForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_task_completion_form():
    user = User.objects.create_user(username='testuser', password='testpassword')
    form_data = {'completed_reason': "reason1"}
    form = TaskCompletionForm(data=form_data)
    assert form.is_valid()
