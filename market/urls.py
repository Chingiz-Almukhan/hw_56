from django.urls import path

from market.views import index_view, product_view, add_view, edit, delete

urlpatterns = [
    path('', index_view, name='main'),
    path('products/<int:pk>', product_view, name='product'),
    path('add/', add_view, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    # path('search/', search_view, name='search')

]
