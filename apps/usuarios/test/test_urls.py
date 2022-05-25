from django.test import TestCase, RequestFactory, Client
from apps.usuarios.views import login, cadastro, lista_usuarios, edita_usuario
from django.contrib.auth.models import User



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

    def test_rota_url_login_usa_a_views_login_get(self):
        """ Teste se a url da pagina de login utiliza a views login"""

        request = self.factory.get('login')
        with self.assertTemplateUsed('login.html'):
            response = login(request)
            self.assertEqual(response.status_code, 200)

    def test_para_fazer_login_usuarios_post(self):
        """Testa quando um usuario faz login.
        verificado se e redirecionado para pagina index"""

        post_request = self.cliente.post('/login',
        {  'password':203050, 'email':self.user.email}, follow=True)
        self.assertRedirects(post_request, '/')

    def test_rota_de_cadastro_usuarios_get(self):
        """ Teste a requisicao GET da pagina de cadastro de usuarios,
            está usando o templates de cadastros.html"""
     
        request = self.factory.get('cadastro')
        with self.assertTemplateUsed('cadastros.html'):
            response = cadastro(request)
            self.assertEqual(response.status_code, 200)
    
    def test_cadastro_usuarios_post(self):
        """Testa para verificar se um usuarios está fazendo cadastros no site,
        e é redirecionado para pagina index"""

        post_request = self.client.post(
            '/cadastro',
            {'nome': 'davi', 'email': 'davi@gmail.com'})
        self.assertRedirects(post_request, '/', target_status_code=302)
    
    def test_rota_lista_de_usuarios(self):
        """Testa se a requisicao da lista de usuarios está usando a view correta"""

        # self.cliente.login(username='teste',password='203050')
        # request = self.cliente.get('/lista_usuarios')
        
        request = self.factory.get('lista_usuarios/')
        request.user = self.user

        with self.assertTemplateUsed('lista_usuarios.html'):
            response = lista_usuarios(request)
            self.assertEqual(response.status_code, 200)

        # self.assertTemplateUsed(request, 'lista_usuarios.html')
        # self.assertEqual(request.status_code, 200)
    
    def test_solicitacao_de_logout(self):
        """Teste url logout do sistema"""

        self.cliente.login(username='teste',password='203050')
        request = self.cliente.get('/logout')
        self.assertRedirects(request, '/login', 302)

    def test_editar_dados_usuarios(self):
        """Teste para edita dados de um usuario"""
       
        request = self.factory.get('usuarios/edita/'+ str(self.user.id))
        request.user = self.user
        with self.assertTemplateUsed('edita_usuario.html'):
            response = edita_usuario(request, self.user.id)
            self.assertEqual(response.status_code, 200)

    def test_rota_atualizar_usuario(self):
        # Testa rota da url de atualização de usuarios

        self.cliente.force_login(self.user)
        redirect_response = self.cliente.post('/usuarios/atualiza',
       {
           'nome': self.user.username,
           'email': 'novo@email.gmail',
           'id': self.user.id
       })
        
        self.assertRedirects(redirect_response, '/lista_usuarios')
    
    def test_deleta_usuario(self):
        """Teste para url de deleta usuarios"""

        self.cliente.force_login(self.user)
        redirect_response = self.cliente.post(
            '/usuarios/deleta/' + str(self.user.id),
            {'usuario_id':self.user.id})

        print(redirect_response.status_code)
        self.assertRedirects(redirect_response,'/lista_usuarios', target_status_code=302)