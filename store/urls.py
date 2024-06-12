from django.contrib import admin
from django.urls import path, include
from store import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about_us/', views.about_us, name="about-us"),
    path('shop/', views.shop, name="shop"),
    path('furniture/', views.furniture, name="furniture"),
    path('furniture/<str:category>', views.furniture, name="furniture"),
    path('contact_us/', views.contact_us, name="contact-us"),
    path('shopcart/', views.shopcart, name="shopcart"),
    path('add/<str:id_producto>', views.add_to_cart, name="add-to-cart")
]