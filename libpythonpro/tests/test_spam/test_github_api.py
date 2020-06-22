from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/63621795?v=4'
    resp_mock.json.return_value = {
        'login': 'atiladalan',
        'id': 3457115,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('atiladalan')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('atiladalan')
    assert 'https://avatars0.githubusercontent.com/u/63621795?v=4' == url
