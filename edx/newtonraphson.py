# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:06:45 2017

@author: Vigneshwaran
"""

epsilon=0.01
y=27.0
guess=y/2.0
no=0

while abs(guess**3-y)>=epsilon:
    no+=1
    guess=guess-(((guess**3)-y)/(3*(guess**2)))
print('no of guesses is ',no)
print(guess)