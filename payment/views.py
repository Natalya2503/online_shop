from django.urls import reverse
import uuid
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from yookassa import Configuration, Payment
from django.contrib.auth.decorators import login_required

from orders.models import Order

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

@login_required
def start_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    try:
        total_amount = order.total_amount
        payment = Payment.create({
            'amount':{
                'value': str(total_amount),
                'currency': 'RUB'
            },
            'confirmation': {
                'type': 'redirect',
                'return_url': request.build_absolute_uri(reverse('payment:success_payment'))
            },
            'capture': True,
            'description': f'Order #{order.id}'
            }, str(uuid.uuid4())
        )
        order.payment_id = payment.id
        order.save()
        return redirect(payment.confirmation.confirmation_url)
    except Exception as e:
        return HttpResponse(f'Произошла ошибка при создании оплаты: {str(e)}')

@login_required
def success_payment(request):
    context = {
        'title': 'Успешная оплата'
    }
    return render(request, 'payment/success_payment.html', context)
