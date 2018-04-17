import time
import requests


class Client:
    base_url = ''
    api_key = ''

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        
    @staticmethod
    def _build_params(urlparams: list) -> str:
        params = ''
        for p in urlparams:
            params += '&{}'.format(p)
        return params

    @staticmethod
    def _check_http_status(response: requests.Response) -> str:
        if response.status_code not in [200, 201]:
            raise ValueError('Error running API request ({} {}): {}'.format(response.status_code,
                                                                       response.reason,
                                                                       response.text))

    def _build_url(self, path: str, urlparams: list) -> str:
        return '{}{}?api_key={}{}'.format(self.base_url,
                                          path,
                                          self.api_key,
                                          Client._build_params(urlparams))

    def get(self, path: str, urlparams=[]):
        r = None
        tries = 1
        while True:
            r = requests.get(self._build_url(path, urlparams))
            if r.status_code != 202 or tries > 6:
                break
            time.sleep(0.05)
            tries += 1
        self._check_http_status(r)
        return r.json()

    def post(self, path: str, json: dict, urlparams=[]):
        r = requests.post(self._build_url(path, urlparams), json=json)
        self._check_http_status(r)
        return r.json()

    def put(self, path: str, json: dict, urlparams=[]):
        r = requests.put(self._build_url(path, urlparams), json=json)
        self._check_http_status(r)


class Clients:
    @staticmethod
    def create(client: Client, data: dict) -> dict:
        return client.post('/clients.json', data)

    @staticmethod
    def get(client: Client, id: int) -> dict:
        path = '/clients/{}.json'.format(id)
        return client.get(path)

    @staticmethod
    def update(client: Client, id: int, data: dict):
        path = '/clients/{}.json'.format(id)
        client.put(path, data)

    @staticmethod
    def code_search(client: Client, code: str) -> dict:
        return client.get('/clients/find-by-code.json',
                          urlparams=['client_code={}'.format(code)])


class Invoices:
    class Types:
        INVOICE = 'invoice'
        SIMPLIFIED_INVOICE = 'simplified_invoice'
        INVOICE_RECEIPT = 'invoice_receipt'
        CREDIT_NOTE = 'credit_note'
        DEBIT_NOTE = 'debit_note'

    class States:
        FINAL = 'finalized'
        DELETED = 'deleted'
        CANCELED = 'canceled'
        SETTLED = 'settled'
        UNSETTLED = 'unsettled'

    @staticmethod
    def create(client: Client, data: dict, type=Types.INVOICE_RECEIPT) -> dict:
        path = '/{}s.json'.format(type)
        return client.post(path, data)

    @staticmethod
    def get(client: Client, id: int, type=Types.INVOICE_RECEIPT) -> dict:
        path = '/{}s/{}.json'.format(type, id)
        return client.get(path)

    @staticmethod
    def update(client: Client, id: int, data: dict, type=Types.INVOICE_RECEIPT):
        path = '/{}s/{}.json'.format(type, id)
        client.put(path, data)

    @staticmethod
    def change_state(client: Client, id: int, state=States.SETTLED, message='', type=Types.INVOICE_RECEIPT):
        path = '/{}s/{}/change-state.json'.format(type, id)
        data = {type: {
                    'state': state
                    }
                }
        if message != '':
            data['message'] = message
        client.put(path, data)

    @staticmethod
    def get_pdf_url(client: Client, id: int) -> str:
        path = '/api/pdf/{}.json'.format(id)
        res = client.get(path)
        return res['output']['pdfUrl']

    @staticmethod
    def send_email(client: Client, id: int, email: str, subject=None, body=None, type=Types.INVOICE_RECEIPT):
        path = '/{}s/{}/email-document.json'.format(type, id)
        data = {'message': {
                    'client': {
                        'email': email,
                        'save': '0'
                        }
                    }
                }
        if subject:
            data['message']['subject'] = subject
        if body:
            data['message']['body'] = body
        client.put(path, data)
