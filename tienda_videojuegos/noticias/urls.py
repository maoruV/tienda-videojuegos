from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.lista_noticias, name='lista'),
    path('<int:id>/', views.detalle_noticia, name='detalle'),
]