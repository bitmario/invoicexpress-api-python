from invoicexpress_api import Client


def test_build_params():
    c = Client('https://dummy.app.invoicexpress.com', 'secret123')
    params = c._build_params({'a': 1, 'x': 'asd'})

    assert len(params) == 3
    assert params['a'] == 1
    assert params['x'] == 'asd'
    assert params['api_key'] == 'secret123'


def test_build_params_empty():
    c = Client('https://dummy.app.invoicexpress.com', 'secret123')
    params = c._build_params({})
    
    assert len(params) == 1
    assert params['api_key'] == 'secret123'


def test_build_url():
    c = Client('https://dummy.app.invoicexpress.com', 'secret123')
    url = c._build_url('/test.json')

    assert url == 'https://dummy.app.invoicexpress.com/test.json'
