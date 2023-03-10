from rest_framework import serializers
from videos.models import Video, Categoria

class VideoSerializer(serializers.ModelSerializer):
    # categoria = serializers.ReadOnlyField(source='categoria.titulo')
    class Meta:
        ordering = ['id']
        model = Video
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ListaCategoriasVideosSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = Video
        fields = ['titulo'] #PODE USAR O __ALL__ PARA MOSTRAR TODOS OS CAMPOS AO INVES DE ESCREVER TODOS OS CAMPOS
        #fields = '__all__'
    def get_periodo(self,obj):
        return obj.get_periodo_display()