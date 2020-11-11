# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:46:43 2020

@author: User
"""

import requests
url='https://www.ptt.cc/bbs/Gossiping/index.html'
#將以滿18歲設置為True(True or False 至Application-cookies即可得知)
cookies={'over18':'1'}
html=requests.get(url,cookies=cookies)
print(html.text)