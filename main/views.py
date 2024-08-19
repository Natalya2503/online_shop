from django.shortcuts import render


def index(request):
 
    context={
        'title': 'Главная'
       
    }
    return render(request, 'main/index.html', context)

def about(request):
    context={
        'title': 'О магазине'
    }
    return render(request, 'main/about.html', context)
