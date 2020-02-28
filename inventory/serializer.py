from rest_framework import serializers
from .models  import Ingredients

class IngredientsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'