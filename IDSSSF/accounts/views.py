from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
# from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminCreationForm


def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
    return render(req, 'signup/signup.html', {'form': form})

def profile(request):
    content = {}
    return render(request, 'profile.html', content)

@login_required()
def homepage(request):
    current_user = request.user
    name = current_user.first_name
    content = {'name':name}
    return render(request, 'homepage.html', content)


def loginPage(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = authenticate(request, phone=phone,password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')

    content = {}
    return render(request, 'registration/login.html', content)