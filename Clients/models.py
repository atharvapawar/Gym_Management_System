from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True)

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    total_fees = models.IntegerField()
    enrolled_on = models.DateField(auto_now_add=True)  

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

