from django.contrib import admin
from django.urls import path
from .views import login_view, register_view, routes_view, logout_view, edit_routes_view, mytickets_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('routes/', routes_view, name='routes'),
    path('logout/', logout_view, name='logout'),
    path('editroutes/', edit_routes_view, name='edit_routes'),
    path('mytickets/', mytickets_view, name='mytickets')

]