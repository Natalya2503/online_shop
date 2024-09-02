from django.shortcuts import render, redirect
from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem



@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            user = request.user
            cart_items = Cart.objects.filter(user=user)
            if not cart_items.exists():
                form.add_error(None, 'Cart is empty')
                return render(request, 'orders/order_create.html', {'form': form})
            try:
                with transaction.atomic():
                        order = Order.objects.create(
                            user = user,
                            phone_number = form.cleaned_data['phone_number'],
                            delivery_address = form.cleaned_data['delivery_address']
                        )
                        for cart_item in cart_items:
                            if cart_item.products:
                              product = cart_item.products
                              stock_quantity = product.quantity
                              item_name = product.name
                            elif cart_item.yarn:
                              product = cart_item.yarn
                              stock_quantity = product.quantity
                              item_name = product.name
                            elif cart_item.adaptations:
                              product = cart_item.adaptations
                              stock_quantity = product.quantity
                              item_name = product.name
                            else:
                              raise ValidationError('Item not available in cart.')

                            if stock_quantity < cart_item.quantity:
                              raise ValidationError(f'Недостаточное количество {item_name} на складе. В наличии - {stock_quantity}')

                            product.quantity -= cart_item.quantity
                            product.save()
          
                           
                            OrderItem.objects.create(
                             order=order,
                             products=cart_item.products,
                             yarn=cart_item.yarn,
                             adaptations=cart_item.adaptations,
                             price=cart_item.products.price if cart_item.products else 0,
                             quantity=cart_item.quantity,
                        )
                            
                         
                        cart_items.delete()
                        return redirect('payment:start_payment', order_id=order.id)
            except Exception as e:
                form.add_error(None, str(e))        
    else:
        initial = {
            'username': request.user.username,
            'last_name': request.user.last_name
        } 
        form = CreateOrderForm(initial=initial) 
    context = {
        'title': 'Оформление заказа',
        'form': form
    }      
    return render(request, 'orders/order_create.html', context)


























# import logging
# logger = logging.getLogger(__name__)
# @login_required
# def create_order(request):

#     logger.debug('Это сообщение отладки')

#     logger.info('Информационное сообщение')

#     logger.error('Сообщение об ошибке')

#     context = {

#         'title': 'Оформление заказа',

#         'form': CreateOrderForm(),  

#         'order': True,

#     }

#     if request.method == 'POST':

#         form = CreateOrderForm(data=request.POST)

#         if form.is_valid():

#             try:

#                 with transaction.atomic():

#                     user = request.user

#                     cart_items = Cart.objects.filter(user=user)

#                     if cart_items.exists():

#                         order = Order.objects.create(

#                             user=user,

#                             phone_number=form.cleaned_data['phone_number'],

#                             requires_delivery=form.cleaned_data['requires_delivery'] == '1',

#                             delivery_address=form.cleaned_data['delivery_address'],

#                             payment_on_get=form.cleaned_data['payment_on_get'] == '1'

#                         )

#                         for cart_item in cart_items:

#                             product = cart_item.products

#                             yarn = cart_item.yarn

#                             adaptation = cart_item.adaptations

#                             price = cart_item.products_price()

#                             quantity = cart_item.quantity

#                             if product is not None:

#                                 if product.quantity < quantity:

#                                     logger.warning(f'Недостаточное количество товара. Продукт: {product.name}, Количество: {product.quantity}, Товар в корзине: {quantity}')

#                                     raise ValidationError(f'Недостаточное количество товара на складе. В наличии - {product.quantity}')

#                             elif yarn is not None:

#                                 if yarn.quantity < quantity:

#                                     logger.warning(f'Недостаточное количество пряжи. Пряжа: {yarn.name}, Количество: {yarn.quantity}, Товар в корзине: {quantity}')

#                                     raise ValidationError(f'Недостаточное количество пряжи на складе. В наличии - {yarn.quantity}')

#                             elif adaptation is not None:

#                                 if adaptation.quantity < quantity:

#                                     logger.warning(f'Недостаточное количество адаптации. Адаптация: {adaptation.name}, Количество: {adaptation.quantity}, Товар в корзине: {quantity}')

#                                     raise ValidationError(f'Недостаточное количество адаптации на складе. В наличии - {adaptation.quantity}')

#                             else:

#                                 logger.warning('Товар отсутствует на складе.')

#                                 raise ValidationError('Товар отсутствует в наличии.')

#                             OrderItem.objects.create(

#                                 order=order,

#                                 products=product if product else None,

#                                 yarn=yarn if yarn else None,

#                                 adaptations=adaptation if adaptation else None,

#                                 price=price,

#                                 quantity=quantity,

#                             )

#                             if product:

#                                 product.quantity -= quantity

#                                 product.save()

#                             if yarn:

#                                 yarn.quantity -= quantity

#                                 yarn.save()

#                             if adaptation:

#                                 adaptation.quantity -= quantity

#                                 adaptation.save()

#                         messages.success(request, 'Заказ успешно создан.')

#                         return redirect('main:index')

#             except ValidationError as e:

#                 form.add_error(None, e)

#                 logger.error('Ошибка при обработке заказа: %s', str(e))

#         context['form'] = form

#     return render(request, 'orders/order_create.html', context)









