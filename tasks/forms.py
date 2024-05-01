from django import forms
from .models import Complaint, Task

class LodgeComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'priority', 'severity', 'deadline']

class TaskNoteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['notes']

class TaskCompletionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed_reason']
