from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('add-to-cart/<int:article_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]
