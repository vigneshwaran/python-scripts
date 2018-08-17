# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:25:32 2017

@author: Vigneshwaran
"""

"""

Using tuple, we can return more than one value """


list=[23,89,65,'rggr']
print(list[2])

tuple=(445,435,'etgr')
print(tuple[2])

""" we must use ',' after tuple[] in case of tuples. Also we can't change any values"""
num=()
num=num+(tuple[1],)
print(num)

list[1]=98
