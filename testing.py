# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""

import os
import json
import sys
import requests
import pyowm
from wit import Wit
from flask import Flask, request
from misc_fn import dump, load
from datetime import datetime
from pytz import timezone
from interactions_1 import default_greeting



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
intents = entities['intent']
print(intents)

actions = {'default_greeting': default_greeting}
entities = resp['entities']
intents = entities['intent']
for intent in intents:
	intent_val = intent['value']
	print(actions[intent_val](entities))


print('\n')

owm = pyowm.OWM('e324e0ba4da528c80606bdd257fd54d7')  # You MUST provide a valid API key

# Search for current weather in London (UK)
observation = owm.weather_at_place('Cambridge, UK')
w = observation.get_weather()


status = w.get_detailed_status()
max_temp = w.get_temperature('celsius')['temp_max']
min_temp = w.get_temperature('celsius')['temp_min']
avg_temp = w.get_temperature('celsius')['temp']
humidity = w.get_humidity()

weather = ("Today's weather is: "
+ status
+ ". The temperature is: "
+ str(avg_temp)
+ " (from "
+ str(min_temp)
+ " to "
+ str(max_temp)
+ "). Humidity is: "
+ str(humidity)
+ ".")

print(weather)
print('\n')

fc = owm.three_hours_forecast('London,uk')
print(fc.get_forecast)

print('\n')

from tts_watson.TtsWatson import TtsWatson
 
ttsWatson = TtsWatson('c1073568-6269-4cad-8d61-fe6e9b83ac66',
	'Qneu8xsmWWfF',
	'en-US_AllisonVoice') 
ttsWatson.play('<voice-transformation type="Custom" glottal_tension="-80%">'
	+ "Hello World"
	+ "</voice-transformation>")

ttsWatson.play("Hello World")




    

    


