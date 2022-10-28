from django.contrib import admin
from .models import Input, Investment, Tender

# Register your models here.

@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display=['name', 'price', 'quantity']
    list_filter=['location', 'created_at']

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display=['name', 'date_due']
    list_filter=['location', 'created_at']

@admin.register(Investment)
class InputAdmin(admin.ModelAdmin):
    list_display=['name', 'created_at']
    list_filter=['location', 'created_at']
