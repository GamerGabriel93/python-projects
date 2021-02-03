from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import os
import urllib3


def process_kill():
    os.system('cmd /c "taskkill /f /im chrome.exe')
    os.system('cmd /c "taskkill /f /im chromedriver.exe"')


option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=option)
urllib3.disable_warnings()


def pri():
    driver.get('https://www.playitstore.hu/ps4/konzolok/playstation-4-pro-1tb')
    sleep(1)
    price = (driver.find_element_by_xpath('//*[@id="poduct_current_price"]')).text
    with open('price.txt', 'a') as save:
        save.write('\n' + price)
    save.close()
    driver.close()
    driver.quit()
    process_kill()


pri()
