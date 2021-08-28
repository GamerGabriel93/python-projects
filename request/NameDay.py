import requests as rq
import json as js


def GetTodayNameDay():
    api = 'https://api.nevnapok.eu/ma'
    response = rq.get(api, verify=False)
    nevnapok = js.loads(response.text)
    print(nevnapok)


GetTodayNameDay()
