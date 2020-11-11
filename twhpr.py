# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:00:04 2020

@author: User
"""

from selenium import webdriver
url='https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c'
driver = webdriver.Chrome('C:/Users/User/.spyder-py3/chromedriver.exe')
driver.get(url)
start='台北'
end='台南'
#個人資料同意,因為參數值會隨時間而有所變化，所以無法利用cookies方式設定
driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]').click()
#起始點設定
driver.find_element_by_xpath('/html/body/div[3]/div[2]/section[3]/div/div[1]/div/div[1]/div/div[1]/select').send_keys(start)
#終點
driver.find_element_by_xpath('/html/body/div[3]/div[2]/section[3]/div/div[1]/div/div[1]/div/div[3]/select').send_keys(end)
#driver.find_element_by_id('Departdate03').click()
driver.find_element_by_xpath('/html/body/div[3]/div[2]/section[3]/div/div[1]/div/div[3]/div[1]/div[1]/input').click()
#driver.find_element_by_id('outWardTime').click()
driver.find_element_by_xpath('/html/body/div[3]/div[2]/section[3]/div/div[1]/div/div[3]/div[1]/div[2]/input').click()
driver.find_element_by_xpath('/html/body/div[3]/div[2]/section[3]/div/div[1]/div/div[5]/button').click()
