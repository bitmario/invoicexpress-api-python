==========================
InvoiceXpress API - Python
==========================

.. image:: https://img.shields.io/pypi/v/invoicexpress_api.svg
        :alt: PyPI
        :target: https://pypi.python.org/pypi/invoicexpress_api

.. image:: https://api.travis-ci.org/bitmario/invoicexpress-api-python.svg?branch=master
        :alt: Build Status
        :target: https://travis-ci.org/bitmario/invoicexpress-api-python

.. image:: https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5%2C%203.6-blue.svg
        :alt: Python 3.3, 3.4, 3.5, 3.6
        :target: https://travis-ci.org/bitmario/invoicexpress-api-python

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :alt: MIT License
        :target: https://github.com/bitmario/invoicexpress-api-python/blob/master/LICENSE.txt


Thin Python 3 wrapper for the InvoiceXpress REST API. Currently rough and incomplete.

API docs at: https://developers.invoicexpress.com/docs/versions/2.0.0/

Included APIs
-------------

================== =========
API                Done in
================== =========
Invoices_          v0.1.0
Estimates_         to-do
Guides_            to-do
`Purchase Orders`_ to-do
Clients_           v0.1.0
Items_             to-do
Sequences_         to-do
Taxes_             to-do
Accounts_          to-do
SAF-T_             to-do
================== =========

.. _Invoices: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/invoices
.. _Estimates: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/estimates
.. _Guides: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/guides
.. _`Purchase Orders`: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/purchase-orders
.. _Clients: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/clients
.. _Items: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/items
.. _Sequences: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/sequences
.. _Taxes: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/taxes
.. _Accounts: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/accounts
.. _SAF-T: https://developers.invoicexpress.com/docs/versions/2.0.0/resources/saf-t

Installation
------------

Automatic install via pip:

.. code-block:: bash

    $ pip install invoicexpress-api


Usage
-----

Setup
^^^^^
.. code-block:: pycon

    >>> import invoicexpress_api as ie
    >>> c = ie.Client('my_account_name', 'my_api_key')

Create an invoice
^^^^^^^^^^^^^^^^^
.. code-block:: pycon

    >>> invoice_type = ie.invoices.Types.INVOICE_RECEIPT
    >>> invoice_data = {
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
    >>> ie.invoices.create(c, invoice_data, invoice_type)
    {
        'invoice_receipt':{
            'id':12345678,
            'status':'draft',
            'archived':False,
            'type':'InvoiceReceipt',
            'sequence_number':'rascunho',
            'date':'17/04/2018',
            'due_date':'17/04/2018',
            'reference':None,
            'observations':None,
            'retention':None,
            'permalink':'https://www.app.invoicexpress.com/documents/113a4152...',
            'sum':50.0,
            'discount':0.0,
            'before_taxes':50.0,
            'taxes':11.5,
            'total':61.5,
            'currency':'Euro',
            'client':{
                'id':1234567,
                'name':'John Doe',
                'code':'XYZ123'
            },
            'items':[
                {
                    'name':'SRV1',
                    'description':'Service 1',
                    'unit_price':'10.0',
                    'unit':None,
                    'quantity':'5.0',
                    'tax':{
                        'id':123456,
                        'name':'IVA23',
                        'value':23.0
                    },
                    'discount':0.0,
                    'subtotal':50.0,
                    'tax_amount':11.5,
                    'discount_amount':0.0,
                    'total':61.5
                }
            ]
        }
    }

Fetch and update an invoice
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: pycon
    
    >>> inv = ie.invoices.get(c, 12345678, invoice_type)
    >>> inv[invoice_type]['items'][0]['unit_price'] = 150
    >>> ie.invoices.update(c, 12345678, inv, invoice_type)
    >>> ie.invoices.get(c, 12345678, invoice_type)
    {
        'invoice_receipt':{
            'id':12345678,
            'status':'settled',
            'archived':False,
            'type':'InvoiceReceipt',
            'sequence_number':'1/A',
            'inverted_sequence_number':'A/1',
            'sequence_id':123456,
            'date':'17/04/2018',
            'due_date':'17/04/2018',
            'reference':None,
            'observations':None,
            'retention':None,
            'permalink':'https://www.app.invoicexpress.com/documents/113a4152...',
            'saft_hash':'iyuX',
            'sum':750.0,
            'discount':0.0,
            'before_taxes':750.0,
            'taxes':172.5,
            'total':922.5,
            'currency':'Euro',
            'client':{
                'id':1234567,
                'name':'John Doe',
                'code':'XYZ123',
            },
            'items':[
                {
                    'name':'SRV1',
                    'description':'Service 1',
                    'unit_price':'150.0',
                    'unit':None,
                    'quantity':'5.0',
                    'tax':{
                        'id':123456,
                        'name':'IVA23',
                        'value':23.0
                    },
                    'discount':0.0,
                    'subtotal':750.0,
                    'tax_amount':172.5,
                    'discount_amount':0.0,
                    'total':922.5
                }
            ]
        }
    }


Set invoice state and send by e-mail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: pycon
    
    >>> ie.invoices.change_state(c, 12345678, ie.invoices.States.FINAL)
    >>> ie.invoices.send_email(c, 12345678, 'name@domain.tld',
			       'New invoice!',
			       'Hi John,\r\nHere is your invoice\r\nRegards,')

License
--------

MIT License. See the `LICENSE 
<https://github.com/bitmario/invoicexpress-api-python/blob/master/LICENSE.txt>`_ 
file for details.
