from django.shortcuts import render

def catalog(request):
    content = {
        'title':"Home - Каталог",
        'goods':'my'
    }
    return render(request, 'goods/catalog.html')

def product(request):
    return render(request, 'goods/product.html')
