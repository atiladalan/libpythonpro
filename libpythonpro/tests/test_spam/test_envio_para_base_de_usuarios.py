import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Atila', email='atiladalan@gmail.com'),
            Usuario(nome='Fabio', email='fabio@gmail.com')
        ],
        [
            Usuario(nome='Atila', email='atiladalan@gmail.com')
        ],
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'atiladalan@gmail.com',
        'Curso Python Pro',
        'Confira os Modulos fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados +=1



def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Atila', email='atiladalan@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fabio@gmail.com',
        'Curso Python Pro',
        'Confira os Modulos fantasticos'
    )
    assert enviador.parametros_de_envio == (
        'fabio@gmail.com',
        'atiladalan@gmail.com',
        'Curso Python Pro',
        'Confira os Modulos fantasticos'
    )
