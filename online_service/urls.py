from django.urls import path, re_path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet


app_name = 'online_service'

router = routers.DefaultRouter()


router.register(r'Product-ViewSet', ProductViewSet, basename='product-viewset')
router.register(r'Category-ViewSet', CategoryViewSet, basename='category-viewset')


urlpatterns = [
    path('', include(router.urls)),

]








