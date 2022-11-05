from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()


class Tender(models.Model):
    tender_holder=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField()
    date_due=models.DateField()
    location=models.CharField(max_length=255)
    tender_picture = models.ImageField(default="wallpaper4.jpg", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Tender {self.name} by {self.tender_holder.id}>"


class Input(models.Model):
    input_holder=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    location=models.CharField(max_length=255)
    input_picture = models.ImageField(default="wallpaper4.jpg", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Input {self.name} by {self.input_holder.id}>"

class Investment(models.Model):
    investor_holder=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField()
    location=models.CharField(max_length=255)
    investment_picture = models.ImageField(default="wallpaper4.jpg", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"<Investment {self.name} by {self.investor_holder.id}>"
