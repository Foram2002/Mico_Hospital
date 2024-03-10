from django.urls import path,include
from django.contrib import admin

from myapp import views
from .views import *

urlpatterns = [
   
    path("",views.Index,name="index"),
    path("signup/",views.Signup,name="signup"),
    path("login/",views.Login,name="login"),
    path("forgot_password/",views.Forgot_password,name="forgot_password"),
    path("reset_password/",views.Reset_password,name="reset_password"),
    path('send-otp/', views.send_otp, name='send-otp'),
    path("logout/",views.Logout,name="logout"),
    path("treatment/",views.Treatment,name="treatment"),
    path("testimonial/",views.Testimonial,name="testimonial"),
    path("doctor/",views.Doctor,name="doctor"),
    path("contact/",views.Contactus,name="contact"),
    path("about/",views.About,name="about")

    



    



]
