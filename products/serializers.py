from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Product
        fields = ['uuid', 'name', 'code', 'description']
