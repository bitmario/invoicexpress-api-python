import time
import requests


class Client:
    base_url = ''
    api_key = ''

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    @staticmethod
    def _check_http_status(response: requests.Response) -> str:
        if response.status_code not in [200, 201]:
            raise ValueError('Error running API request ({} {}): {}'.format(response.status_code,
                                                                       response.reason,
                                                                       response.text))

    def _build_params(self, urlparams: dict) -> str:
        urlparams['api_key'] = self.api_key
        return urlparams

    def _build_url(self, path: str) -> str:
        return '{}{}'.format(self.base_url, path)

    def get(self, path: str, urlparams={}):
        r = None
        tries = 1
        while True:
            r = requests.get(self._build_url(path), params=self._build_params(urlparams))
            if r.status_code != 202 or tries > 6:
                break
            time.sleep(0.05)
            tries += 1
        self._check_http_status(r)
        return r.json()

    def post(self, path: str, json: dict, urlparams={}):
        r = requests.post(self._build_url(path), json=json, params=self._build_params(urlparams))
        self._check_http_status(r)
        return r.json()

    def put(self, path: str, json: dict, urlparams={}):
        r = requests.put(self._build_url(path), json=json, params=self._build_params(urlparams))
        self._check_http_status(r)
