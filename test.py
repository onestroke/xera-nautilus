# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:26:14 2017

@author: alexr
"""
#import simplejson as json
import json


def dump(data, filename):
    """Save JSON object to file"""
    with open(filename, 'w') as f:
        data = json.dump(data, f)


def load(filename):
    """Load JSON object from file"""
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


a = {'1174561402652568' : 'phyllis poh',
     '1410039532390737' : 'kai tan',
     '1575402229166905' : 'hui shu',
     '1117609775034736' : 'yuan han'
    }
print('a = '+str(a))

dump(a,'contacts.txt')
x1=load('contacts.txt')

print(x1)
print(type(x1))    
print('finished')
