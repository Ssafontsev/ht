import requests
import json
response = requests.get('https://stackoverflow.com/questions',
                        headers={'User-Agent': 'netology_client'}, params={'limit': 10})
print(response.status_code)
# print(response.headers)
print(response.text)
# print(response.content)
# print(response.json())
  