""" # workers/urls.py

from django.urls import path
from .views import WorkerListCreateAPIView, WorkerRetrieveUpdateDestroyAPIView, WorkerLoginView

urlpatterns = [
    path('login/', WorkerLoginView.as_view(), name='worker_login'),
    path('workers/', WorkerListCreateAPIView.as_view(), name='worker_list_create'),
    path('workers/<int:pk>/', WorkerRetrieveUpdateDestroyAPIView.as_view(), name='worker_retrieve_update_destroy'),
]
 """

# workers/urls.py
from django.urls import path
from .views import worker_login, view_assigned_tasks, add_task_note, complete_task, worker_signup, worker_logout

urlpatterns = [
    path('login/', worker_login, name='worker_login'),
    path('signup/', worker_signup, name='worker_signup'),  # Add this line for worker signup
    path('assigned_tasks/', view_assigned_tasks, name='view_assigned_tasks'),
    path('add_task_note/<int:task_id>/', add_task_note, name='add_task_note'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('logout/', worker_logout, name='worker_logout'),
]



