import requests

class APIClient:
    """ Reusable API client for sending HTTP request. """

    def get(self,url):
       return requests.get(url)

    def post(self,url,payload):
        return requests.post(url, json=payload)

    def put(self,url,payload):
        return requests.put(url, json= payload)

    def delete(self,url):
       return requests.delete(url)
