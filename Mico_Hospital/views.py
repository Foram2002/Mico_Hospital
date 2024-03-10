from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *
from .models import Doctor
import random
# import math

# Create your views here.
def Index(request):
    return render(request,"app/index.html")
def Signup(request):
    if request.POST:

        if 'Doctor' in request.POST['role']:
            fname=request.POST['fname']
            lname=request.POST['lname']
            number=request.POST['number']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['repassword']
            if password==confirm_password:
                Users.objects.create(fname=fname,lname=lname,number=number,email=email,password=password,confirm_password=confirm_password,role=request.POST['role'])
                
                message='Your Registration Successfully'
                return render(request,"app/login.html",{'msg':message})
            else:
                message='Email Already Exist'
                return render(request,"app/signup.html",{'msg':message})
            
        else:
            
            fname=request.POST['fname']
            lname=request.POST['lname']
            number=request.POST['number']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['repassword']
            if password==confirm_password:
                
                Users.objects.create(fname=fname,lname=lname,number=number,email=email,password=password,confirm_password=confirm_password,role=request.POST['role'])
                
                message='Your Registration Successfully'
                return render(request,"app/login.html",{'msg':message})
            else:
                message='Email Already Exist'
                return render(request,"app/signup.html",{'msg':message})
    else:
        return render(request,"app/signup.html")
    

def Login(request):

    # if "Doctor" in request.POST['role']:
        if request.method=="POST":
            email=request.POST['email']
            password=request.POST['password']
            newuser=Users.objects.get(email=email)

            if newuser:
                if newuser.password==password and newuser.role=="Doctor":
                    request.session['fname']=newuser.fname
                    request.session['lname']=newuser.lname
                    request.session['email']=newuser.email
                    return render(request,"app/index.html")
                else:
                    message="Password Does Not Match"
                    return render(request,"app/login.html",{'msg':message})
            else:
                message="User Does Not Exist"
                return render(request,"app/login.html",{'msg':message})

        return render(request,"app/login.html")

# def forget_pas


def Treatment(request):
    return render(request,"app/treatment.html")
    
def Logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,"app/signup.html")
    else:
        return render(request,"app/signup.html")
    
def Testimonial(request):
    return render(request,"app/testimonial.html")

def Doctor(request):
    return render(request,"app/doctor.html")

def Contact_us(request):
    if 'email' in request.session:
        if request.POST:
            Users.objects.get(email=request.session['email'])
            print(Users.objects.get(email=request.session['email']))
            fullname=request.POST['name']
            email=request.POST['email']
            phone_number=request.POST['number']
            message=request.POST['message']
            cid=Contact_us.objects.create(fullname=fullname,email=email,phone_number=phone_number,message=message)
            print(cid)
            if Users.role=="Doctor":
                return render(request,"app/contact.html",{'cd':cid})
            else:
                return render(request,"app/contact.html",{'cd':cid})
        else:
            return render(request,"app/contact.html")