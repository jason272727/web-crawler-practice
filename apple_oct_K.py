# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:40:12 2020

@author: User
"""

import pandas as pd
import pandas_datareader.data as web
import datetime
start=datetime.datetime(2020, 10, 2)
end=datetime.datetime(2020, 10, 31)
xlwb=pd.ExcelWriter('C:/Users/User/Desktop/pypractice/apple_oct_stock.xlsx')
data=web.get_data_yahoo('AAPL', start,end)
data.to_excel(xlwb,'Apple')
xlwb.save()