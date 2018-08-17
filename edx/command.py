# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:40:44 2017

@author: Vigneshwaran
"""

import sys

# command line arguments are stored in the form
# of list in sys.argv
sys.argv=[sys.argv[0],30,50]
argumentList = sys.argv
print (argumentList)

# Print the name of file
print (sys.argv[0])

# Print the first argument after the name of file
print (sys.argv[1])

