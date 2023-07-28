from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    images = Image.objects.all()
    categories = Category.objects.all().order_by("-id")
    
    
    context = {'products': products, 'images': images, "categories": categories}
    
    return render(request, 'main/index.html', context)

def show_category(request, category_slug):
    products = Product.objects.filter(category=Category.objects.get(slug=category_slug))
    images = Image.objects.all()
    categories = Category.objects.all().order_by("-id")

    context = {'products': products, 'images': images, "categories": categories}
    return render(request, 'main/index.html', context)

def show_product(request, category_slug, product_slug):
    product = Product.objects.get(slug=product_slug)
    category = Category.objects.get(slug=category_slug)

    return render(request, 'main/product.html', {'product': product, "category": category})

def img_show(request):
    return render(request, 'main/img_show.html')