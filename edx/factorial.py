# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:18:01 2017

@author: Vigneshwaran
"""

def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
print("fact(4) =",fact(4))

for i in range(1,6,1):
    print(i)