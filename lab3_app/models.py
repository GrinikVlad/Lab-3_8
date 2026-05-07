from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва бренду")
    country = models.CharField(max_length=100, verbose_name="Країна виробник")
    # auto_now_add - автоматично записує час при створенні
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    # auto_now - автоматично оновлює час при кожному збереженні
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренди"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Rim(models.Model):
    # Поля моделі
    name = models.CharField(max_length=100, verbose_name="Модель диску")
    diameter = models.IntegerField(verbose_name="Діаметр (R)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (грн)")
    photo = models.ImageField(upload_to='rims_photos/', null=True, blank=True, verbose_name="Фото диску")

    # ЗВ'ЯЗОК ТАБЛИЦЬ: Диск належить певному бренду і певній категорії
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категорія")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    class Meta:
        verbose_name = "Диск"
        verbose_name_plural = "Диски"

    def __str__(self):
        return f"{self.brand.name} {self.name} (R{self.diameter})"

class NewsletterSubscriber(models.Model):
        email = models.EmailField(unique=True)
        joined_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.email

class Rating(models.Model):
        rim = models.ForeignKey('Rim', on_delete=models.CASCADE, related_name='ratings')
        score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Оцінки 1-5
        created_at = models.DateTimeField(auto_now_add=True)
        comment = models.TextField(blank=True, null=True, verbose_name="Коментар")
        text = models.TextField(verbose_name="Ваш коментар", blank=True, null=True)  # Додаємо це
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.rim.name} - {self.score}"

class Order(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
            created_at = models.DateTimeField(auto_now_add=True)
            is_completed = models.BooleanField(default=False)

            def __str__(self):
                return f"Замовлення #{self.id} від {self.user.username}"

class OrderItem(models.Model):
            order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
            rim = models.ForeignKey('Rim', on_delete=models.CASCADE)
            price = models.DecimalField(max_digits=10, decimal_places=2)