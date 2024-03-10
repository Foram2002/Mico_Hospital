# from .collections import *
from django.db import models
from paramiko import PKey
# from django.contrib.auth.models import User



# Create your models here.
class Users(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    number=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=6)
    confirm_password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,default='users')
    status = models.BooleanField(default=1)

    #cheack models 
    def __str__(self):
        return self.fname+" - "+self.role


class Patient(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    symptoms=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50,blank=False)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.city + " "+self.country
    
class Doctor(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=50)
    days_of_treatment=models.CharField(max_length=50)
    fees=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.doctor_name
    
class Treatment(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    nephrologist=models.CharField(max_length=100)
    eye_care=models.CharField(max_length=100)
    pediatrician_clinic=models.CharField(max_length=100)
    parental_care=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nephrologist

class Contact_us(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact_no=models.CharField(max_length=50)
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.fullname
