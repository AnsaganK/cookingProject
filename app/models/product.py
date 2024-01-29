from django.db import models

from app.models.base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=512)
    usage_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
