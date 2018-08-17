# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:31:28 2017

@author: Vigneshwaran
"""

import random

r=int(random.random()*100)
print(r)
s=str(r).zfill(3)
print(s)

print(-5 == True)

a=[43,87,65]

a.append(48)

print("This is a string"[:0:-1])

print("{} can be{} {}".format("Strings"," hahaha ","interpolated"))
print("{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick"))
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))
print("gbb",a)
print("%s can be %s the %s way" % ("Strings", "interpolated", "old"))       #old way
print("%d"%(a[0]))

print("Hello, World", end="!""\n")
"""
    append()
    del
    pop()
    remove()
    index()
    extend() #to concatenate lists
"""
h={'name':'vignesh','age':20}
print(h.keys())
m=list(h.values())
print(m)
print('NOTE:',20 in h,'age' in h,' only it search for key')
#print(h[20])
print(h.get('age','onne'))  #show only available content skip the data not available
h.setdefault("five", 5)
print(h['five'])
"""
   get()
   setdefault()
   del

   '''set'''

"""
seta=set("malayalam")
print(seta)    #displays only characters
seta.update([50,70])    #updatde can be done only with help of list
print(seta)

import datetime
print(datetime.date.today())


def kick(*arg,**war):             #dictory
    return (arg,war)
a=11
print(kick(a,b=30))

import time
t0=time.clock()

import math

t1=time.clock()-t0
print("\nt1:",t1,"\n")

print(math.sqrt(16))
#to import all use from math import *
from math import ceil,floor,trunc

print(ceil(3.7))
print(floor(3.7))
print(trunc(3.7))

#print(dir(math))
























