from bs4 import BeautifulSoup
import requests

URL = 'https://dodopizza.ru/moscow#pizzas'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.86 YaBrowser/20.8.0.903 Yowser/2.5 Yptp/1.23 Safari/537.36', 
    'accept': '*/*'}
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    print(1)
    soup = BeautifulSoup(html, 'html.parser') #второй параметр - необязателен
    print(2)
    items = soup.find_all('section', class_='sc-814yrq-2 bVRcWG', id='pizzas')
    return items


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        l = get_content(html.text)
        for i in l:
            print(i.main.h2.text)
    else:
        print("Wrong format")


parse()
