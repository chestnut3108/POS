from django.db import models

Ingredients_choices = (("s","sauces"), ("f","frozen"))
# Create your models here.
class Ingredients(models.Model):
    product_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    quantity_per_unit = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    type_of_product = models.CharField(max_length=128, choices=Ingredients_choices)
    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __unicode__(self):
        return self.product_name
    