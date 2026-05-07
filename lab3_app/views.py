from django.shortcuts import render, get_object_or_404, redirect
from .models import Rim, Category, Rating, NewsletterSubscriber, Order, OrderItem
from django.db.models import Avg
from .forms import NewsletterForm, RatingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import ExtendedUserCreationForm

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

def main_page(request):
    return render(request, 'lab3_app/index.html', {
        'categories': Category.objects.all(),
        'rims': Rim.objects.all()
    })

# Сторінка конкретної категорії
def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    rims = Rim.objects.filter(category=category) # Тільки товари цієї категорії
    return render(request, 'lab3_app/category.html', {
        'category': category,
        'categories': Category.objects.all(),
        'rims': rims
    })

# Сторінка одного товару
def rim_detail(request, rim_id):
    rim = get_object_or_404(Rim, id=rim_id)
    return render(request, 'lab3_app/rim_detail.html', {
        'rim': rim,
        'categories': Category.objects.all()
    })


def main_page(request):
    # Обробка форми розсилки в хедері/футері на кожній сторінці
    if request.method == 'POST' and 'subscribe' in request.POST:
        sub_form = NewsletterForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('main')

    return render(request, 'lab3_app/index.html', {
        'categories': Category.objects.all(),
        'rims': Rim.objects.all(),
        'sub_form': NewsletterForm()
    })


def rim_detail(request, rim_id):
    rim = get_object_or_404(Rim, id=rim_id)

    # Обробка оцінки
    if request.method == 'POST' and 'rate' in request.POST:
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            new_rating.rim = rim
            new_rating.save()
            return redirect('rim_detail', rim_id=rim.id)
    else:
        rating_form = RatingForm()

    # Рахуємо середній бал
    avg_rating = rim.ratings.aggregate(Avg('score'))['score__avg']

    return render(request, 'lab3_app/rim_detail.html', {
        'rim': rim,
        'rating_form': rating_form,
        'avg_rating': avg_rating,
    })


def add_to_cart(request, rim_id):
    cart = request.session.get('cart', [])
    cart.append(rim_id)
    request.session['cart'] = cart
    return redirect('cart_page')


def cart_page(request):
    cart = request.session.get('cart', [])
    rims = Rim.objects.filter(id__in=cart)

    # Логіка для кнопки "Оформити замовлення"
    if request.method == 'POST' and 'checkout' in request.POST:
        request.session['cart'] = []  # Очищаємо кошик після "замовлення"
        return render(request, 'lab3_app/cart.html', {'message': "Дякуємо! Ваше замовлення прийнято."})

    return render(request, 'lab3_app/cart.html', {'rims': rims})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_staff:  # Якщо адмін
        orders = Order.objects.all().order_by('-created_at')
    else:  # Якщо звичайний юзер
        orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'lab3_app/profile.html', {'orders': orders})


# Онови функцію оформлення замовлення в cart_page
def checkout(request):
    cart_ids = request.session.get('cart', [])
    if cart_ids and request.user.is_authenticated:
        new_order = Order.objects.create(user=request.user)
        rims = Rim.objects.filter(id__in=cart_ids)
        for rim in rims:
            OrderItem.objects.create(order=new_order, rim=rim, price=rim.price)
        request.session['cart'] = []  # Очищуємо кошик
        return redirect('profile')
    return redirect('login')


@login_required
def profile(request):
    if request.user.is_staff:
        # Адмін бачить абсолютно всі замовлення сайту
        orders = Order.objects.all().order_by('-created_at')
    else:
        # Звичайний користувач бачить лише ті, де він вказаний як власник
        orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'lab3_app/profile.html', {'orders': orders})

# Створюємо власну форму на основі стандартної, щоб додати поле Email
class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Обов'язкове поле для відновлення пароля")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# У твоїй view-функції:
def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            # 1. Зберігаємо користувача в змінну
            user = form.save()

            # 2. Автоматично логінимо його
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # 3. Перекидаємо відразу на головну (або в профіль)
            return redirect('main')
    else:
        form = ExtendedUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})