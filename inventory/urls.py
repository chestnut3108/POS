from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IngredientList, InventoryListView,save,contact
from pos.settings import API_PREFIX
from django.conf.urls  import url

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'add', IngredientList)

urlpatterns = [url(r'', InventoryListView),
             url('save/',save),
            path('contact/', contact, name='contact'),]
urlpatterns+=  router.urls
