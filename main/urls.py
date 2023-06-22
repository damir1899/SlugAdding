from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from .views import IndexView, ProductDetailView
from .api import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register('api.categories', CategoryViewSet, basename='categories')
router.register('api.products', ProductViewSet, basename='products')

urlpatterns = [
    path('', IndexView, name='index'),
    path('<slug:slug>/', ProductDetailView, name='product_detail'),
]

urlpatterns += router.urls