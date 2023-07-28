from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<slug:category_slug>', show_category, name='show_category'),
    path('<slug:category_slug>/<slug:product_slug>', show_product, name='show_product'),
]
