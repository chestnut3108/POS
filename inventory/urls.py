from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IngredientList, InventoryListView,save,contact,inventory_new
from pos.settings import API_PREFIX
from django.conf.urls  import url

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'inventory/show', IngredientList)

urlpatterns = [url(r'save/',save),
            path(r'contact/', contact, name='contact'),
            path(r'inventory/', InventoryListView, name='inventory'),
            path('inventory/new/', inventory_new, name='inventory_new'), ]
             
urlpatterns+=  router.urls
