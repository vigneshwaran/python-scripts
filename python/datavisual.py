# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 12:03:04 2018

@author: Vigneshwaran
"""

import matplotlib.pyplot as plt
import math as m
import numpy as np
x=list(range(0,10))
y=[m.sin(i) for i in range(0,10)]
#np.arange(0,1.0,0.01)
plt.plot(x,y)