from django.shortcuts import render, redirect

from market.forms import SearchForm, AddEditForm
from market.models import Product, CATEGORIES


def index_view(request):
    search_form = SearchForm()
    products = Product.objects.filter(qty__gte=0)
    context = {
        'products': products,
        'categories': CATEGORIES,
        'search_form': search_form
    }
    return render(request, 'main.html', context)


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = AddEditForm()
        return render(request, 'add_product.html', context={'form': form,
                                                            'categories': CATEGORIES
                                                            })
    elif request.method == 'POST':
        form = AddEditForm(data=request.POST)
        if form.is_valid():
            article = Product.objects.create(description=form.cleaned_data['description'],
                                             category=form.cleaned_data["category"], image=form.cleaned_data['image'],
                                             name=form.cleaned_data['name'], qty=form.cleaned_data['qty'],
                                             cost=form.cleaned_data['cost'], )
            return redirect('main')
        else:
            return render(request, 'add_product.html', context={'form': form,
                                                                'categories': CATEGORIES})


def edit(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        form = AddEditForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'image': product.image,
            'qty': product.qty,
            'cost': product.cost

        })
        return render(request, 'edit.html', context={'form': form, 'product': product, 'categories': CATEGORIES})
    elif request.method == 'POST':
        form = AddEditForm(data=request.POST)
        if form.is_valid():
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data["category"]
            product.name = form.cleaned_data['name']
            product.image = form.cleaned_data['image']
            product.qty = form.cleaned_data['qty']
            product.cost = form.cleaned_data['cost']
            product.save()
            return redirect('main')
        else:
            return render(request, 'edit.html', context={'form': form, 'product': product})


def delete(request, pk):
    guest = Product.objects.get(pk=pk)
    guest.delete()
    return redirect('main')
