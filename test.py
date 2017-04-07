# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:26:14 2017

@author: alexr
"""
import json as json
file = open("logs.txt",'r+') 
test='adsfhkl'
a = (test,'test1')
json.dump(a,file)
x1=json.load(file)
print(x1)
