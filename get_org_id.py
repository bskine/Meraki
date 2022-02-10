import json

import requests
from shared_lists import credentials

base_url = "https://api.meraki.com/api/v1/organizations"

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': credentials.apiKey,
    'Accept': 'application/json'
}


response = requests.request("GET", base_url, headers=headers, data=payload)
retrieved = response.json()

for i in retrieved:
    org_id = i['id']

print(f'Organization ID for use in API calls is {org_id}')
