from market.models import Product
from django.shortcuts import redirect


def delete(request, pk):
    guest = Product.objects.get(pk=pk)
    guest.delete()
    return redirect('main')
