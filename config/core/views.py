from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Article, Cart, Category

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_site')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def main_site(request):
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
    article = get_object_or_404(Article, id=article_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        article=article
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return JsonResponse({'cart_count': Cart.objects.filter(user=request.user).count()})

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.article.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def user_login(request):
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
