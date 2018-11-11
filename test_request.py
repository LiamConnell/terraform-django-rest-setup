import requests

url = 'http://54.244.117.183/api/'
query = ['cia', 'condor', 'spy']
payload = {'search': query}
headers = {'Content-type': 'application/json'} #optional

r = requests.post(url, json=payload , headers=headers)
print(r.text)
