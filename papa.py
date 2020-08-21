from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
URL = 'https://www.papajohns.ru/moscow/'
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
    items = soup.find('div', class_='_2ActO0fnm7_oDvg-SJT-JZ', id='pizza__list')
    items_title = items.find_all('div', class_="aQQmaKmYxsncqMA3oNzKh _1K-NO2hvBJkvG95nIKjJsf ProductCard OCoeOMqCJdPjzC5s_sRgG")
    titles = []
    for i in items_title:
        title = i.h3.text
        titles.append(title)
    
    items_description = items.find_all('div', class_="_1FiPi2Gaw3EGNHfoz45s5u _34NfwZlklq1BtK4zwPsbem")
    descriptions = []
    for i in items_description:
        description = i.text
        descriptions.append(description)

    items_prices = items.find_all('div', class_="_2bUiEDiEIn2oqKbaMdaMvf _25gakQ_Z5WE-pzuH7CC2nM _3x_sQheo-Od3RI74rYvigX bsfJHoo-z7dlyqVDxwpw4")
    prices = []
    for i in items_prices:
        price = i.text
        prices.append(price)
        print(price)
    print(len(titles), len(descriptions), len(prices))
    global_data['Пицца'] = titles
    global_data['Ингридиенты'] = descriptions
    global_data['Начальная цена'] = prices
    return pd.DataFrame(global_data)
    


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        
    else:
        print("Wrong format")

print(parse())

