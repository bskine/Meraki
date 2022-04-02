# import json
import requests
from shared_lists import credentials

# from pprint import pprint as pp

get_devices_url = credentials.url
get_devices_payload = {}
get_devices_headers = {
    'X-Cisco-Meraki-API-Key': credentials.apiKey,
    'Accept': 'application/json'
}

response = requests.request("GET", get_devices_url, headers=get_devices_headers, data=get_devices_payload)
retrieved = response.json()

devices_in_use = []
lldp_source = []
for i in retrieved:
    device_data = {'device_name': i['name'],
                   'mac': i['mac'],
                   'serial#': i['serial']
                   }
    sn_for_url = i['serial']
    get_lldp_url = f"https://api.meraki.com/api/v1/devices/{sn_for_url}/lldpCdp"
    get_lldp_payload = {}
    get_lldp_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": credentials.apiKey
    }
    lldp_response = requests.request('GET', get_lldp_url, headers=get_lldp_headers, data=get_lldp_payload)
    lldp_all = lldp_response.json()
    if lldp_all.get('ports') is None:
        print(f'LLDP disabled on port for AP named {i["name"]}')
        continue
    else:
        try:
            yeetus = lldp_all.get('ports')['wired0']['cdp']
            lldp_data = {'deviceId': yeetus['deviceId'],
                         'address': yeetus['address'],
                         'portId': yeetus['portId'],
                         'MAC_of_AP': i['mac']
                         }
            print(f'{i["name"]} : {lldp_data}')
        except Exception:
            yeetus = lldp_all.get('ports')['wan0']['cdp']
            lldp_data = {'deviceId': yeetus['deviceId'],
                         'address': yeetus['address'],
                         'portId': yeetus['portId']
                         }
            print(f'{i["name"]} : {lldp_data}')
