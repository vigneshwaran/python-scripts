# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:54:35 2017

@author: Vigneshwaran
"""


class cordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,other):
        sum=self.x+other.x
        d=self.y+other.y
        return (sum,d)
    def __str__(self):
        return "x="+str(self.x)+"\ty="+str(self.y)
    def __sub__(self,other):
       return cordinate(self.x-other.x,self.y-other.y)
    def disp(self):
       return (self.x,self.y)
    def div(self,p=8):
       return (self.x/self.y,p)
class rt(object):
    def __init__(self):
        self.talk=None
    def __str__(self):
        return str(56)
c=cordinate(5,3)
v=cordinate(2,10)
print(c.add(v))   # cordinate.add(c,v)
print(c)
print(isinstance(c,cordinate))

m=c-v
print(m)
print(c.div(79))

h=rt()
print(h)