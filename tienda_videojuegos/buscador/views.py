from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from catalogo.models import Juego

def buscar_juegos(request):
    query = request.GET.get('q')

    if query:
        juegos = Juego.objects.filter(
            Q(nombre__icontains=query) |
            Q(plataforma__icontains=query)
        ).order_by('id')
    else:
        juegos = Juego.objects.all().order_by('id')

    # Paginación
    paginator = Paginator(juegos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 🔥 CLAVE: generar rango de páginas
    current_page = page_obj.number
    total_pages = paginator.num_pages

    inicio_pag = max(current_page - 2, 1)
    fin_pag = min(current_page + 2, total_pages)

    rango_paginas = range(inicio_pag, fin_pag + 1)

    context = {
        'lista_juegos': page_obj,
        'rango_paginas': rango_paginas,
        'query': query  
    }

    return render(request, 'buscador/resultados_busqueda.html', context)
