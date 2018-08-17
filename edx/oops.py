# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 23:24:39 2017

@author: Vigneshwaran
"""
import datetime
class person(object):
    def __init__(self,name):
        self.name=name
        self.birthday=None
        self.lastname=name.split(' ')[-1]

    def getlastname(self):
        return self.lastname

    def __lt__(self,other):
        if self.lastname==other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        return self.name
    def setbirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
    def age(self):
        return ((datetime.date.today()-self.birthday).days)/365

p1=person('mark zuck')
p1.setbirthday(5,1,1984)
p2=person('bill gates')
p2.setbirthday(3,4,1983)
p3=person('vignesh waran')
p3.setbirthday(6,24,1998)
p4=person('ashish kedia')
p5=person('jack ma')
p6=person('elon musk')

PersonList=[p1,p2,p3,p4,p5,p6]
"""for e in PersonList:
    print(e)
print("After sorting")   """
PersonList.sort()
for e in PersonList:
    print(e)

class mit(person):
    id=0
    def __int__(self,name):
        person.__int__(self,name)
        self.idnum=mit.id
        mit.id+=1
    def __lt__(self,other):
        return self.id<other.id
    def speak(self,word):
        return self.lastname+"  says  "+word
m1=mit('mark zuck')
person.setbirthday(m1,5,1,1984)
m2=mit('vigneshwaran')
m2.setbirthday(6,24,1998)
m3=mit('ram prakash')
m3.setbirthday(10,10,1998)

mitlist=[m1,m2,m3]














