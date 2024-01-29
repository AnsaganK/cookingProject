from django.contrib import admin

from app.models.product import Product
from app.models.recipe import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [RecipeIngredientInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'usage_quantity']
    list_editable = ['name', 'usage_quantity']


@admin.register(RecipeIngredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'product', 'weight']
