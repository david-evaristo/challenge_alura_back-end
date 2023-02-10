from django.http import JsonResponse

from rest_framework import viewsets, generics
from videos.models import Video
from videos.serializer import VideoSerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

#versioning_class = settings.REST_FRAMEWORK.get('DEFAULT_VERSIONING_CLASS')

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os videos"""
    queryset = Video.objects.all()
    def get_serializer_class(self):
        return VideoSerializer