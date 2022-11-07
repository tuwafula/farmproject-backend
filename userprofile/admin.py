from django.contrib import admin
from .models import TenderProfile, InputProfile, InvestorProfile, FarmerProfile

# Register your models here.
admin.site.register((TenderProfile, InputProfile, InvestorProfile, FarmerProfile))
