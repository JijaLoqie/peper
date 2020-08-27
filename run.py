import Dodo
import dominoz
import pandas as pd
import glob

print(1)
Dodo.main()
print(2)
dominoz.main()
print('Done')
someXlsx = glob.glob('*xlsx')
menus = []
for i in someXlsx:
    menus.append(pd.read_excel(i, index_col = 0))

newdf = pd.concat(menus)
newdf = newdf.sort_values(by='Начальная цена')
newdf.to_excel('FullMenu.xlsx')
