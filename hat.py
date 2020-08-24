from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://pizzahut.ru/#!/catalog/hot-pizza'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.86 YaBrowser/20.8.0.903 Yowser/2.5 Yptp/1.23 Safari/537.36', 
    'accept': '*/*'}
global_data = {}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r



def get_content(html):

    soup = BeautifulSoup(html, 'html.parser') #второй параметр - необязателен

    mane = soup.find('div', class_='col-md-8 food-content')
    print(mane)
    titles, parts, price = [], [], []
    for i in mane:
        titles.append(i['data-title'])
        price.append(i['data-price'])
    allParts = soup.find_all('div', class_='font4 text-center description')

    for i in allParts:
        parts.append(i.text)


    
    


    global_data['Пицца'] = titles
    global_data['Описание'] = parts
    global_data['Начальная цена'] = price
    
    df = pd.DataFrame(global_data)


    return df



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
        
    else:
        print("Wrong format")

def main():
    data = parse()

    data.to_excel('HatPizzas.xlsx')

if __name__ == '__main__':
    main()

