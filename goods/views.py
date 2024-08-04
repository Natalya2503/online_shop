from django.shortcuts import render, get_object_or_404


from goods.models import Yarn, YarnSubCategories, YarnCategories

# выбираю каждый первый товар из всех категорий и подкатегорий

def first_product(request):
    categories = YarnCategories.objects.prefetch_related('subcategories__products').all()
    first_products = []

    for category in categories:
        for subcategory in category.subcategories.all():
            first_product = subcategory.products.first()
            if first_product:
                first_products.append(first_product)
    context = {
        'title':'Пряжа',
        'first_products': first_products
    }
    return render(request, 'goods/yarn.html', context)

# выбираю первый товар из всех подкатегорий определенной категории

def first_category(request, category_id):
    category = get_object_or_404(YarnCategories, id=category_id)
    subcategories = category.subcategories.all()
    first_products = []
    for subcategory in subcategories:
        first_product = subcategory.products.first()
        if first_product:
            first_products.append(first_product)
    context = {
        'title':'Категория пряжи',
        'category': category,
        'first_products': first_products
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




































# def product(request, product_id):
#     product = Products.objects.get(id=product_id)
#     context = {
#         'title': 'Товар',
#         'product': product
#     }
#     return render(request, 'goods/product.html', context)
