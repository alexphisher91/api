from rest_framework import viewsets, views
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response


class ProductView(views.APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
