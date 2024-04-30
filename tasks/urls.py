""" # tasks/urls.py

from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, lodge_complaint

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    #path('lodge_complaint', lodge_complaint, name='lodge_complaint'),  # Updated URL pattern
    path('lodge_complaint/', lodge_complaint, name='lodge_complaint'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_retrieve_update_destroy'),
    
]
 """

from django.urls import path
from .views import TaskListCreateAPIView, lodge_complaint, submission_success
from field_service.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('lodge_complaint/', lodge_complaint, name='lodge_complaint'),
    path('submission_success/', submission_success, name='submission_success'), 
]
