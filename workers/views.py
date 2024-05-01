# workers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import WorkerLoginForm, WorkerSignupForm  # Import WorkerSignupForm
from .models import Worker
from tasks.models import Task
from tasks.forms import TaskNoteForm, TaskCompletionForm
from django.utils import timezone

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import WorkerLoginForm


def worker_logout(request):
    logout(request)
    return redirect('worker_login')

def worker_login(request):
    if request.method == 'POST':
        form = WorkerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('view_assigned_tasks')
            else:
                # User authentication failed, display a message suggesting sign up
                messages.error(request, 'Invalid username or password. If you don\'t have an account, please sign up.')
    else:
        form = WorkerLoginForm()
    return render(request, 'workers/login_signup.html', {'form': form})


def worker_signup(request):
    if request.method == 'POST':
        form = WorkerSignupForm(request.POST)
        if form.is_valid():
            # Save the user object
            user = form.save()
            # Create a corresponding Worker object
            is_available = True if form.cleaned_data['availability'] == 'True' else False
            Worker.objects.create(user=user, is_available=is_available)
            # Authenticate and login the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('view_assigned_tasks')
        else:
            messages.error(request, form.errors)
    else:
        form = WorkerSignupForm()
    return render(request, 'workers/login_signup.html', {'form': form})


def view_assigned_tasks(request):
    assigned_tasks = Task.objects.filter(assignee=request.user, completed=False)
    task_id = request.POST.get('task_id') if request.POST.get('task_id') else None
    if request.method == 'POST':
        if 'note_form' in request.POST:
            note_form = TaskNoteForm(request.POST)
            if note_form.is_valid():
        
                notes = note_form.cleaned_data['notes']
                task = Task.objects.get(pk=task_id)
                task.notes = notes
                task.save()
                messages.success(request, 'Notes added successfully.')
                return redirect('view_assigned_tasks')
        elif 'completed_reason' in request.POST:
            completion_form = TaskCompletionForm(request.POST)
            if completion_form.is_valid():
                #task_id = completion_form.cleaned_data.get('task_id') if completion_form.cleaned_data.get('task_id') else 
                completion_reason = completion_form.cleaned_data['completed_reason']
                task = Task.objects.get(pk=task_id)
                task.completed = True
                task.completed_reason = completion_reason
                task.completed_at = timezone.now()
                task.save()
                messages.success(request, 'Task completed successfully.')
                return redirect('view_assigned_tasks')
    else:
        note_form = TaskNoteForm()
        completion_form = TaskCompletionForm()
    return render(request, 'assigned_tasks.html', {'assigned_tasks': assigned_tasks, 'note_form': note_form, 'completion_form': completion_form})

    
def add_task_note(request, task_id):
    if request.user.is_authenticated and isinstance(request.user, Worker):
        task = Task.objects.get(pk=task_id)
        if request.method == 'POST':
            form = TaskNoteForm(request.POST)
            if form.is_valid():
                task.notes = form.cleaned_data['notes']
                task.save()
                return redirect('view_assigned_tasks')
        else:
            form = TaskNoteForm()
        return render(request, 'add_task_note.html', {'form': form})
    else:
        return redirect('worker_login')
@login_required
def complete_task(request, task_id):
    if request.user.is_authenticated and isinstance(request.user, Worker):
        task = Task.objects.get(pk=task_id)
        if request.method == 'POST':
            form = TaskCompletionForm(request.POST)
            if form.is_valid():
                task.completed_at = timezone.now()
                task.completion_reason = form.cleaned_data['completion_reason']
                task.save()
                return redirect('view_assigned_tasks')
        else:
            form = TaskCompletionForm()
        return render(request, 'complete_task.html', {'form': form})
    else:
        return redirect('worker_login')
