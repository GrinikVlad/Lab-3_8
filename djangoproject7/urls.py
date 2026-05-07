from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab3/', include('lab3_app.urls')), # Підключаємо urls нашої аплікухи
]