from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
        

def slugify_func(content):
    return slugify(content)
        

class Product(models.Model):
    # Первый вариант создания слагов
    # slug = models.SlugField(max_length=100, unique=True, verbose_name='URL Slug')
    # Второй вариант создания слагов
    # slug = AutoSlugField(populate_from='name')
    slug = AutoSlugField(populate_from=slugify_func, unique=True, editable=False)
    
    
    image = models.ImageField(upload_to='product/', verbose_name='Изобрание')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self) -> str:
        return f'{self.name} - {self.category} - {self.price}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']