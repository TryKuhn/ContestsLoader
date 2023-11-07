import json
import os.path

from apiCodeforces import CodeforcesApi

if os.path.exists('cache/Api.json'):
    api = open('cache/Api.json')
    data = json.load(api)
    api_key = data['apiKey']
    api_secret = data['apiSecret']
    client_key

print("Enter api key:")
api_key = input()

api_key = '20c641f1843da2b5da2cc1d3d8855a30b2e0bd74'
api_secret = '50fe7edcd5bf211d2bbf14ad7cd38a2ee666e0df'
api = CodeforcesApi(api_key, api_secret, 'https://codeforces.com')

api.get_standings('1')
