from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from yookassa import Configuration, Payment
from orders.models import Order, OrderItem
from django.db.models import Prefetch
from shop import settings
import json

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

def create_payment(order_id):
    order = get_object_or_404(Order, id=order_id)
    amount = sum(item.price * item.quantity for item in order.orderitem_set.all())
    payment = Payment.create({
        "amount": {
            "value": str(amount),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"http://localhost:8000/orders/{order_id}/success"
        },
        "capture": True,
        "description": f"Order {order_id}",
        "metadata": {"order_id": order_id}
    })
    return payment

def order_create_view(request, order_id):
    payment = create_payment(order_id)
    return redirect(payment.confirmation.confirmation_url)

def payment_success_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "Оплачено"
    order.save()
    return render(request, 'payment_success.html', {'order': order})

def yookassa_webhook_view(request):
    event_json = json.loads(request.body)
    if event_json.get("event") == "payment.succeeded":
        payment_id = event_json['object']['id']
        order_id = event_json['object']['metadata']['order_id']
        order = get_object_or_404(Order, id=order_id)
        order.status = "Оплачено"
        order.save()
    return JsonResponse({"status": "ok"})


def payment(request):
    context = {
        'title': 'Оплата'
    }
    return render(request, 'payment/create_payment.html', context)

