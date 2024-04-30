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


""" 
class TaskCompletionForm(forms.ModelForm):
    # Define choices for the completion reason
    COMPLETION_REASON_CHOICES = [
        ('reason1', 'Reason 1'),
        ('reason2', 'Reason 2'),
        ('reason3', 'Reason 3'),
        # Add more choices as needed
    ]

    # Define the completion_reason field with choices
    completed_reason = forms.ChoiceField(choices=COMPLETION_REASON_CHOICES, widget=forms.Select)

    class Meta:
        model = Task
        fields = ['completed_reason'] """
""" 
from tasks.forms import TaskCompletionForm as BaseTaskCompletionForm

class TaskCompletionForm(BaseTaskCompletionForm):
    # You can customize or override fields if needed
    pass
 """
""" from django import forms

class TaskNoteForm(forms.Form):
    #task_id = forms.IntegerField()
    notes = forms.CharField(widget=forms.Textarea)

class TaskCompletionForm(forms.Form):
    completed_reason = forms.CharField(widget=forms.Textarea)#forms.CharField(max_length=100)
 """