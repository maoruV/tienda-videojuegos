from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages
from carrito.models import Carrito

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'Inicio de sesion exitoso {usuario.username}')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesion correctamente')
    return redirect('login')

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = request.user

        if user.check_password(password):
            try:
                carrito = Carrito.objects.get(usuario=user)
                carrito.items.all().delete()
                carrito.delete()
            except Carrito.DoesNotExist:
                pass

            user.delete()
            logout(request)
            messages.success(request, 'Tu cuenta ha sido eliminada correctamente.')
            return redirect('home')
        else:
            messages.error(request, 'Contraseña incorrecta.')
            return redirect('perfil')

    return redirect('perfil')
