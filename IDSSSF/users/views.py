from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm, UserProfileForm
# Create your views here.

def registrationPage(request):
    form = CreateUserForm()
    userform = UserProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        userform = UserProfileForm(request.POST)
        if form.is_valid() and userform.is_valid():
            user = form.save()
            profile = userform.save(commit=False)
            profile.user = user
            profile.save()

    
    content = {'form' : form,'profile_form' : userform}
    return render(request,"users/reg.html",content)

def loginPage(request):
    content = {}
    return render(request,"users/login.html",content)

