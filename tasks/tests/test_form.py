# test_form.py

import pytest
from tasks.forms import LodgeComplaintForm, TaskNoteForm, TaskCompletionForm

@pytest.mark.django_db
def test_lodge_complaint_form():
    # Test valid form data
    form_data = {
        'title': 'Test Complaint',
        'description': 'This is a test complaint.',
        'priority': 'High',
        'severity': 'Critical',
        'deadline': '2024-05-01',
    }
    form = LodgeComplaintForm(data=form_data)
    assert form.is_valid()

    # Test invalid form data
    invalid_form_data = {
        'title': '',
        'description': 'This is a test complaint.',
        'priority': 'High',
        'severity': 'Critical',
        'deadline': '2024-05-01',
    }
    form = LodgeComplaintForm(data=invalid_form_data)
    assert not form.is_valid()

@pytest.mark.django_db
def test_task_note_form():
    # Test valid form data
    form_data = {
        'notes': 'Test note for the task.',
    }
    form = TaskNoteForm(data=form_data)
    assert form.is_valid()
