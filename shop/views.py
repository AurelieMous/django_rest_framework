from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializer import CategorySerializer

class CategoryAPIViews(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProductAPIViews(APIView):
    def get(self, *arg, **kwargs):
        identifiant =