from market.forms import AddEditForm
from market.models import Product
from django.shortcuts import render, redirect


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
        return render(request, 'edit.html', context={'form': form, 'product': product})
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
