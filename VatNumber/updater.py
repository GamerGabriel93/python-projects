from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile
import os
from time import sleep


def process_kill():
    os.system('cmd /c "taskkill /f /im chrome.exe')
    os.system('cmd /c "taskkill /f /im chromedriver.exe"')


def update():
    driver.get('https://chromedriver.chromium.org/downloads')
    sleep(1)
    online_version = (driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td['
                                                   '2]/div/div[3]/div/table/tbody/tr/td/div/div[4]/div[3]/a')).text
    version = str(online_version[-12:-1]) + str(online_version[-1])
    link = "https://chromedriver.storage.googleapis.com/" + str(version) + "/chromedriver_win32.zip"
    print(link)
    process_kill()
    os.system('cmd /c "curl "' + link + '" -o chromedriver.zip"')
    with zipfile.ZipFile("chromedriver.zip") as zip_ref:
        cwd = os.getcwd()
        zip_ref.extractall(cwd)
        zip_ref.close()
        os.system('cmd /c "del chromedriver.zip')


option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=option)
str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

if str1 == str2 or str2 > str1:
    print('A program naprakész!')
else:
    if str1 > str2:
        print('Frissítés szükséges!')
        print('Kérem frissítse a Chrome Webdriver-ét a', str1, 'verzióra')
        update()
