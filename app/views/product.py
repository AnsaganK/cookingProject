from django.db.models import Q, Value, Count, Sum
from django.shortcuts import render, get_object_or_404

from app.models import Product, Recipe


def product_list(request):
    products = Product.objects.all()
    return render(request, 'app/product/list.html', {
        'products': products
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/product/detail.html', {
        'product': product
    })


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recipes = Recipe.objects.filter(
        ~Q(ingredients__product=product) | (Q(ingredients__product=product) & Q(ingredients__weight__lt=10))
    ).annotate(
        product_weight=Sum('ingredients__weight', default=0)
    )
    return render(request, 'app/product/recipes_without.html', {
        'product': product,
        'recipes': recipes
    })
