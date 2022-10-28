from django.db import models
from django.db import models
from authentication.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class FarmerProfile(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)

    class Meta: 
        '''
        to set table name in database

        '''
        db_table = "farmer_profile"



class InvestorProfile(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investor_profile')
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)

    class Meta: 
        '''
        to set table name in database

        '''
        db_table = "investor_profile"
    


class TenderProfile(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenderholder_profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False) 

    class Meta: 
        '''
        to set table name in database

        '''
        db_table = "tenderholder_profile"

class InputProfile(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inputholder_profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    
    class Meta: 
        '''
        to set table name in database

        '''
        db_table = "inputholder_profile"