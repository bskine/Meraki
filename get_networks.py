import json

import requests
from shared_lists import credentials
from pprint import pprint as pp

base_url = credentials.base_url
url = f'{base_url}organizations/{credentials.org_id}/networks'
payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': credentials.apiKey,
    'Accept': 'application/json',
    "Content-Type": "application/json"
}

response = requests.request("GET", url, headers=headers, data=payload)
pp(response.json())
