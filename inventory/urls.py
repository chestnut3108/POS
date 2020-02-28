from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IngredientList
from pos.settings import API_PREFIX


router = routers.DefaultRouter()
router.register(API_PREFIX+r'/ingredients', IngredientList)


urlpatterns = router.urls

