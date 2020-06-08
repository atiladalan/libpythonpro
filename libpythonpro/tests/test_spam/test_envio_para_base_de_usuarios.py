import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Atila',email='atiladalan@gmail.com'),
            Usuario(nome='Fabio',email='fabio@gmail.com')
        ],
        [
            Usuario(nome='Atila',email='atiladalan@gmail.com')
        ],
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'atiladalan@gmail.com',
        'Curso Python Pro',
        'Confira os Modulos fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados