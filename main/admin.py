from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (Category,
                     Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at', 'get_image']
    list_filter = ['category', 'created_at']
    search_fields = ['name']
    
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" >')
        else:
            return 'Not image'
        

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
        
        
        

