from .models import Input, Investment, Tender
from rest_framework import serializers


class TenderViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    date_due=serializers.DateField()
    location=serializers.CharField(max_length=255)
   
    class Meta:
        model = Tender
        fields = [
            'id','name','description', 'date_due', 'location'
        ]

class TenderDetailViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    date_due=serializers.DateField()
    location=serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

   
    class Meta:
        model = Tender
        fields = [
            'name','description', 'date_due', 'location', 'created_at', 'updated_at'
        ]


class InvestViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    location=serializers.CharField(max_length=255)
    
    class Meta:
        model = Investment
        fields = [
            'id','name', 'description', 'location'
        ]

class InvestDetailViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    location=serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

   
    class Meta:
        model = Input
        fields = [
            'name','description','location', 'created_at', 'updated_at'
        ]



class InputViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity=serializers.IntegerField()
    location=serializers.CharField(max_length=255)

    class Meta:
        model = Input
        fields = [
            'id','name', 'description', 'quantity', 'price', 'location'
        ]

class InputDetailViewSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity=serializers.IntegerField()
    location=serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

   
    class Meta:
        model = Input
        fields = [
            'name','description', 'quantity', 'price','location', 'created_at', 'updated_at'
        ]



