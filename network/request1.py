import requests
import time


def RequestData():
    # adószám lekérdezése
    run = True
    while run is not False:
        vatNumber = input('Adjom meg egy adószámot:')
        request = 'https://www.nyilvantarto.hu/evny-lekerdezo/api/vallalkozas?adoszam='
        x = requests.get(request+vatNumber)
        if x.status_code == 200:
            with open('adat/response.json', 'w', encoding='UTF-8') as f:
                f.write(x.text)
                f.close()
            print('Adatok lementve az adat mappába!\n')
        else:
            print('Érvénytelen adószám vagy nem adott meg adószámot!\n')
            break


def Checker():
    # website availabitity monitoring
    run = True
    website = input('Type or paste in a website link:')
    while run is not False:
        x = requests.get(website)
        if x.status_code == 200:
            print('Webpage is available!')
            time.sleep(5)
        else:
            print('No response!')
            break


Checker()
