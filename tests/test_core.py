from pytest import fixture
from invoicexpress_api import Client


@fixture
def client():
    return Client('dummy', 'secret123')


def test_build_params(client):
    params = client._build_params({'a': 1, 'x': 'asd'})

    assert len(params) == 3
    assert 'a' in params
    assert params['a'] == 1
    assert 'x' in params
    assert params['x'] == 'asd'
    assert 'api_key' in params
    assert params['api_key'] == 'secret123'


def test_build_params_empty(client):
    params = client._build_params({})
    
    assert len(params) == 1
    assert 'api_key' in params
    assert params['api_key'] == 'secret123'


def test_build_url(client):
    url = client._build_url('/test.json')

    assert url == 'https://dummy.app.invoicexpress.com/test.json'
