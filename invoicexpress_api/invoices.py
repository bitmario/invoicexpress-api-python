from .core import Client


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


def create(client: Client, data: dict, type=Types.INVOICE_RECEIPT) -> dict:
    path = '/{}s.json'.format(type)
    return client.post(path, data)


def get(client: Client, id: int, type=Types.INVOICE_RECEIPT) -> dict:
    path = '/{}s/{}.json'.format(type, id)
    return client.get(path)


def update(client: Client, id: int, data: dict, type=Types.INVOICE_RECEIPT):
    path = '/{}s/{}.json'.format(type, id)
    client.put(path, data)


def change_state(client: Client, id: int, state=States.SETTLED, message='', type=Types.INVOICE_RECEIPT):
    path = '/{}s/{}/change-state.json'.format(type, id)
    data = {type: {
                'state': state
                }
            }
    if message != '':
        data['message'] = message
    client.put(path, data)


def get_pdf_url(client: Client, id: int) -> str:
    path = '/api/pdf/{}.json'.format(id)
    res = client.get(path)
    return res['output']['pdfUrl']


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
