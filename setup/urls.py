from django.contrib import admin
from django.urls import path,include
from videos.views import VideosViewSet, CategoriasViewSet, ListaVideoCategoria, ListaCategoriasVideos
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriasViewSet, basename='Categorias')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path("videos/<int:pk>/categorias/", ListaVideoCategoria.as_view()),
    path("categorias/<int:pk>/videos/", ListaCategoriasVideos.as_view()),
]
