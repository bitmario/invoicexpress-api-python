from .core import Client


def create(client: Client, data: dict) -> dict:
    return client.post('/clients.json', data)


def get(client: Client, id: int) -> dict:
    path = '/clients/{}.json'.format(id)
    return client.get(path)


def update(client: Client, id: int, data: dict):
    path = '/clients/{}.json'.format(id)
    client.put(path, data)


def code_search(client: Client, code: str) -> dict:
    return client.get('/clients/find-by-code.json',
                      urlparams={'client_code': code})
