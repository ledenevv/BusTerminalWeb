from django.contrib import admin
from django.urls import path
from .views import login_view, register_view, routes_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('routes/', routes_view, name='routes')
]