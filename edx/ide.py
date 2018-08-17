# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 02:30:59 2017
"""



guess=0.0
increment=0.001
epsilon=0.1
cube=27
ans=0.0
noofguess=0
while abs(ans**3-cube)>=epsilon:
    guess+=increment
    noofguess=+1
print('no of guesses is ',noofguess)
if abs(ans**3-cube)>=epsilon:
    print('can\'t find cubeth root')
else:
    print('the cubeth root ',guess)

