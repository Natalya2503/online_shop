from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm
from django.urls import  reverse_lazy


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}
   
    def get_success_url(self):
        return reverse_lazy('main:index')

    
class RegisterUser(CreateView):
    form_class =  RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {'title':'Регистрация'}
   
    def get_success_url(self):
        return reverse_lazy('user:login')








