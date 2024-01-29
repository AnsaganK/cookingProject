import datetime

from django import template

from app.models import RecipeIngredient

register = template.Library()


@register.filter(name='get_product_weight_in_recipe')
def get_product_weight_in_recipe(recipe, product):
    try:
        weight = recipe.ingredients.get(product=product).weight
    except RecipeIngredient.DoesNotExist:
        weight = 0
    return weight
