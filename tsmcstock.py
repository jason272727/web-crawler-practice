# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:25:38 2020

@author: User
"""

import pandas as pd
import pandas_datareader.data as web
import datetime
start=datetime.datetime(2000, 1, 1)
end=datetime.datetime(2020, 11, 2)
data=web.DataReader('2330.tw','yahoo',start,end)
newxl=pd.ExcelWriter('C:/Users/User/Desktop/pypractice/2330stockdata.xlsx')
data.to_excel(newxl,'sheet1')
newxl.save()