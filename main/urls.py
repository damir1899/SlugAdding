from django.urls import path
from .views import IndexView, ProductDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', IndexView, name='index'),
    path('<slug:slug>/', ProductDetailView, name='product_detail'),
]

urlpatterns += static(settings.STATIC_URL, 
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)