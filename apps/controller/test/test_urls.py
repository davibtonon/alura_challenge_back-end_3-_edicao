from django.test import TestCase, RequestFactory
from apps.controller.views import index, importacoes_realizadas,transacoes_importadas, analise_transacao
from django.contrib.auth.models import User
from controller.models import Transacao, ImportacaoRealizada
from django.db import models

from datetime import datetime


class ControllerUrlsTestcase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='teste', 
            email='teste@email.com', 
            password='203050')
        cls.user.save()

        cls.transacao = Transacao.objects.create(
            banco_origem = 'Banco_origem_teste',
            agencia_origem = 'Agencia_origem_teste',
            conta_origem = "Conta_origem_teset",
            banco_destino = 'Banco_destino_teste',
            agencia_destino = 'Agencia_destino_teste',
            conta_destino = 'Conta_destino_teste',
            valor_transacao = 1000,
            data = datetime.now(),
            usuario = cls.user ,

        )
        cls.transacao.save()

        cls.importacao_realizadas = ImportacaoRealizada.objects.create(
            data_transacao = datetime.now().date(),
            data_importacao = datetime.now(),
            usuario = cls.user
        )

    def test_rota_pagina_index(self):
        """ Teste da rota da pagina index"""

        request = self.factory.get('/')
        request.user = self.user

        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    def test_importacao_realizadas(self):
        request = self.factory.get('/importacoes_realizadas')
        request.user = self.user

        with self.assertTemplateUsed('importacoes_realizadas.html'):
            response = importacoes_realizadas(request)
            self.assertEqual(response.status_code, 200)
    
    def test_transacoes_importadas(self):
        request = self.factory.get('/transacoes_importadas/1')
        request.user = self.user

        with self.assertTemplateUsed('transacoes_importadas.html'):
            response = transacoes_importadas(request, 1)
            self.assertEqual(response.status_code, 200)

    def test_analise_transacoes(self):
        """Teste rota analise de transacoes"""
        mes_procura = str(datetime.now().date())[:7]
        
        request = self.factory.post(
            '/analise_transacao', 
            {'mes_procura': mes_procura })
        request.user = self.user
        
        with self.assertTemplateUsed('analise_transacao.html'):
            response = analise_transacao(request)
            self.assertEqual(response.status_code, 200)