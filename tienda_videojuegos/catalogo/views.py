from django.shortcuts import render

def lista_juegos(request):
   juegos = [
    {'nombre': 'Dogo Racing', 'precio': 75000, 'plataforma': 'PC, PS5, Xbox Series X/S'},
    {'nombre': 'Platform Fighter', 'precio': 50000, 'plataforma': 'PC, Nintendo Switch'},
    {'nombre': 'Galaxy Explorers', 'precio': 92000, 'plataforma': 'PC, PS5'},
    {'nombre': 'Shadow Ninja Legends', 'precio': 68000, 'plataforma': 'PC, PS4, PS5'},
    {'nombre': 'Cyber City 2099', 'precio': 110000, 'plataforma': 'PC, Xbox Series X/S'},
    {'nombre': 'Mystic Kingdom', 'precio': 87000, 'plataforma': 'PC, Nintendo Switch'},
    {'nombre': 'Zombie Survival Outbreak', 'precio': 60000, 'plataforma': 'PC, PS5, Xbox Series X/S'},
    {'nombre': 'Racing Thunder Pro', 'precio': 78000, 'plataforma': 'PC, PS4, Xbox One'},
    {'nombre': 'Dragon Arena Online', 'precio': 95000, 'plataforma': 'PC, PS5'},
    {'nombre': 'Pixel Adventure Quest', 'precio': 42000, 'plataforma': 'PC, Nintendo Switch, Mobile'},
    {'nombre': 'Battle Mechs Arena', 'precio': 88000, 'plataforma': 'PC, Xbox Series X/S'},
    {'nombre': 'Fantasy Heroes Saga', 'precio': 73000, 'plataforma': 'PC, PS5, Nintendo Switch'},
    {'nombre': 'Space Colonies Builder', 'precio': 67000, 'plataforma': 'PC'},
    {'nombre': 'Street Soccer Legends', 'precio': 55000, 'plataforma': 'PC, PS4, Xbox One'},
    {'nombre': 'Ancient Gods Odyssey', 'precio': 99000, 'plataforma': 'PC, PS5, Xbox Series X/S'}
]
   contexto_catalogo_juegos = {'lista_juegos': juegos}
   return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)
