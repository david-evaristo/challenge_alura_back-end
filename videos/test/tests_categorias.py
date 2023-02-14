from rest_framework.test import APITestCase
from videos.models import Categoria
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CategoriasTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Categorias-list')
        self.user = User.objects.create_user('testeuser', password='123456')
        self.video_1 = Categoria.objects.create(
            titulo = 'Titulo teste 1',
            cor = 'Cor teste 1'
        )
        self.video_2 = Categoria.objects.create(
            titulo = 'Titulo teste 2',
            cor = 'Cor teste 2'
        )
    
    def test_requisicao_get_para_listar_categorias(self):
        '''Teste para verificar a requisição GET para listar os categorias'''
        # user = User.objects.get(id=1)
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)