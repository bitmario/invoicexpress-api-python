==========================
InvoiceXpress API - Python
==========================


.. image:: https://img.shields.io/pypi/v/invoicexpress_api.svg
        :alt: PyPI
        :target: https://pypi.python.org/pypi/invoicexpress_api

.. image:: https://img.shields.io/travis/bitmario/invoicexpress-api-python.svg
        :alt: Build Status
        :target: https://travis-ci.org/bitmario/invoicexpress-api-python

.. image:: https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg
        :alt: Python Versions

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :alt: MIT License
        :target: https://github.com/bitmario/invoicexpress-api-python/blob/master/LICENSE.txt


Thin Python 3 client for the InvoiceXpress REST API.

API docs at: https://developers.invoicexpress.com/docs/versions/2.0.0/


Sample usage
------------

.. code-block:: python

	import invoicexpress_api as ie

	BASE_URL = 'https://mycompany.app.invoicexpress.com'
	API_KEY = 'my api key'

	invoice_data = {
	  "invoice": {
		"date": "17/04/2018",
		"due_date": "17/04/2018",
		"client": {
			"name": "John Doe",
			"code": "XYZ123"
		},
		"items": [
			{
			  "name": "SRV1",
			  "description": "Service 1",
			  "unit_price": 10.0,
			  "quantity": 5.0,
			  "tax": {
				  "name": "IVA23"
				  }
			}
		  ]
	   }
	}

	c = ie.Client(BASE_URL, API_KEY)
	inv_type = ie.invoices.Types.INVOICE_RECEIPT
	inv = ie.invoices.create(c, invoice_data, inv_type)
	print('## Create invoice result')
	print(inv)

	cli = ie.clients.code_search(c, inv[inv_type]['client']['code'])
	cli_upd = {"client": {"fiscal_id": "212345678", "country": "Portugal"}}
	ie.clients.update(c, cli['client']['id'], cli_upd)
	print('## Client Updated')
	print(cli)

	inv[inv_type]['items'][0]['unit_price'] = 150
	ie.invoices.update(c, inv[inv_type]['id'], inv, inv_type)
	print('## Invoice Updated')
	print(inv)

	ie.invoices.change_state(c, inv[inv_type]['id'], ie.Invoices.States.FINAL)
	inv = ie.invoices.get(c, inv[inv_type]['id'])
	print('## Invoice Settled')
	print(inv)

	print('PDF URL: ', ie.invoices.get_pdf_url(c, inv[inv_type]['id']))

	ie.invoices.send_email(c, inv[inv_type]['id'], 'email@domail.tld', 'New invoice!', 'Hi John,\r\nHere is your new invoice\r\nRegards,')
	print('## E-mail sent')


License
--------

MIT
