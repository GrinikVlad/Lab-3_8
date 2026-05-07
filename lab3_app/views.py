from django.shortcuts import render

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