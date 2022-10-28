from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))

        email=self.normalize_email(email)

        new_user=self.model(email=email, **extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user



    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))

        return self.create_user(email, password, **extra_fields)

    def create_farmeruser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_farmer', True)

        if extra_fields.get('is_farmer') is not True:
            raise ValueError(_("Farmer should have is_farmer as True"))
	    
        return self.create_user(email, password, **extra_fields)
  
    def create_inputuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_input_holder', True)

        if extra_fields.get('is_input_holder') is not True:
            raise ValueError(_("Input holder should have is_inputuser as True"))
	    
        return self.create_user(email, password, **extra_fields)

    def create_investoruser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_investor', True)

        if extra_fields.get('is_investor') is not True:
            raise ValueError(_("Investor should have is_investoruser as True"))
	    
        return self.create_user(email, password, **extra_fields)


    def create_tenderuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_tender_holder', True)

        if extra_fields.get('is_tender_holder') is not True:
            raise ValueError(_("Tender holder should have is_tenderuser as True"))
	    
        return self.create_user(email, password, **extra_fields)

    
class User(AbstractUser):
    username=models.CharField(max_length=25, unique=True)
    email=models.EmailField(max_length=80, unique=True)
    phone_number=PhoneNumberField(null=False, unique=True)
    is_farmer = models.BooleanField(default=False)
    is_tender_holder = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    is_input_holder = models.BooleanField(default=False)


    USERNAME_FIELD="email"

    REQUIRED_FIELDS= ['username', 'phone_number']

    objects=CustomUserManager()

    def __str__(self):
        return f"<User {self.email}"
