from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


# implement custom user model
# this class is helper class for providing helper functions for creating a user or creating a super user.
class UserManager(BaseUserManager):  # to override some methods
    def create_user(self, email, password=None, **extra_fields):  # **extra_fields: makes function more flexible
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        # normalize_email()은 BaseUserManager 의 built-in method
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# functions 는 없고 fields 만 존재
class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # 이걸로 인하여, 상위의 UserManager 클래스를 받아온 것 --> 왜 굳이 UserManager()를 만드는 거야?
    # 현재 클래스는 변수만 선언하고, 함수는 상위 클래스에서 받아오도록 분리한
    objects_ = UserManager()

    USERNAME_FIELD = 'email'
