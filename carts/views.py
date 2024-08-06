from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404, JsonResponse
from goods.models import Products, Yarn, Adaptations
from carts.models import Cart
from carts.utils import get_user_carts






def cart_add(request):
    product = None
    product_classes = [Products, Yarn, Adaptations]
    product_field = None
    product_id = request.POST.get('product_id')

    for cls in product_classes:
        if cls.objects.filter(id=product_id).exists():
            product = get_object_or_404(cls, id=product_id)
            product_field = cls._meta.model_name
            break
    else:
        raise Http404("Product not found")
    
  

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            defaults={'quantity': 1}, user=request.user, **{product_field: product}
        )
        if not created:
            cart.quantity += 1
            cart.save()
    
    user_cart = get_user_carts(request)
    
    cart_items_html = render_to_string('goods/product.html', {'carts': user_cart}, request=request)
    
    response_data = {
        'cart_items_html': cart_items_html
    }
    
    return JsonResponse(response_data)




    


def cart_remove(request):
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    context = {'carts': user_cart}

    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', context, request=request

    )

    response_data = {
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity
    }
    return JsonResponse(response_data)
    


def cart_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string('carts/includes/included_cart.html', {'carts':cart}, request=request)
     
    response_data = {
        'cart_items_html': cart_items_html,
        'quantity': updated_quantity
    }
    return JsonResponse(response_data)

def user_cart(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'carts/cart.html', context)
