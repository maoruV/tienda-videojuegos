from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalogo.models import Juego
from .models import Carrito, ItemCarrito

@login_required
def agregar_al_carrito(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, juego=juego)
    
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, juego=juego)
    if not creado:
        item.cantidad += 1
        item.save()
        
    return redirect('catalogo:detalle_juego', pk=juego_id)
    
    
@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.select_related('juego')
    total = carrito.total_precio()
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito, 'items': items, 'total': total})

@login_required
def eliminar_del_carrito(request, juego_id):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item = carrito.items.filter(juego_id=juego_id).first()
    if item:
        item.delete()
    return redirect('carrito:ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    carrito.items.all().delete()
    return redirect('carrito:ver_carrito')