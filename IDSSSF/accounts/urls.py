from django.urls import path
from . import views


urlpatterns = [
    path("registration", views.register, name= "registration"),
    path("accounts/profile/", views.profile, name= "profile"),
    path("homepage/", views.homepage, name= "home"),
    path("login", views.loginPage, name= "login"),
    
    #path("login", views.loginPage, name= "login")

]
