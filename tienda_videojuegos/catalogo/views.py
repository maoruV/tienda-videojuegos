from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Juego


def lista_juegos(request):
    # 1. Query base (ordenado)
    juegos = Juego.objects.all().order_by('id')

    # 2. Paginador
    paginator = Paginator(juegos, 6)

    # 3. Página actual
    page_number = request.GET.get('page')
    lista_juegos = paginator.get_page(page_number)

    # 4. Lógica de rango (para evitar lógica en el template)
    current_page = lista_juegos.number
    total_pages = paginator.num_pages

    rango_paginas = [
        num for num in paginator.page_range
        if current_page - 2 <= num <= current_page + 2
    ]

    # 5. Contexto
    contexto = {
        'lista_juegos': lista_juegos,
        'rango_paginas': rango_paginas,
        'total_paginas': total_pages
    }

    return render(request, 'catalogo/lista_juegos.html', contexto)
