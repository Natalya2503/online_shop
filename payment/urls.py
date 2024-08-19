from django.urls import path
from payment import views


app_name = 'payment'

urlpatterns = [
    path('orders/<int:order_id>/pay/', views.order_create_view, name='order_create_view'),
    path('orders/<int:order_id>/success/', views.payment_success_view, name='payment_success'),
    path('webhook/yookassa/', views.yookassa_webhook_view, name='yookassa_webhook'),
    path('payment/', views.payment, name='create_payment')

]

