""" # tasks/views.py

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
 """


""" from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task, Complaint
from .serializers import TaskSerializer, TaskCreateSerializer, TaskUpdateSerializer, ComplaintSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        serializer.save()  # Override perform_create to assign the task to a worker if needed

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        tasks_serializer = self.get_serializer(queryset, many=True)
        complaints_queryset = Complaint.objects.all()
        complaints_serializer = ComplaintSerializer(complaints_queryset, many=True)
        data = {
            'tasks': tasks_serializer.data,
            'complaints': complaints_serializer.data
        }
        return Response(data)
# tasks/views.py

from django.shortcuts import render, redirect
from .forms import LodgeComplaintForm

def lodge_complaint(request):
    if request.method == 'POST':
        form = LodgeComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')  # Replace 'home' with the name of your home page URL
    else:
        form = LodgeComplaintForm()
    return render(request, 'home.html', {'form': form})
 """

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        serializer.save()  # Override perform_create to assign the task to a worker if needed

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .forms import LodgeComplaintForm
from .serializers import TaskCreateSerializer
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import LodgeComplaintForm

""" def lodge_complaint(request):
    #if request.method == 'POST':
    form = LodgeComplaintForm()#LodgeComplaintForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')  # Redirect to the home page after successful form submission
    else:
        form = LodgeComplaintForm()
    return render(request, 'home.html', {'form': form})
 """
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import LodgeComplaintForm
from .serializers import TaskCreateSerializer

""" @api_view(['GET', 'POST'])
def lodge_complaint(request):
    if request.method == 'POST':
        form = LodgeComplaintForm(request.POST)
        if form.is_valid():
            # Extract complaint details from the form
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            severity = form.cleaned_data['severity']
            deadline = form.cleaned_data['deadline']

            # Create a new Task object for the complaint
            task_data = {
                'title': title,
                'description': description,
                'priority': priority,
                'severity': severity,
                'deadline': deadline,
                'assignee': None,  # You may need to assign a worker here based on availability
            }
            serializer = TaskCreateSerializer(data=task_data)
            if serializer.is_valid():
                serializer.save()
                print('submission succefull saving !!!!!!')
                return render(request, 'submission_success.html')
                #render(request, 'home.html', {'form': form})
                #render(request, 'home.html', {'form': form})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = LodgeComplaintForm()
        return render(request, 'lodge_complaint.html', {'form': form})
    return render(request, 'home.html', {'form': form}) """


from django.shortcuts import render, redirect
from .forms import LodgeComplaintForm
from .serializers import TaskCreateSerializer

def submission_success(request):
    return render(request, 'submission_success.html')

@api_view(['GET', 'POST'])
def lodge_complaint(request):
    if request.method == 'POST':
        form = LodgeComplaintForm(request.POST)
        print('Submission successful! Complaint saved 1.')
        if form.is_valid() or True:
            print('Submission successful! Complaint saved.2.')
            # Extract complaint details from the form
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            severity = form.cleaned_data['severity']
            deadline = form.cleaned_data['deadline']

            # Create a new Task object for the complaint
            task_data = {
                'title': title,
                'description': description,
                'priority': priority,
                'severity': severity,
                'deadline': deadline,
                'assignee': None,  # You may need to assign a worker here based on availability
            }
            serializer = TaskCreateSerializer(data=task_data)
            if serializer.is_valid():
                print('Submission successful! Complaint saved.3.')
                serializer.save()
                print('Submission successful! Complaint saved.')
                return redirect('submission_success')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: 
            
            # Output validation errors to the logs or console
            print(form.errors)
            # Or log the errors using the logging module
            import logging
            logging.error(form.errors)
    else:
        form = LodgeComplaintForm()
    return render(request, 'lodge_complaint.html', {'form': form})


