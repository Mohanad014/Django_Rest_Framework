from rest_framework import serializers
from .models import *

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

