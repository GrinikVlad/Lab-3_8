from django.shortcuts import render
from .models import Rim, Category

def main_page(request):
    # Контекст для головної сторінки
    context = {
        'title': 'Головна сторінка Лаб 3',
        'content': 'Вітаю! Це головна сторінка. Звідси можна перейти на інші.',
        'is_main_page': True, # Прапорець, який скаже шаблону показати потрібні посилання
    }
    return render(request, 'lab3_app/dynamic_page.html', context)

def page_one(request):
    # Контекст для першої сторінки
    context = {
        'title': 'Сторінка 1',
        'content': 'Це контент першої сторінки. Він переданий через контекст!',
        'is_main_page': False,
    }
    return render(request, 'lab3_app/dynamic_page.html', context)

def page_two(request):
    # Контекст для другої сторінки
    context = {
        'title': 'Сторінка 2',
        'content': 'Це контент другої сторінки. Шаблон той самий, а дані інші.',
        'is_main_page': False,
    }
    return render(request, 'lab3_app/dynamic_page.html', context)

def main_page(request):
    categories = Category.objects.all()
    rims = Rim.objects.all()
    context = {
        'categories': categories,
        'rims': rims
    }
    return render(request, 'lab3_app/index.html', context)

def about_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'lab3_app/about.html', context)


def main_page(request, category_id=None):
    categories = Category.objects.all()

    if category_id:
        rims = Rim.objects.filter(category_id=category_id)
    else:
        rims = Rim.objects.all()

    context = {
        'categories': categories,
        'rims': rims
    }
    return render(request, 'lab3_app/index.html', context)