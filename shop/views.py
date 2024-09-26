from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category, Product
from shop.serializer import CategorySerializer, ProductSerializer

class CategoryAPIViews(APIView):
    def get(self, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductAPIViews(APIView):
    def get(self, *arg, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
