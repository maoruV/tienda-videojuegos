from .models import Carrito, ItemCarrito


def carrito_total(request):
    total_items = 0
    try:
        if request.user.is_authenticated:
            carrito = (
                Carrito.objects.prefetch_related("items")
                .filter(usuario=request.user)
                .first()
            )
            if carrito:
                total_items = ItemCarrito.objects.filter(carrito=carrito).count()
    except Exception:
        pass
    return {"carrito_total_items": total_items}
