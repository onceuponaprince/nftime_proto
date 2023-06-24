
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    profile_id = models.IntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, default="", blank=True)
    profile_img = models.ImageField(upload_to='profile_imgs', blank=True)
    bio = models.TextField(blank=True)
    is_wallet_user = models.BooleanField(default=False,blank=True)
    is_active = models.BooleanField(default=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    accept_terms = models.BooleanField(default=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'profile_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.profile_id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
