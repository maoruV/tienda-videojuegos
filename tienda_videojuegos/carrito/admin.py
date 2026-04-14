from django.contrib import admin
from .models import Carrito, ItemCarrito

# Inline para mostrar los items del carrito
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0 # No mostrar filas vacias adicionales
    readonly_fields = ('subtotal',) # subtotal solo lectura

# Admin para el carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total_items', 'total_precio', 'creado', 'actualizado')
    search_fields = ('usuario__username',)
    # Carrito por nombre de usuario
    inlines = [ItemCarritoInline]

# Admin para los items (opcional, tambien accesible por separado)
@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'juego', 'cantidad', 'subtotal')
    list_filter = ('carrito',)
    search_fields = ('juego__nombre',)
    readonly_fields = ('subtotal',)
