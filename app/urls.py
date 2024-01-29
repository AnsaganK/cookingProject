from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.page.home, name='home'),

    # Recipe Url
    path('recipe', views.recipe.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>', views.recipe.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/cook_recipe', views.recipe.cook_recipe, name='cook_recipe'),
    path('recipe/add-product', views.recipe.add_product_to_recipe, name='add_product_to_recipe'),

    # Product Url
    path('product', views.product.product_list, name='product_list'),
    path('product/<int:product_id>', views.product.product_detail, name='product_detail'),
    path(
        'product/<int:product_id>/recipes_without_product', views.product.show_recipes_without_product,
        name='show_recipes_without_product'
    ),
]
