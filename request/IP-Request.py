import json as js
import requests as rq


def IPLookup():
    url = 'https://freegeoip.app/json/'
    ipaddress = input('IP Adress:')
    address = url + str(ipaddress)
    response = rq.get(address)
    with open('response.json', 'a', encoding='UTF-8') as f:
        f.write(response.text)
        f.close()
    python_obj = js.loads(response.text)
    print('\nIP:', python_obj["ip"], '\nOrszág:', python_obj["country_name"], '\nVáros:', python_obj["city"], '\nSzélesség:', python_obj["latitude"],
          '\nHosszúság:', python_obj["longitude"])


IPLookup()
