from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Ingredients
from .serializer import IngredientsSerializers
from django_filters.rest_framework import  DjangoFilterBackend
# Create your views here.

class IngredientList(generics.ListCreateAPIView):
    model = Ingredients
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('product_name')