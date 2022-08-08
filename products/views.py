from rest_framework import viewsets, views
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import generics


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

