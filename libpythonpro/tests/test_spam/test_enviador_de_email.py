import pytest

from libpythonpro.spam.enviador_de_email import Enviador


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
    assert 'atiladalan@gmail.com' in resultado
