# workers/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Worker

class WorkerLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class WorkerSignupForm(UserCreationForm):
    #availability = forms.BooleanField(label='Availability', required=True)
    availability=forms.CharField(max_length=5)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'availability']


# tasks/forms.py
from django import forms
from tasks.models import Task  # Import the Task model

class TaskNoteForm(forms.ModelForm):  # Change to ModelForm
    class Meta:
        model = Task  # Set the model to Task
        fields = ['notes']  # Specify the field(s) you want to include in the form

class TaskCompletionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed_reason']
