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
from commands_1 import weather_forecast

"""Main file for interacting with xera_v1.0"""

# access_token taken from wit.ai (server-side)
access_token = 'UN7WMZXEXLEMUTXBG6IO64JWL6X6MUDC'

client = Wit(access_token=access_token)

# dict of all actions
actions = {
	'default_greeting': default_greeting,
	'weather_forecast': weather_forecast,
}


i = 0 # Loop counter for easy testing

# Main loop to keep xera running
while True:
	i += 1 # Loop counter for easy testing

	# User text input
	#print('Your input = ')
	#input_text = input()

	# Inputs for easy testing
	if i == 1:
		input_text = 'hello'
	elif i == 2:
		input_text = 'hello xera'
	elif i == 3:
		input_text = 'hello siri'
	elif i == 4:
		input_text = 'what is the weather in london?'
	else:
		break
	print('Input text = ' + str(input_text))

	# User inputs 'end' to break loop
	if input_text == 'end':
		break

	# Response by wit.ai
	resp = client.message(input_text)
	print(resp)

	# Filtering out intents and entities from response
	entities = resp['entities']
	intents = entities['intent']

	# Running actions based on intents
	for intent in intents:
		intent_val = intent['value']
		print(actions[intent_val](entities))


		






    

    


