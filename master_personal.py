# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""

import json
from wit import Wit
from misc_fn import dump, load
from datetime import datetime
from interactions_1 import greetings


"""Main file for interacting with xera_v1.0"""

# access_token taken from wit.ai (server-side)
access_token = 'UN7WMZXEXLEMUTXBG6IO64JWL6X6MUDC'

client = Wit(access_token=access_token)

# dict of all actions
actions = {
	'greetings': greetings
}

# main loop to keep xera running
while True:

	# user text input
	print('Your input = ')
	input_text = input()
	print('Input text = ' + str(input_text))

	# user inputs 'end' to break loop
	if input_text == 'end':
		break

	# response by wit.ai
	resp = client.message(input_text)
	print(resp)

	entities = resp['entities']
	for entry in actions:
		print('entry = ' + str(entry))
		print(entities['greetings'][0]['value'])
		try: 
			val = entities['greetings'][0]['value']
			print('val = ' + str(val))
		except KeyError:
			print('key not found')






    

    


