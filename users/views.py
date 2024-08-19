from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import  reverse_lazy, reverse
from django.db.models import Prefetch
from carts.models import Cart
from orders.models import Order, OrderItem



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
# ----------------------------------------
    
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

# -------------------------------------------
    
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}

    def get_success_url(self):
        return reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('products', 'yarn', 'adaptations')
            )
        ).order_by('-id')
        return context

# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
           
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = ProfileForm(instance=request.user)

#     # orders = Order.objects.filter(user=request.user).prefetch_related(
#     #             Prefetch(
#     #                 "orderitem_set",
#     #                 queryset=OrderItem.objects.select_related("product"),
#     #             )
#     #         ).order_by("-id")
        

#     context = {
#         'title': 'Home - Кабинет',
#         'form': form,
#         # 'orders': orders,
#     }
#     return render(request, 'users/profile.html', context)
    








