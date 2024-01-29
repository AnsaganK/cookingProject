from django.db import models
from django.shortcuts import reverse

from app.models.base import BaseModel
from .product import Product


class Recipe(BaseModel):
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:recipe_detail', args=[str(self.id)])


class RecipeIngredient(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients', verbose_name='Рецепт')
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='ingredients', verbose_name='Продукт'
    )
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецептов'

    def __str__(self):
        return f'{self.recipe.name} - {self.product.name if self.product else ""} - {self.weight}гр.'
