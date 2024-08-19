from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from goods.models import Yarn,YarnCategories, Adaptations, Products


# --------------------yarn--------------------------------

# выбираю каждый первый товар из всех категорий и подкатегорий

def first_product(request):
    page = request.GET.get('page', 1)

    categories = YarnCategories.objects.prefetch_related('subcategories__products').all()
    first_products = []

    for category in categories:
        for subcategory in category.subcategories.all():
            first_product = subcategory.products.first()
            if first_product:
                first_products.append(first_product)
    
    paginator = Paginator(first_products, 4)
   
    current_page = paginator.page(int(page))
    


    context = {
        'title':'Пряжа',
        'first_products': current_page
    }
    return render(request, 'goods/yarn.html', context)

# выбираю первый товар из всех подкатегорий определенной категории

def first_category(request, category_id):
    
    page = request.GET.get('page', 1)


    category = get_object_or_404(YarnCategories, id=category_id)
    subcategories = category.subcategories.all()
    first_products = []
    for subcategory in subcategories:
        first_product = subcategory.products.first()
        if first_product:
            first_products.append(first_product)

    paginator = Paginator(first_products, 4)
    current_page = paginator.page(int(page))
    



    context = {
        'title':'Категория пряжи',
        'category': category,
        'first_products': current_page,
        # 'id_url': category_id
    }
    return render(request, 'goods/yarn_category.html', context)



def product_details(request, product_id):
    product = get_object_or_404(Yarn, id=product_id)
    subcategory_product = Yarn.objects.filter(subcategory = product.subcategory)
    context = {
        'title':'Категория пряжи',
        'product': product,
        'subcategory_product':subcategory_product
    }
    return render(request, 'goods/product.html', context)

# ------------------adaptations-----------------------------
def catalog_adapt(request):
    adapts = Adaptations.objects.all()
    context = {
        'title': 'Категории инструментов',
        'adapts': adapts
    }
    return render(request, 'goods/adapt.html', context)

    

def adapt_detail(request, adapt_id):
    adapt = Adaptations.objects.get(id=adapt_id)
    context = {
        'title': 'Инструмент для вязания',
        'adapt': adapt
    }
    return render(request, 'goods/adapt_detail.html', context)
    

def category_adapt(request, cat_id):
     adapts = Adaptations.objects.filter(category__id=cat_id)
     context = {
         'title': 'Категории инструментов',
         'adapts': adapts,
        
     }
     return render(request, 'goods/cat_adapt.html', context)


# -------------------products----------------------

def products_catalog(request):
    page = request.GET.get('page', 1)
    products = Products.objects.all()

    paginator = Paginator(products, 4)
    current_page = paginator.page(int(page))

    context = {
        'title':'Каталог товаров',
        'products': current_page
    }
    return render(request, 'goods/cat_products.html', context)

def product_sample(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'title':'Аксессуары',
        'product': product
    }
    return render(request, 'goods/product_sample.html', context)


































# def product(request, product_id):
#     product = Products.objects.get(id=product_id)
#     context = {
#         'title': 'Товар',
#         'product': product
#     }
#     return render(request, 'goods/product.html', context)
