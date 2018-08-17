# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:56:45 2017

@author: Vigneshwaran
"""

def ispalindrome(s):
    def tochars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans=ans+c
        #print(ans)
        return ans
    def ispal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[1] and ispal(s[1:-1])
    return ispal(tochars(s))
ispalindrome('malayalam ')
print(ispalindrome('mam'))