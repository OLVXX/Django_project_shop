# Sklep Internetowy - Django Project Shop

## O Projekcie
Projekt prostego sklepu internetowego wykonanego w Django.

## Technologie
- Python 3.13
- Django 5.1.5
- SQLite
- HTML/CSS
- JavaScript

## Funkcje
1. **Panel użytkownika**
   - Rejestracja i logowanie
   - Przeglądanie produktów
   - Zarządzanie koszykiem

2. **Katalog produktów**
   - Podział na kategorie
   - Filtrowanie produktów
   - Informacje o dostępności

3. **Koszyk**
   - Dodawanie/usuwanie produktów
   - Zmiana ilości
   - Podgląd sumy zamówienia

## Uruchomienie projektu
1. **Wymagania**
   - Python 3.10+
   - Django
   - Pillow (do obsługi zdjęć)

2. **Instalacja**
   ```bash
   pip install django
   pip install Pillow
   python manage.py migrate
   python manage.py loaddata initial_data.json
   python manage.py createsuperuser
   python manage.py runserver