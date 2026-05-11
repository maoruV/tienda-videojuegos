from django.urls import path
from . import views

app_name = "buscador"

urlpatterns = [
    path('', views.buscar_juegos, name='buscar'),
    path('api/', views.buscar_json, name='buscar_api'),
]
