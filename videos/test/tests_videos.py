from rest_framework.test import APITestCase
from videos.models import Video, Categoria
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class VideosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Videos-list')
        self.categoria = Categoria.objects.create("teste")
        self.categoria_id = Categoria.objects.get(self.categoria).id
        self.user = User.objects.create_user('testeuser', password='123456')
        self.video_1 = Video.objects.create(
            titulo = 'Titulo Teste 1', 
            descricao = 'Descrição teste 1', 
            url= 'URL teste 1',
            categoria_id = self.categoria_id
        )
        self.video_2 = Video.objects.create(
            titulo = 'Titulo Teste 2', 
            descricao = 'Descrição teste 2', 
            url= 'URL teste 2'
        )
    
    def test_requisicao_get_para_listar_videos(self):
        '''Teste para verificar a requisição GET para listar os Videos'''
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
