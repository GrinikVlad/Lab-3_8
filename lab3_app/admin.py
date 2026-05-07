from django.contrib import admin
from .models import Brand, Category, Rim

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # list_display вказує, які колонки показувати в списку
    list_display = ('name', 'country', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Rim)
class RimAdmin(admin.ModelAdmin):
    # Додали також бренд, діаметр і ціну для більшої наочності
    list_display = ('name', 'brand', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('brand', 'category') # Фільтри збоку