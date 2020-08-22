from bs4 import BeautifulSoup
import requests
import pandas as pd

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
    items = soup.find_all('div', {'class': 'iULuXr'})
    titles, parts, price = [], [], []
    print(items)

    for i in items:
        title = i.find('h2', class_='sc-1fleilf-5 butGbl').get_text()
        print(title)
        print(123)

    


    global_data['Пицца'] = titles
    global_data['Описание'] = parts
    global_data['Начальная цена'] = price


    pizza_data = pd.DataFrame(global_data)
    return(pizza_data)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
        
    else:
        print("Wrong format")

p = parse()
print(p)
