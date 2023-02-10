from django.contrib import admin
from videos.models import Video

# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id','titulo', 'descricao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
admin.site.register(Video, Videos)