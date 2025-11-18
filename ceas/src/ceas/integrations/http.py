import requests

class HttpClient:
    def __init__(self, base_url='', headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def request(self, method, endpoint, **kwargs):
        url = self.base_url + endpoint
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request('PUT', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)

# Default HTTP client
http = HttpClient()

def task(func):
    def wrapper(*args, **kwargs):
        # Here we can inject the http client or other context
        return func(*args, http=http, **kwargs)
    return wrapper
