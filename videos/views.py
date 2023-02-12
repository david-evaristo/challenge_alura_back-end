from django.http import JsonResponse

from rest_framework import viewsets, generics, filters
from videos.models import Video, Categoria
from videos.serializer import VideoSerializer, CategoriaSerializer, ListaVideosCategoriaSerializer, ListaCategoriasVideosSerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

#versioning_class = settings.REST_FRAMEWORK.get('DEFAULT_VERSIONING_CLASS')

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    queryset = Video.objects.all()
    def get_serializer_class(self):
        return VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']

class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as Categorias"""
    queryset = Categoria.objects.all()
    def get_serializer_class(self):
        return CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']

class ListaVideoCategoria(generics.ListAPIView):
    '''EXIBINDO AS CATEGORIAS DE UM VIDEO'''
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosCategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']

class ListaCategoriasVideos(generics.ListAPIView):
    '''EXIBINDO OS VIDEOS DE UMA CATEGORIA'''
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCategoriasVideosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id','titulo']
    search_fields = ['titulo']