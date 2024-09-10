from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q



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
    
    first_products = []

   
           
    category = get_object_or_404(YarnCategories, id=category_id)
    subcategories = category.subcategories.all()
       
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
    page = request.GET.get('page', 1)
    adapts = Adaptations.objects.all()
  
    paginator = Paginator(adapts, 4)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Категории инструментов',
        'adapts': current_page
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
    page = request.GET.get('page', 1)
  
    adapts = Adaptations.objects.filter(category__id=cat_id)
    
    paginator = Paginator(adapts, 4)
    current_page = paginator.page(int(page))
    context = {
         'title': 'Категории инструментов',
         'adapts': current_page
        
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

# --------------------search-------------------------------

def q_searсh(query):
    keywords = [word for word in query.split() if len(word)>0]
    
    yarn_q_objects =Q()
    adaptations_q_objects = Q()
    products_q_objects = Q()

    for token in keywords:
        yarn_q_objects |= Q(description__icontains=token)
        adaptations_q_objects |= Q(name__icontains=token) | Q(description__icontains=token)
        products_q_objects |= Q(name__icontains=token) | Q(description__icontains=token)

    yarn_results = Yarn.objects.filter(yarn_q_objects)
    adaptations_results = Adaptations.objects.filter(adaptations_q_objects)
    products_results = Products.objects.filter(products_q_objects)

    return {
        'yarn_results': yarn_results,
        'adaptations_results': adaptations_results,
        'products_results': products_results
    }
                
def search(request):
    query = request.GET.get('q', '') 
    results = q_searсh(query) if query else {}

    context = {
        'title': 'Поиск',
        'query': query,
        'results': results
    }
    return render(request, 'goods/search.html', context)


   
   




        
     

        
    

 
      




































