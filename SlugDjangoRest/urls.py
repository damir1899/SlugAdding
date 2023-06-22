from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main.api import CategoryViewSet, ProductViewSet


schema_view = get_schema_view(
    openapi.Info(
        title='Slug Product API',
        default_version='v1',
        description='API documentation for Slug Product',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(
            name='Damir',
            email='damin_99.99@mail.ru',
            url='https://github.com/damir1899'),
        license=openapi.License(
            name='BSD License'
        )
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
        # permissions.IsAuthenticated,
        # permissions.IsAdminUser
    ]
)


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='scema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='scema-swagger'),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns += static(settings.STATIC_URL, 
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)
