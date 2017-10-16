
 


# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""
import speech_recognition as sr
import json
from wit import Wit
from misc_fn import dump, load, find_entity
from datetime import datetime
from interactions_1 import default_greeting
from commands_1 import weather_forecast

 

"""Main file for interacting with xera_v1.0"""

# Access_token taken from wit.ai (server-side)
access_token = 'UN7WMZXEXLEMUTXBG6IO64JWL6X6MUDC'
client = Wit(access_token=access_token)



# Dict of all actions
actions = {
	'default_greeting': default_greeting,
	'weather_forecast': weather_forecast,
}




# Main loop to keep xera running
while True:

	# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)
	    print('Message recorded.')
	    
    	
 
# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    input_text = r.recognize_google(audio)
	    input_text = input_text.lower()
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	
	print('Input text = ' + str(input_text) + '\n')

	# User inputs 'end' to break loop
	if input_text == 'end':
		break

	# Response by wit.ai
	resp = client.message(input_text)
	print(resp)
	print('\n')

	# Filtering out intents and entities from response
	entities = resp['entities']
	intents = entities['intent']

	# Running actions based on intents
	for intent in intents:
		intent_val = intent['value']

		text_resp = actions[intent_val](entities)

		# Printing response
		print('\n')
		print('text_response = ' + text_resp + '\n')

		


		






    

    


