from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo',)
    list_filter = ('fecha',)
    ordering = ('-fecha',)
