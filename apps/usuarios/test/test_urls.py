import email
from http import client
from django.test import TestCase, RequestFactory, Client
from apps.usuarios.views import login, cadastro, lista_usuarios
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware


# Create your tests here.

class UsuariosUrlsTestcase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.cliente = Client()

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
        """Testa quando um usuario faz login.
        verificado se e redirecionado para pagina index"""

        post_request = self.cliente.post('/login',
        {  'password':203050, 'email':self.user.email}, follow=True)
        self.assertRedirects(post_request, '/')

    def test_cadastro_usuarios_get(self):
        """ Teste a requisicao GET da pagina de cadastro de usuarios"""

        request = self.factory.get('cadastro')
        with self.assertTemplateUsed('cadastros.html'):
            response = cadastro(request)
            self.assertEqual(response.status_code, 200)
    
    def test_cadastro_usuarios_post(self):
        """Testa a requisicao POST da pagina de cadastros"""

        post_request = self.client.post(
            '/cadastro',
            {'nome': 'davi', 'email': 'davi@gmail.com'})
        self.assertRedirects(post_request, '/', target_status_code=302)

    def test_lista_de_usuarios(self):
        """Testa as requisição do templates da lista de usuarios"""

        self.cliente.login(username='teste',password='203050')
        request = self.cliente.get('/lista_usuarios')
       
        self.assertTemplateUsed(request, 'lista_usuarios.html')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.status_code, 200)
 