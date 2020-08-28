import Dodo
import dominoz
import pandas as pd
import glob
import os
print('Парсинг сайта Додо...')
Dodo.main()
print("Готово. Парсинг сайта Доминос...")
dominoz.main()
print('Готово, открываем меню...')
someXlsx = glob.glob('AllData/*xlsx')
menus = []
for i in someXlsx:
    menus.append(pd.read_excel(i, index_col = 0))

newdf = pd.concat(menus)
newdf = newdf.sort_values(by='Начальная цена')
name = 'FullMenu.xlsx'
if name in glob.glob(name):
    os.remove(name)
newdf.to_excel(name)
os.startfile(name)
