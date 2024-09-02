from django.urls import path
from payment import views


app_name = 'payment'

urlpatterns = [
    path('start_payment/<int:order_id>/', views.start_payment, name='start_payment'),
    path('success_payment/', views.success_payment, name='success_payment'),
   
]