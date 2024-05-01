# tests/test_urls.py

from django.urls import reverse, resolve
from tasks.views import TaskListCreateAPIView, lodge_complaint, submission_success
from field_service.views import HomePageView

def test_home_page_url():
    url = reverse('home')
    assert resolve(url).func.view_class == HomePageView

def test_task_list_create_url():
    url = reverse('task_list_create')
    assert resolve(url).func.view_class == TaskListCreateAPIView

def test_lodge_complaint_url():
    url = reverse('lodge_complaint')
    assert resolve(url).func == lodge_complaint

def test_submission_success_url():
    url = reverse('submission_success')
    assert resolve(url).func == submission_success
