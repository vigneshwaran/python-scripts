# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:22:40 2017

@author: Vigneshwaran
"""

import os
print(os.getcwd())
os.chdir('C:\\Users\\Vigneshwaraen\\Desktop')
print(os.getcwd())
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet2')
