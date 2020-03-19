from django import forms

from .models import Ingredients

class PostForm(forms.ModelForm):

    class Meta:
        model = Ingredients
        fields = ("product_name","company_name","quantity_per_unit","quantity","description","type_of_product")