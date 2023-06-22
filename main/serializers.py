from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 
                  'created_at']
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['image', 
                 'name', 
                 'description', 
                 'price', 
                 'category', 
                 'created_at']