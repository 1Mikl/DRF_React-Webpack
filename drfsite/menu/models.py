from django.db import models


class Recipes(models.Model):

    CATEGORY_CHOICES = (
        ("Завтраки", "Завтраки"),
        ("Супы", "Супы"),
        ("Салаты", "Салаты"),
        ("Горячие блюда", "Горячие блюда"),
    )

    categoryType = models.CharField(max_length=40, choices=CATEGORY_CHOICES, verbose_name='Категория')
    name = models.CharField(max_length=257, verbose_name='Наименование')
    recipe = models.TextField(verbose_name="Peцепт")

    def __str__(self):
        return f'{self.name} | {self.categoryType}'
