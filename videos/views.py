from rest_framework import viewsets, generics, filters
from videos.models import Video, Categoria
from videos.serializer import VideoSerializer, CategoriaSerializer, ListaCategoriasVideosSerializer
from django_filters.rest_framework import DjangoFilterBackend

#versioning_class = settings.REST_FRAMEWORK.get('DEFAULT_VERSIONING_CLASS')

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    queryset = Video.objects.all()
    def get_serializer_class(self):
        return VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']

class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as Categorias"""
    queryset = Categoria.objects.all()
    def get_serializer_class(self):
        return CategoriaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']

class ListaCategoriasVideos(generics.ListAPIView):
    '''EXIBINDO OS VIDEOS DE UMA CATEGORIA'''
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCategoriasVideosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']