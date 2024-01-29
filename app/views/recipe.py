from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect, reverse

from app.models import Recipe, Product, RecipeIngredient


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/recipe/list.html', {
        'recipes': recipes
    })


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.all()
    products = Product.objects.all()
    return render(request, 'app/recipe/detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'products': products
    })


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product_ids = recipe.ingredients.values_list('product_id', flat=True)
    products = Product.objects.filter(id__in=product_ids)
    products.update(usage_quantity=F('usage_quantity') + 1)
    return redirect(reverse('app:recipe_list'))


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe')
    product_id = request.GET.get('product')
    weight = request.GET.get('weight')

    ingredient = RecipeIngredient.objects.get_or_create(
        recipe_id=recipe_id,
        product_id=product_id,
    )
    ingredient[0].weight = weight
    ingredient = ingredient[0]
    ingredient.save()

    return redirect(reverse('app:recipe_detail', args=[recipe_id]))
