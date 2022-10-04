from django.urls import path

from market.views.base import index_view
from market.views.product_view import product_view
from market.views.add_view import add_view
from market.views.edit_view import edit
from market.views.delete import delete
from market.views.search_view import search_view

urlpatterns = [
    path('', index_view, name='main'),
    path('products/<int:pk>', product_view, name='product'),
    path('add/', add_view, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('search/', search_view, name='search')

]
