from django.contrib import admin
from django.urls import path, include

from shop.views import CategoryAPIViews, ProductAPIViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIViews.as_view()),
    path('api/product', ProductAPIViews.as_view())
]
