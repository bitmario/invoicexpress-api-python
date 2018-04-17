from invoicexpress_api import Client

def test_build_params():
    params = Client._build_params(['a=1', 'asd=def'])
    assert params == '&a=1&asd=def'
