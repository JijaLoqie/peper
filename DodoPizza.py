from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
URL = 'https://dodopizza.ru/moscow#pizzas'
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
    items = soup.find('section', class_='sc-814yrq-2 bVRcWG', id='pizzas')
    titles = items.find_all('article', class_="sc-1x0pa1d-6 dpfxvk")
    parts = []
    count = len(titles)
    for i in range(count):
        parts.append(titles[i].text.replace(titles[i].h2.text, ''))
        titles[i] = titles[i].h2.text.replace('\xa0',' ')
    
    global_data['Пицца'] = titles
    global_data['Ингридиенты'] = parts

    price = items.find_all('div', class_="sc-1x0pa1d-5 dKJLGn")
    for i in range(count):
        price[i] = price[i].span.text
    global_data['Начальная цена'] = price

    global_data['Ингридиенты'][0] = 'На ваш вкус и цвет!'

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
p.to_excel('Pizzas.xlsx')
