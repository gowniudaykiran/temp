from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime
from django.core.exceptions import ValidationError 
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin

def validate_digit_length(phone):
    if not (phone.isdigit() and len(phone) == 10):    
        raise ValidationError('%(phone)s must be 10 digits', params={'phone': phone},)

class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, email, name, phone_number, password=None):
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, phone_number, password=None):
        
        user = self.create_user(
            email,
            password=password,
            phone_number=phone_number,         
            name=name,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password=None):

        user = self.create_user(
            email,
            password=password,
            phone_number=phone_number,
            name= name,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(verbose_name="Phone number", max_length=10,  
                                    validators=[validate_digit_length],unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'phone_number','name',]
    is_staff = models.BooleanField(_('staff status'),default=False)
    is_active = models.BooleanField(_('active status'),default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    





