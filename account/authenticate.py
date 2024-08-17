from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
            if user is not None:
                if user.check_password(password):
                    return user
            return None
        except User.DoesNotExist:
            return None
        
        
    def get_user(self, request, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None