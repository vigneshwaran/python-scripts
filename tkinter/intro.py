# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:38:29 2018

@author: Vigneshwaran
"""


from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')

lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
btn = Button(window, text="Click Me")
 
btn.grid(column=1, row=1)

lbl1 = Label(window, text="Hello World")
 
lbl1.grid(column=2, row=0)
window.mainloop()