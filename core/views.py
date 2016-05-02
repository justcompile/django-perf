from django.shortcuts import get_object_or_404, render
from core.models import Category, Product, Order, Store

def index(request):
    ctx = {
        'products': Product.objects.all()[:200]
    }
    return render(request, 'core/index.html', ctx)

def store(request, store_id):
    store_obj = get_object_or_404(Store, id=store_id)

    products = Product.objects.filter(store=store_obj)
    if request.GET.get('category'):
        products = products.filter(categories__name=request.GET.get('category'))

    ctx = {
        'store': store_obj,
        'categories': Category.objects.filter(store=store_obj),
        'products': products,
        'filtered_category': request.GET.get('category', 'All')
    }

    return render(request, 'core/store.html', ctx)


def orders(request, store_id=None):
    qs = Order.objects.all()
    if store_id:
        qs = qs.filter(store__id=store_id)

    ctx = {
        'orders': qs
    }

    return render(request, 'core/orders.html', ctx)
