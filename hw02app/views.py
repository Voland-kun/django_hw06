from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .models import Customer, Order, Product
from .forms import ProductForm


def index(request):
    return render(request, 'hw02app/index.html')


def ordered_products(request, customer_id, days):
    customer = Customer.objects.get(pk=customer_id)
    current_date = timezone.now()
    start_date = current_date - timedelta(days=days)
    products_list = Product.objects.filter(order__customer=customer,
                                           order__order_date__gte=start_date,
                                           order__order_date__lte=current_date).distinct().values('name')

    return render(request, 'hw02app/ordered_items.html', {'products_list': products_list})


def customer_name(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "hw02app/customer.html", {"customer": customer})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'hw02app/product_create.html', {'form': form})


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_page', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'hw02app/product_edit.html', {'form': form})


def products_list(request):
    products = Product.objects.all()
    return render(request, "hw02app/products.html", {"products": products})


def product_page(request, product_id):
    product_ = get_object_or_404(Product, pk=product_id)
    return render(request, "hw02app/product.html", {"product": product_})