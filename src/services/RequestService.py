import requests

class RequestService():
    def __init__(self):
        self.url = "https://httpbin.org/get"
        self.headers = {'Content-Type': 'application/json'}

    def get_example(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()