from market.forms import SearchForm
from market.models import Product, CATEGORIES
from django.shortcuts import render


def index_view(request):
    search_form = SearchForm()
    products = Product.objects.filter(qty__gt=0).order_by('category', 'name')
    context = {
        'products': products,
        'categories': CATEGORIES,
        'search_form': search_form
    }
    return render(request, 'main.html', context)
