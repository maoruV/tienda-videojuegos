from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha')

    return render(request, 'noticias/lista_noticias.html', {
        'noticias': noticias
    })

def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    return render(request, 'noticias/detalle_noticia.html', {
        'noticia': noticia
    })