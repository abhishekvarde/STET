from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from datetime import datetime, timezone

from django.utils.timezone import utc


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, phone_no, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(username=username, email=self.normalize_email(email))
        user.phone_no = phone_no
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=300, unique=True, verbose_name="Email Address")
    phone_no = models.CharField(max_length=10, unique=True)
    otp = models.CharField(max_length=10, default="1234")
    otp_generated_time = models.DateTimeField(verbose_name="otp time", auto_now_add=True)
    no_of_attempts = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True

    def validateotp(self):
        print(datetime.now())
        print(datetime.now())
        print(datetime.now())
        print(datetime.now())
        print(self.otp_generated_time.utcnow().replace(tzinfo=utc))
        print(type(self.otp_generated_time))
        time = datetime.now(timezone.utc) - self.otp_generated_time
        print(datetime.now(timezone.utc))
        print(self.otp_generated_time)
        self.no_of_attempts = self.no_of_attempts + 1

        print(self.no_of_attempts)
        print(time.total_seconds())
        if time.total_seconds() > 30 or int(str(self.no_of_attempts)) > 5:
            return False
        return True
