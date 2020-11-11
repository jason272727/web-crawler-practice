# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 01:06:02 2020

@author: User
"""

import pandas as pd
import pandas_datareader.data as web
import datetime
start=datetime.datetime(2000, 1, 1)
end=datetime.datetime(2020, 10, 30)
lis1=['2303','2330','3008','2498','2311','2409','2357','2317']
xlwb=pd.ExcelWriter('C:/Users/User/Desktop/pypractice/allstock.xlsx')
for i in range(0,len(lis1)):
    try:
        stock=lis1[i]+'.tw'
        data=web.DataReader(stock,'yahoo',start,end)
        data.to_excel(xlwb,lis1[i])
    except KeyError:
        pass
xlwb.save()
                    