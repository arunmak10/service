import pytest
from django.contrib.auth.models import User
from workers.models import Worker


@pytest.mark.django_db
def test_worker_model():
    user = User.objects.create(username='testuser')
    worker = Worker.objects.create(user=user, expertise='Test Expertise', is_available=True)
    assert worker.user.username == 'testuser'
    assert worker.expertise == 'Test Expertise'
    assert worker.is_available
