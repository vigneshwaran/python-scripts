# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


count=0
def printmove(fr,to):
    print('move from '+str(fr)+' to '+str(to))
    global count
    count+=1
def Towers(n,fr,to,spare):
    if n==1:
        printmove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
       

n=4
Towers(n,'source','destination','broker')
print(count)