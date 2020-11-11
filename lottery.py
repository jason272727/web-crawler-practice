# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:18:48 2020

@author: User
"""

import requests
from bs4 import BeautifulSoup
url='https://www.taiwanlottery.com.tw/'
html=requests.get(url)
html.encoding='UTF-8'
sp = BeautifulSoup(html.text,'lxml')
data=sp.find('div',class_='contents_box02')
date=data.find('span',class_='font_black15').text
print('開獎期數:',date)
res1=data.find_all('div',class_='ball_tx ball_green')
print('開出順序:',end='')
for i  in range(0,6):
    print(res1[i].text,end='')
print('\n大小順序:',end='')
for j in range(6,12):
    print(res1[j].text,end='')
print('\n第二區:',end='')
spec=data.find('div',class_='ball_red').text
print(spec)