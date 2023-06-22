from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, profile_id=None, password=None, **extra_fields):
        if not profile_id:
            raise ValueError('Profile ID must be provided')

        user = self.model(profile_id=profile_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, profile_id, password, **extra_fields):
        user = self.create_user(profile_id=profile_id, password=password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)

        return user