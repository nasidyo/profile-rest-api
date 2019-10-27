from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """"Create a new user manager"""
        if not email:
            raise ValueError('User must have an email address!')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.seve(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """"Create a super user with detail"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.seve(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database models for users in the systems"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRES_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
