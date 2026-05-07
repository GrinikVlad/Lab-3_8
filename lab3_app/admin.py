from django.contrib import admin
from .models import Brand, Category, Rim, NewsletterSubscriber, Rating

# Налаштування для Брендів
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created_at')

# Налаштування для Категорій
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

# Налаштування для дисків
@admin.register(Rim)
class RimAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'created_at')

# Відображення підписників
@admin.register(NewsletterSubscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'joined_at')
    search_fields = ('email',)

# Відображення оцінок
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rim', 'score', 'created_at')