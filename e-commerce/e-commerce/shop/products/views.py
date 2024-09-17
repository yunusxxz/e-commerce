from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.
def index(request):
    items = {
        "products": Product.objects.all()
    }
    return render(request, 'products_index.html', items)


def detail(request, product_id):
    item = {
        "product": get_object_or_404(Product, pk=product_id)
    }
    return render(request, 'products_detail.html', item)
