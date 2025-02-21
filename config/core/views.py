from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.contrib import messages
from .models import Article, Cart, Category
from django.db.models import F
from decimal import Decimal

# Widoki aplikacji

def register(request):
    """Rejestracja nowego użytkownika"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main_site')
        except IntegrityError:
            messages.error(request, 'Username already exists. Please choose a different username.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def main_site(request):
    """Strona główna sklepu"""
    categories = Category.objects.all()
    articles = Article.objects.all()
    cart_items = Cart.objects.filter(user=request.user).count()
    return render(request, 'main_site.html', {
        'articles': articles,
        'categories': categories,
        'cart_items': cart_items
    })

@login_required
def add_to_cart(request, article_id):
    """Dodawanie produktu do koszyka"""
    article = get_object_or_404(Article, id=article_id)
    if article.stock > 0:
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            article=article
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        article.stock -= 1
        article.save()
        return JsonResponse({
            'cart_count': Cart.objects.filter(user=request.user).count(),
            'stock': article.stock
        })
    return JsonResponse({'error': 'Out of stock'}, status=400)

@login_required
def view_cart(request):
    """Podgląd koszyka"""
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.article.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    """Usuwanie produktu z koszyka"""
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        
        # Return stock to article
        article = cart_item.article
        article.stock += 1
        article.save()
        
        return JsonResponse({'status': 'success'})

def user_login(request):
    """Logowanie użytkownika"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_site')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid login details'})
    return render(request, 'registration/login.html')

def logout_view(request):
    """Wylogowanie użytkownika"""
    logout(request)
    return redirect('login')
