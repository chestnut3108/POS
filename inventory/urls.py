from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IngredientList,homeView, InventoryListView
from pos.settings import API_PREFIX
from django.conf.urls  import url

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'i', IngredientList)

urlpatterns = [url('home/', homeView),
                url('list/', InventoryListView)]
urlpatterns+=  router.urls
