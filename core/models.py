import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, **extra_fields):
        if not email:
            raise ValueError("Debe tener email")

        email = self.normalize_email(email)
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff not True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser not True')

        return self.create_user(first_name, last_name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    objects = UserManager()

    def __str__(self):
        return self.email
