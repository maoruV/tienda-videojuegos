from django.shortcuts import render

# Vista de la pagina principal
def index(request):
    # Render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

# Vista de la pagina de contactos
def contacto(request):
    # Render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/contacto.html')
