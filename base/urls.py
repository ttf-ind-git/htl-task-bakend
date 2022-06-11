from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [
    path('',views.getRoutes, name='routes'),

    path('login/',views.login, name='login'),

    path('faker/',views.faker, name='faker'),
    path('customer_faker/',views.customer_faker, name='customer_faker'),

    path('users/',views.getUsers, name='users'),


    path('products/',views.getProducts, name='products'),
    path('createProduct/',views.createProduct, name='createProduct'),
    path('products/<str:pk>/',views.getProduct, name='product'),
    path('UpdateProduct/<str:pk>/',views.UpdateProduct, name='UpdateProduct'),
    path('DeleteProduct/<str:pk>/',views.DeleteProduct, name='DeleteProduct'),

]