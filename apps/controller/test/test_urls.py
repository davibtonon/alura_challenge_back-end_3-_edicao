from django.test import TestCase, RequestFactory
from apps.controller.views import index


class ControllerUrlsTestcase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    # def test_cadastro_usuarios(self):
    #     """ Teste a pagina de cadastro de usuarios"""
    #     request = self.factory.get('/')

    #     with self.assertTemplateUsed('index.html'):
    #         response = index(request)
    #         self.assertEqual(response.status_code, 200)