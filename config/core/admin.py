from django.contrib import admin
from .models import Category, Article, Cart

# Rejestracja modeli w panelu administracyjnym
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Wyświetlane pola

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock']  # Wyświetlane pola

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'quantity', 'created_at']  # Wyświetlane pola
