import Dodo
import papa
import dominoz
import pandas as pd
import glob


Dodo.main()
papa.main()
dominoz.main()
someXlsx = glob.glob('*xlsx')
menus = []
for i in someXlsx:
    menus.append(pd.read_excel(i, index_col = 0))

newdf = pd.concat(menus)
newdf.to_excel('FullMenu.xlsx')
