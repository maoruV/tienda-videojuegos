from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # Ruta principal: llama a la vista index
    path('contacto/', views.contacto, name='contacto') # Ruta contacto llama a la vista contacto
]