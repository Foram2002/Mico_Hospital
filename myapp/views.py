
from django.shortcuts import render
from django.core.mail import send_mail
from Mico_Hospital.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from .models import *
from .models import Doctor
import random

# Create your views here.
def Index(request):
    return render(request,"app/index.html")

def Signup(request):
    if request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['repassword']
        if password==confirm_password:
            Users.objects.create(fname=fname,lname=lname,number=number,email=email,password=password,confirm_password=confirm_password,role=request.POST['role'])
            message='Your Registration Successfully'
            return render(request,"app/send_otp.html",{'msg':message})
        else:
            message='Email Already Exist'
            return render(request,"app/signup.html",{'msg':message})
    

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

def Forgot_password(request):
     return render(request,"app/forgot_password.html")

def send_otp(request):
        try:
            email=request.POST['email']
            generate_otp=random.randint(1111,9999)
            print(generate_otp)
            newuser=Users.objects.get(email=email)
            if newuser:
                send_mail(" Forgot Password ","mail_template",email,{'otp':generate_otp,'newu':newuser})
                print('mail_send')
                newuser.otp=generate_otp
                newuser.save()
                return render(request,'login.html')
            else:
                messaage="Email does not exist"
                return render(request,'forgot_password.html',{'msg':messaage})
        except:
            messaage="Email does not exist"
            return render(request,'forgot_password.html',{'msg':messaage})

def Reset_password(request):
	try:
		email=request.POST['email']
		otp=request.POST['otp']
		otp1=request.POST['otp1']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		newuser=Users.objects.get(email=email)
		print("***",email)
		if newuser:
			if otp1==otp and password==cpassword:
				newuser.password=password
				newuser.save()
				message="password reset succesfully"
				return render(request,'login.html',{'msg':message})
			else:
				message="invalid otp or password"
				return render(request,'reset_password.html',{'msg':message})
	except:
		message="invalid Email"
		return render(request,'login.html',{'msg':message})
    
def Logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,"app/signup.html")
    else:
        return render(request,"app/signup.html")
    
def Testimonial(request):
    return render(request,"app/testimonial.html")

def Treatment(request):
    return render(request,"app/treatment.html")

def Doctor(request):
    return render(request,"app/doctor.html")

def Contactus(request):
    if request.POST:
        vrf_email = Users.objects.get(email=request.POST['email'])
        # print(Users.objects.get(email=request.POST['email']))
        fullname=request.POST['name']
        email=request.POST['email']
        phone_number=request.POST['number']
        message=request.POST['message']
        # chck git
        # check second comment
        if (email):
            Contact_us.objects.create(fullname=fullname,email=email,contact_no=phone_number,message=message)
            return render(request,"app/contact.html")
    else:
         return render(request, 'app/contact.html')
    
def About(request):
     return render(request,"app/about.html")