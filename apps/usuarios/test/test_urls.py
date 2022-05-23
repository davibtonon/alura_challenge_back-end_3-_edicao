import email
from http import client
from django.test import TestCase, RequestFactory, Client
from apps.usuarios.views import login, cadastro, lista_usuarios
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware


# Create your tests here.

class UsuariosUrlsTestcase(TestCase):
    
    def setUp(self):
        nome = 'teste'
        email = 'teste@email.com'
        senha = '203050'

        self.factory = RequestFactory()
        self.cliente = Client()

        # self.user = User.objects.create_user(
        #     username=nome, 
        #     email=email, 
        #     password=senha)
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='teste', 
            email='teste@email.com', 
            password='203050')
        cls.user.save()

    def test_login_usuarios_get(self):
        """ Teste get da pagina de login de usuarios"""
        request = self.factory.get('login')

        with self.assertTemplateUsed('login.html'):
            response = login(request)
            self.assertEqual(response.status_code, 200)

    def test_login_usuarios_post(self):
        post_request = self.cliente.post('/login',
        {  'password':203050, 'email':self.user.email}, follow=True)
        self.assertRedirects(post_request, '/')

    def test_cadastro_usuarios_get(self):
        """ Teste a requisicao GET da pagina de cadastro de usuarios"""
        request = self.factory.get('cadastro')

        with self.assertTemplateUsed('cadastros.html'):
            response = cadastro(request)
            self.assertEqual(response.status_code, 200)
    
    def test_cadastro_usurios_post(self):
        """Testa a requisicao POST da pagina de cadastros"""
        post_request = self.client.post(
            '/cadastro',
            {'nome': 'davi', 'email': 'davi@gmail.com'})
        self.assertRedirects(post_request, '/', target_status_code=302)

    def test_lista_de_usuarios(self):
        request = self.factory.get('lista_usuarios')
        self.client.login(password=self.user.password, username=self.user.username)
        request = self.cliente.get('/lista_usuarios')
        with self.assertTemplateUsed('lista_usuarios.html'):
            response = lista_usuarios(request)
            self.assertEqual(response.status_code, 200)