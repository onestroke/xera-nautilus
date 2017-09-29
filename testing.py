# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""

import os
import json
import sys
import requests
from wit import Wit
from flask import Flask, request
from misc_fn import dump, load
from datetime import datetime
from pytz import timezone
from interactions_1 import greetings



"""Main file for interacting with xera_v1.0"""

# access_token is taken from wit.ai
access_token = 'UN7WMZXEXLEMUTXBG6IO64JWL6X6MUDC'

client = Wit(access_token=access_token)

# text to be tested
message_text = 'hello'

# response from wit.ai
resp = client.message(message_text)
print('Response = ' + str(resp))
print(type(resp))
print(resp['entities'])
entities = resp['entities']

actions = {
	'greetings': greetings
}



print(entities['greetings'][0]['value'])

for entry in actions:
	print(entities[entry][0]['value'])

print(actions['greetings'](val=True))

list1 = [1, 2, 3, 4]
print(type(list1))
if type(list1) is list:
	print(list1)

print('testing repo')







    

    


