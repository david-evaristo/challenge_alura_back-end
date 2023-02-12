from django.contrib import admin
from videos.models import Video, Categoria

# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id','titulo', 'descricao', 'categoria')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
    ordering = ('id',)
admin.site.register(Video, Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id','titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
    ordering = ('id',)
admin.site.register(Categoria, Categorias)
