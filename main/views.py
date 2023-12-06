from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from main.models import Route


def index_view(request):
    return render(request, 'main/index.html')


def routes_view(request):
    return render(request, 'main/routes.html')


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

            route = Route(name=name, start_point=start_point, end_point=end_point,
                          schedule=schedule)
            route.save()

            return redirect('routes')  # Перенаправляем пользователя на страницу со списком маршрутов

        return render(request, 'main/editroutes.html')
