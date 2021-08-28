import requests as rq
import json as js


def GetHolidays():
    url = 'https://date.nager.at/api/v3/publicholidays/'
    year = input('Adja meg az évet:')
    location = '/HU'
    request = url + str(year) + location
    response = rq.get(request)
    jsonformated = js.loads(response.text)
    for item in jsonformated:
        with open('unnepek.xls', 'a', encoding='UTF-8') as f:
            f.write(str(item["date"]) + ": " + str(item["localName"]) + "\n")
    f.close()
