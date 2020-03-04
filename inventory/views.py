from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Ingredients
from .serializer import IngredientsSerializers
from django_filters.rest_framework import  DjangoFilterBackend
from django.http import HttpResponse
from django.views.generic import ListView
from .tables import IngredientTable
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
# Create your views here.

class IngredientList(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializers

def homeView(request):
    return HttpResponse("You're looking at question")

def InventoryListView(request):
    

    table = IngredientTable(Ingredients.objects.all())
    RequestConfig(request, paginate={"per_page": 10}).configure(table)

    return render(request, "ingredients.html", {"table": table})