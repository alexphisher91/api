from dataclasses import fields
from pyexpat import model
from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'code', 'description',]
