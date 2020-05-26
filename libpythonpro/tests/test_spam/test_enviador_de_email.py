from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'atiladalan@gmail.com',
        'atiladalan@gmail.com',
        'Teste de Envio de Email do Curso Python PRO',
        'Enviado Email com Sucesso.'
    )
    assert 'atiladalan@gmail.com' in resultado
