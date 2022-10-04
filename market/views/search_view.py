from django.shortcuts import render
from market.forms import SearchForm
from market.models import Product, CATEGORIES


def search_view(request):
    form = SearchForm(data=request.GET)
    if form.is_valid():
        name = form.cleaned_data["search"]
        try:
            products = Product.objects.get(name=name)
        except Exception:
            context = {
                'error': 'Продукт с таким названием не найден',
                'search_form': form,
            }
            return render(request, 'main.html', context)
        context = {
            'product': products,
            'search_form': form,
            'categories': CATEGORIES
        }
        return render(request, 'main.html', context)
    else:
        products = Product.objects.filter(qty__gt=0)
        context = {
            'products': products,
            'search_form': form
        }
        return render(request, 'main.html', context)
