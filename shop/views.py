
from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Category, Product, Article
from shop.serializer import CategorySerializer, ProductSerializer, ArticleSerializer

class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        # Filtrer seulement les objets actif
        return Category.objects.filter(active=True)
        # Filtrer les articles par leur ID


class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Product.objects.filter(active=True)
        # Filtre pour afficher les category par leur ID
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset=Article.objects.filter(active=True)
        return queryset
