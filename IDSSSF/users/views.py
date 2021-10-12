from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def registrationPage(request):
    content = {}
    return render(request,"users/reg.html",content)

def loginPage(request):
    content = {}
    return render(request,"users/login.html",content)

