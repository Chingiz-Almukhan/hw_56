from market.models import Product, CATEGORIES
from django.shortcuts import render


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_view.html', context={
        'product': product,
        'categories': CATEGORIES
    })
