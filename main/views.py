from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

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