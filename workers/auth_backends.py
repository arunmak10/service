""" # workers/auth_backends.py

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class WorkerBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(username=username)
            if user.check_password(password) and hasattr(user, 'worker'):
                return user.worker
        except user_model.DoesNotExist:
            return None
 """