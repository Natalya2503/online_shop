from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm
from django.urls import  reverse_lazy
from carts.models import Cart


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}
   
    def get_success_url(self):
        return reverse_lazy('main:index')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()

        if user:
            auth.login(self.request, user)
        
            if session_key:
              Cart.objects.filter(session_key = session_key).update(user=user)
              return HttpResponseRedirect(self.get_success_url())
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
class RegisterUser(CreateView):
    form_class =  RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {'title':'Регистрация'}
   
    def get_success_url(self):
        return reverse_lazy('user:login')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)
            return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    








