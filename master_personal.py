# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""

import json
from wit import Wit
from misc_fn import dump, load, find_entity
from datetime import datetime
from interactions_1 import default_greeting


"""Main file for interacting with xera_v1.0"""

# access_token taken from wit.ai (server-side)
access_token = 'UN7WMZXEXLEMUTXBG6IO64JWL6X6MUDC'

client = Wit(access_token=access_token)

# dict of all actions
actions = {
	'default_greeting': default_greeting
}

# main loop to keep xera running
i = 0
while True:
	i += 1

	# user text input
	#print('Your input = ')
	#input_text = input()
	if i == 1:
		input_text = 'hello'
	elif i == 2:
		input_text = 'hello xera'
	else:
		break
	print('Input text = ' + str(input_text))

	# user inputs 'end' to break loop
	if input_text == 'end':
		break

	# response by wit.ai
	resp = client.message(input_text)
	print(resp)

	entities = resp['entities']
	intents = entities['intent']
	for intent in intents:
		intent_val = intent['value']
		print(actions[intent_val](entities))


		






    

    


