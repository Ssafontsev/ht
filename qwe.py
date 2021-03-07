import requests

url = 'https://httpbin.org/get'
resp = requests.get(url)
print(resp.json)