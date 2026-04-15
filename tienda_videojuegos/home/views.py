from django.shortcuts import render
from catalogo.models import Juego
import random
from django.contrib import messages

# Vista de la pagina principal
def index(request):

    # Opción 1: juegos aleatorios (tipo tienda real)
    juegos_destacados = Juego.objects.all().order_by('?')[:6]

    # Opción 2 (mejor a futuro): los más recientes
    # juegos_destacados = Juego.objects.all().order_by('-id')[:6]

    contexto = {
        'juegos_destacados': juegos_destacados
    }

    return render(request, 'home/index.html', contexto)

# Vista de la pagina de contactos
def contacto(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Aquí podrías enviar email o guardar en BD
        messages.success(request, 'Mensaje enviado correctamente')

    return render(request, 'home/contacto.html')
