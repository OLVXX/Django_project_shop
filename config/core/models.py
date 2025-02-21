from django.db import models
from django.contrib.auth.models import User

# Kategorie produktów
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Kategorie"
    
    def __str__(self):
        return self.name

# Model produktu
class Article(models.Model):
    name = models.CharField(max_length=200)  # Nazwa produktu
    description = models.TextField()  # Opis produktu
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Cena
    image = models.ImageField(upload_to='articles/', null=True, blank=True)  # Zdjęcie produktu
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Kategoria
    stock = models.IntegerField(default=0)  # Stan magazynowy
    
    def __str__(self):
        return self.name

# Koszyk użytkownika
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Użytkownik
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Produkt
    quantity = models.IntegerField(default=1)  # Ilość
    created_at = models.DateTimeField(auto_now_add=True)  # Data dodania do koszyka
