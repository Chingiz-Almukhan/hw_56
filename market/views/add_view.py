from market.forms import AddEditForm
from market.models import Product
from django.shortcuts import render, redirect


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = AddEditForm()
        return render(request, 'add_product.html', context={'form': form})
    elif request.method == 'POST':
        form = AddEditForm(data=request.POST)
        if form.is_valid():
            article = Product.objects.create(description=form.cleaned_data['description'],
                                             category=form.cleaned_data["category"], image=form.cleaned_data['image'],
                                             name=form.cleaned_data['name'], qty=form.cleaned_data['qty'],
                                             cost=form.cleaned_data['cost'], )
            return redirect('main')
        else:
            return render(request, 'add_product.html', context={'form': form})
