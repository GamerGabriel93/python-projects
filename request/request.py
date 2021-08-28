import time
import requests


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


def Another():
    # post a payload on a url
    url = 'https://www.gamestar.hu/hirek'
    payload = {'some': 'data'}
    r = requests.post(url, json=payload)
    print(r.text)


def Cookies():
    # allow_redirects=False/True
    r = requests.get('http://github.com/', timeout=0.1)
    x = r.url
    print(x)


def SaveAWebpage():
    # save a webpage into a html file
    website = input('Type or paste a url:')
    r = requests.get(website)
    with open('last.html', 'w', encoding='UTF-8') as f:
        f.write(r.text)
        f.close()
