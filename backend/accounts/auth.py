from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class UsernameBackend(ModelBackend):
    def authenticate(self, request, profile_id=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(profile_id=profile_id)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None