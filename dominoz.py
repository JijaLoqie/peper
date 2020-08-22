from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

URL = 'https://dominospizza.ru'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.86 YaBrowser/20.8.0.903 Yowser/2.5 Yptp/1.23 Safari/537.36', 
    'accept': '*/*'}
global_data = {}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    print(1)
    soup = BeautifulSoup(html, 'html.parser') #второй параметр - необязателен
    print(2)
    mane = soup.find_all('h2', class_='sc-1fleilf-5 hiuaAU')

    titles, parts, price = [], [], []
    for i in mane:
        titles.append(i.text)
    mane = soup.find_all('div', class_='sc-1fleilf-16 kYcovD')
    for i in mane:
        price.append(i.text)
        print(i.text)
    print(mane,'-----------------------------')
    
    


    global_data['Пицца'] = titles
    global_data['Описание'] = parts
    global_data['Начальная цена'] = price


    return 1


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
        
    else:
        print("Wrong format")

p = parse()
print(p)
