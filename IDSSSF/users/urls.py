from django.urls import path
from . import views


urlpatterns = [
    path("reg/", views.registrationPage, name= "reg"),
    path("login/", views.loginPage, name= "login")

]
