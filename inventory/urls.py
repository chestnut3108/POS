from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IngredientList, InventoryListView,save,contact
from pos.settings import API_PREFIX
from django.conf.urls  import url

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'add', IngredientList)

urlpatterns = [url(r'save/',save),
            path(r'contact/', contact, name='contact'),
            path(r'store/', InventoryListView, name='store') ]
             
urlpatterns+=  router.urls
