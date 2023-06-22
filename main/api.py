from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny, # разрешение на все запросы
        # permissions.IsAuthenticated,                    #разрешение после авторизации
        # permissions.IsAdminUser,                        # разрешение только администраторам
        # permissions.IsAuthenticatedOrReadOnly,          #разрешение на чтение без администраторов
        
    ]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.AllowAny, # разрешение на все запросы
        # permissions.IsAuthenticated,                    #разрешение после авторизации
        # permissions.IsAdminUser,                        # разрешение только администраторам
        # permissions.IsAuthenticatedOrReadOnly,          #разрешение на чтение без администраторов
        
    ]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)