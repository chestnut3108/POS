import django_tables2 as tables
from .models import Ingredients

class IngredientTable(tables.Table):
    class Meta:
        model = Ingredients
        template_name = "django_tables2/semantic.html"
        exclude = ("friendly", )
        fields = ("id","product_name","company_name","quantity_per_unit","quantity","description","type_of_product")