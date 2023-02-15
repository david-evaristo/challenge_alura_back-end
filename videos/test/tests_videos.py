from rest_framework.test import APITestCase
from videos.models import Video, Categoria
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class VideosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Videos-list')
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.categoria = Categoria.objects.create(titulo='Titulo categoria teste',cor='Cor teste categoria').pk
        self.video_1 = Video.objects.create(
            titulo = 'Titulo Teste 1', 
            descricao = 'Descrição teste 1', 
            url= 'URL teste 1',
            categoria_id = self.categoria
        )
        self.video_2 = Video.objects.create(
            titulo = 'Titulo Teste 2', 
            descricao = 'Descrição teste 2', 
            url= 'URL teste 2',
            categoria_id = self.categoria
        )
    
    def test_requisicao_get_para_listar_videos(self):
        '''Teste para verificar a requisição GET para listar os Videos'''
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_videos(self):
        '''Teste para verificar a requisição POST para criar um Video'''
        data = {
            'titulo':'Titulo teste criação video',
            'descricao':'Descrição teste criação video',
            'url':'URL teste criação video',
            'categoria_id': 1
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_videos(self):
        '''Teste para verificar a requisição DELETE para deletar um Video'''
        self.client.force_authenticate(self.user)
        response = self.client.delete('/videos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_videos(self):
        '''Teste para verificar a requisição PUT para atualizar um Video'''
        data = {
            'titulo':'Titulo teste criação video',
            'descricao':'Descrição teste criação video',
            'url':'URL teste criação video',
            'categoria_id': 1
        }
        self.client.force_authenticate(self.user)
        response = self.client.put('/videos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



