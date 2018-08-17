# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 02:03:27 2017

@author: Vigneshwaran
"""
import os,shutil
for folderName, subfolders, filenames in os.walk('G:\COMPUTER SCIENCE\machine-learning'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        if filename.endswith(".mp4"):
            print(filename)
        elif filename.endswith(".en"+".srt"):
            print(filename)
        elif filename.endswith(".pdf"):
            print(filename)
        elif filename.endswith(".html"):
            print(filename)
        else:
            shutil.move(os.path.join(folderName, filename),"C:\\Users\\Vigneshwaraen\\Desktop\\new")

    print('')
               