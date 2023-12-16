from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from main.models import Route, Ticket
from django.contrib.auth.models import User
from datetime import datetime


def index_view(request):
    return render(request, 'main/index.html')


def mytickets_view(request):
    tickets = Ticket.objects.filter(passenger_id=request.user)
    routes = Route.objects.all()
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.delete()
    return render(request, 'main/mytickets.html', {'tickets': tickets, 'routes': routes})


def routes_view(request):
    routes = Route.objects.all()
    if request.method == 'POST':
        if 'buy_ticket' in request.POST:
            user_id = request.user.id
            route_id = request.POST.get('route_id')
            ticket = Ticket.objects.create(passenger_id=user_id, route_id=route_id)
            return redirect('routes')
        elif 'delete_route' in request.POST:
            route_id = request.POST.get('route_id')
            try:
                route = Route.objects.get(id=route_id)
                route.delete()
                return redirect('routes')
            except Route.DoesNotExist:
                pass
        elif 'edit_route' in request.POST:
            route_id = request.POST.get('route_id')
            try:
                route = Route.objects.get(id=route_id)
                # Получаем данные из POST-запроса для редактирования
                name = request.POST.get('name')
                start_point = request.POST.get('start_point')
                end_point = request.POST.get('end_point')
                schedule = request.POST.get('schedule')
                price = request.POST.get('price')

                # Применяем изменения к объекту маршрута
                route.name = name
                route.start_point = start_point
                route.end_point = end_point
                route.schedule = schedule
                route.price = price

                # Сохраняем обновленный маршрут
                route.save()

                return redirect('routes')
            except Route.DoesNotExist:
                pass
    current_datetime = datetime.now()
    for route in routes:
        if current_datetime >= route.schedule.replace(tzinfo=None):
            route.status = 'Проведен'
        else:
            route.status = 'Ожидает'
        route.save()
    return render(request, 'main/routes.html', {'routes': routes, 'current_datetime': current_datetime})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(index_view)  # перенаправление на главную страницу после входа
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(index_view)  # Перенаправьте пользователя на нужную страницу после выхода


def edit_routes_view(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            start_point = request.POST.get('start_point')
            end_point = request.POST.get('end_point')
            schedule = request.POST.get('schedule')
            price = request.POST.get('price')

            route = Route(name=name, start_point=start_point, end_point=end_point,
                          schedule=schedule, price=price)
            route.save()

            return redirect('routes')  # Перенаправляем пользователя на страницу со списком маршрутов

        return render(request, 'main/editroutes.html')
