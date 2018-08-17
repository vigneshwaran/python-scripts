from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd
import re
from bs4 import BeautifulSoup

url=r'http://students.psgitech.ac.in/'
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
name = driver.find_element_by_id("TxtStudID")
name.send_keys(715516104055)
nam = driver.find_element_by_id("TxtPasswd")
nam.send_keys("24JUN98")
button = driver.find_element_by_id("BtnLogin")
button.click()

soup_level1=BeautifulSoup(driver.page_source, 'html.parser')

table = soup_level1.find_all('table')[0]

df = pd.read_html(str(table),header=0)

print(df)



#driver.execute_script("window.history.go(-1)") 