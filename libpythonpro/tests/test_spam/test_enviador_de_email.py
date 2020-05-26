import pytest


from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.enviador_de_email import EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinario',
    ['teste@teste.com.br', 'atiladalan@gmail.com.br']
)

def test_remetente(destinario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinario,
        'atiladalan@gmail.com',
        'Teste de Envio de Email do Curso Python PRO',
        'Enviado Email com Sucesso.'
    )
    assert destinario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['teste.teste.com.br', 'atiladalan']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'atiladalan@gmail.com',
            'Teste de Envio de Email do Curso Python PRO',
            'Enviado Email com Sucesso.'
        )
