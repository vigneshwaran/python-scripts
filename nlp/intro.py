# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:38:31 2018

@author: Vigneshwaran
"""

from bs4 import BeautifulSoup
 
import urllib.request
import os
import nltk
 
response = urllib.request.urlopen('http://php.net/')
 
html = response.read()

os.chdir(r'G:')
 
soup = BeautifulSoup(html,"html5lib")
 
text = soup.get_text(strip=True)

v=open('text.txt','w')
v.write(str(text))

v.close()

tokens = [t for t in text.split()]

x=open('tokens.txt','w')
x.write(str(tokens))
x.close() 

 
'''for key,val in freq.items():
 
    print (str(key) + ':' + str(val))
'''    

from nltk.corpus import stopwords

clean_tokens = tokens[:]
 
sr = stopwords.words('english')
 
for token in tokens:
 
    if token in stopwords.words('english'):
 
        clean_tokens.remove(token)
#print (text)

freq = nltk.FreqDist(clean_tokens)
freq.plot(20, cumulative=False)