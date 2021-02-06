import json


def writetojson(data):
    with open('data.json', "w") as f:
        json.dump(data, f, ensure_ascii=False)
        f.close()


datas = {'personal': {}}
datas['personal']['name'] = str(input('Név:'))
datas['personal']['phone'] = str(input('Telefonszám:'))
datas['personal']['birthDatum'] = str(input('Születési dátum:'))
datas['personal']['motherName'] = str(input('Anyja neve:'))
datas['personal']['country'] = str(input('Ország:'))
datas['personal']['zipCode'] = str(input('Irányítószám:'))
datas['personal']['city'] = str(input('Város:'))
datas['personal']['address'] = {}
datas['personal']['address']['street'] = str(input('Utca:'))
datas['personal']['address']['type'] = str(input('Típus:'))
datas['personal']['address']['number'] = str(input('Házszám:'))

writetojson(datas)
