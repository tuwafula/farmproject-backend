from email.policy import default
from .models import Input, Investment, Tender
from rest_framework import serializers


class TenderViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    date_due=serializers.DateField()
    location=serializers.CharField(max_length=255)
    tender_picture = serializers.ImageField(default='wallpaper4.jpg')
   
    class Meta:
        model = Tender
        fields = [
            'id','name','description', 'date_due', 'location', 'tender_picture'
        ]

class TenderDetailViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    date_due=serializers.DateField()
    location=serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    tender_picture = serializers.ImageField(default='wallpaper4.jpg')
   
    class Meta:
        model = Tender
        fields = [
            'id','name','description', 'date_due', 'location', 'created_at', 'updated_at', 'tender_picture'
        ]


class InvestViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    location=serializers.CharField(max_length=255)
    investment_picture = serializers.ImageField(default='wallpaper4.jpg')

    class Meta:
        model = Investment
        fields = [
            'id','name', 'description', 'location', 'investment_picture'
        ]

class InvestDetailViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    location=serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    investment_picture = serializers.ImageField(default='wallpaper4.jpg')

   
    class Meta:
        model = Input
        fields = [
            'id','name','description','location', 'created_at', 'updated_at', 'investment_picture'
        ]



class InputViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity=serializers.IntegerField()
    location=serializers.CharField(max_length=255)
    input_picture=serializers.ImageField(default='wallpaper4.jpg')


    class Meta:
        model = Input
        fields = [
            'id','name', 'description', 'quantity', 'price', 'location', 'input_picture'
        ]

class InputDetailViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity=serializers.IntegerField()
    location=serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    input_picture = serializers.ImageField(default='wallpaper4.jpg')

   
    class Meta:
        model = Input
        fields = [
            'id','name','description', 'quantity', 'price','location', 'created_at', 'updated_at', 'input_picture'
        ]



