from django.db import models


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