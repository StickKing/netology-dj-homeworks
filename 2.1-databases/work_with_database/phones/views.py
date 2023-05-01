from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_name = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_name == 'name':
        context = {'phones': sorted(phones, key=lambda phone: phone.name)}
    elif sort_name == 'min_price':
        context = {'phones': sorted(phones, key=lambda phone: phone.price)}
    elif sort_name == 'max_price':
        context = {'phones': sorted(phones, key=lambda phone: phone.price, 
                                    reverse=True)}
    else:  
        context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
