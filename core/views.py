from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('home')

        # Cria o usuário usando o e-mail como username
        user = User.objects.create_user(username=email, email=email, password=password, first_name=nome)
        user.save()
        
        # Faz o login automático após o cadastro
        login(request, user)
        messages.success(request, f'Bem-vindo(a), {nome}!')
        return redirect('dashboard')
        
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Busca o usuário pelo e-mail
            user_obj = User.objects.get(email=email)
            # Autentica usando o username atrelado a este e-mail
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Senha incorreta.')
        except User.DoesNotExist:
            messages.error(request, 'E-mail não encontrado.')
            
    return redirect('home')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('home')

@login_required(login_url='home')
def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def sobre(request):
    return render(request, 'sobre.html')