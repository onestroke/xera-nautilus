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
from misc_fn import dump, load, find_entity, find_confidence
from datetime import datetime, timedelta, time
from pytz import timezone
import pytz as pytz
from interactions_1 import default_greeting
from commands_1 import weather_forecast



"""Main file for interacting with xera_v1.0"""

# access_token is taken from wit.ai
access_token = 'UN7WMZXEXLEMUTXBG6IO64JWL6X6MUDC'

client = Wit(access_token=access_token)


owm = pyowm.OWM('e324e0ba4da528c80606bdd257fd54d7')  
# You MUST provide a valid API key

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

message = 'what is the weather in Cambridge today?'
resp = client.message(message)
entities = resp['entities']
print(entities)
datetime_val = find_entity(entities,'datetime')
print(datetime_val)
print(type(datetime_val))
date_val = datetime_val[:10]
print(date_val)
date_val = date_val.replace('-','')
print(date_val)
year = date_val[:4]
day = date_val[6:]
month = date_val[4:6]
print(year, month, day)
london = timezone('Europe/London')
singapore = timezone('Asia/Singapore')
time_val = datetime_val[11:16]
time_val = time_val.replace(':','')
hour = time_val[:2]
minute = time_val[3:5]
year = int(year)
month = int(month)
day = int(day)
hour = int(hour)
minute = int(minute)
date_val1 = datetime(year, month, day, hour, minute, tzinfo=london)
print(datetime.now(london))
print(date_val1)
print(date_val1 - datetime.now(london))

if ( datetime.now(london) - date_val1 < timedelta(minutes=1)
	and date_val1.time() != time(00,00)):
	print('weather right now')
else:
	print('today or tmr')


print('\n')

fc = owm.three_hours_forecast('London,GB')
print(fc)
for weather in fc.get_forecast():
	#print (weather.get_reference_time(timeformat='date'), weather.get_status(), weather.get_detailed_status())
	time1 = (weather.get_reference_time(timeformat='date').time())
	if time(9,00) <= time1 <= time(18,00):
		print(time1)



print('\n')
clear = 0
clouds = 0
rain = 0
for weather in fc.get_forecast():
	if (timedelta(days=0) <= weather.get_reference_time(timeformat='date')
		- date_val1 <= timedelta(days=1)
		and time(9,00) <= weather.get_reference_time(timeformat='date').time()
		<= time(18,00)):
		print(weather.get_reference_time(timeformat='date'))
		print(weather.get_reference_time(timeformat='date') - date_val1)
		if weather.get_status() == 'Clear':
			clear += 1
		elif weather.get_status() == 'Clouds':
			clouds += 1
		elif weather.get_status() == 'Rain':
			rain += 1

print(clear)
print(clouds)
print(rain)

if clear >= clouds and clear >= rain:
	print('weather is mainly clear.')
elif clouds >= clear and clouds >= rain:
	print('weather is mainly cloudy.')
elif rain >= clouds and rain >= clear:
	print('weather is mainly rainy.')

print('\n')
print('\n')

print(weather_forecast(entities))

    

    


