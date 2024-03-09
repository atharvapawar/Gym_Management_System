from django.db import models


# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

