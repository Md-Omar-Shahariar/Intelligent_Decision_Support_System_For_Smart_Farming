from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminCreationForm

@login_required()
def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')
    return render(req, 'register.html', {'form': form})

def profile(request):
    content = {}
    return render(request, 'profile.html', content)

def homepage(request):
    content = {}
    return render(request, 'homepage.html', content)