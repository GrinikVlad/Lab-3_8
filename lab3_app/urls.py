from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('category/<int:category_id>/', views.category_page, name='category_detail'),
    path('rim/<int:rim_id>/', views.rim_detail, name='rim_detail'),
    path('about/', views.about_page, name='about'),
    path('cart/', views.cart_page, name='cart_page'),
    path('add-to-cart/<int:rim_id>/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
]