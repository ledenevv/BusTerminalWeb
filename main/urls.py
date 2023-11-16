from django.contrib import admin
from django.urls import path
from .views import login_view, register_view
from main.views import index

urlpatterns = [
    path('main/', index ),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login')
]