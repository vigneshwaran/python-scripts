# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:33:44 2017

@author: Vigneshwaran
"""
b=0
def fib(x):
    global b
    if x==0 or x==1:
        b=1
        return b
    else:
        b=fib(x-1)+fib(x-2)
        return b
print(fib(7))