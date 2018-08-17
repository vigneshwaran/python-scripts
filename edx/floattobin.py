# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


count=0
num=14.90
result=''
if num<0:
    flag=1
else:
    flag=0
x=num%1
num=int(num)
mm=''
v=''
while x%1!=0:
    x=x*2
    v=v+str(int(x)//1)
    x=x%1
    count+=1
v=v[0:4:1]
print(v)
while num>0:
    result=str(num%2)+result
    num=num//2
print(result+'.'+v)
