import json

import requests
from shared_lists import credentials
from pprint import pprint as pp

url = credentials.url
payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': credentials.apiKey,
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
retrieved = response.json()

mr18 = 0
mr20 = 0
mx100 = 0
devices_in_use = []
device_names = []
for i in retrieved:
    device_data = {'model': i['model'],
                   'mac': i['mac'],
                   'serial#': i['serial']
                   }
    devices_in_use.append(device_data)
    if i['model'] == "MR18":
        mr18 += 1
    elif i['model'] == "MR20":
        mr20 += 1
    elif i['model'] == "MX100":
        mx100 += 1

output = json.dumps(devices_in_use, indent=2)

with open('meraki_devices.txt', 'w') as f:
    f.write('Devices in use in the "alp-projects-wireless" network are:')
    f.write(output)
    f.write('\n')
    f.write(f"Model MR18's in this environment = {mr18}\n")
    f.write(f"Model MR20's in this environment = {mr20}\n")
    f.write(f"Model MX100's in this environment = {mx100}\n")
