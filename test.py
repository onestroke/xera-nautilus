# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:26:14 2017

@author: alexr
"""

file = open("logs.txt",'r+') 

file.write('hello there')
print(file.read())
file.close
print('finished')
