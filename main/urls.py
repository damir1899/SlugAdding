from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from .views import IndexView, ProductDetailView
from .api import CategoryViewSet, ProductViewSet


urlpatterns = [
    path('', IndexView, name='index'),
    path('<slug:slug>/', ProductDetailView, name='product_detail'),
]

urlpatterns += static(settings.STATIC_URL, 
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)


router = routers.DefaultRouter()

router.register('api.categories', CategoryViewSet, basename='categories')
router.register('api.products', ProductViewSet, basename='products')
urlpatterns += router.urls