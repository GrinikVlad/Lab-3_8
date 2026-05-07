from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('page-1/', views.page_one, name='lab3_page1'),
    path('page-2/', views.page_two, name='lab3_page2'),
    path('about/', views.about_page, name='about'),
    path('category/<int:category_id>/', views.main_page, name='category'),
]