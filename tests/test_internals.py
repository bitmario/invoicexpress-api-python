from invoicexpress_api import Client

def test_build_params():
    params = Client._build_params(['a=1', 'asd=def'])
    assert params == '&a=1&asd=def'

def test_build_params_empty():
    params = Client._build_params([])
    assert params == ''

def test_build_url():
    pass
