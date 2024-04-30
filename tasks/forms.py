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

""" class TaskCompletionForm(forms.ModelForm):
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
        fields = ['completed_reason']
 """