from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
# Create your views here.

def registrationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    
    content = {'form' : form}
    return render(request,"users/reg.html",content)

def loginPage(request):
    content = {}
    return render(request,"users/login.html",content)

