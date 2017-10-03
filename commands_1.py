import json
import pyowm
from misc_fn import compare, rand_choice, find_entity, find_confidence
from tts_watson.TtsWatson import TtsWatson
from pytz import timezone
from datetime import datetime, timedelta, time

def weather_forecast(entities):
	"""
	Gets current weather from Open Weather Map (OWM) in given location.
	"""
	print('Running commands_1.weather_forecast')

	# Get data from OWM with API key
	owm = pyowm.OWM('e324e0ba4da528c80606bdd257fd54d7')

	# Access to Watson text-to-speech
	ttsWatson = TtsWatson('c1073568-6269-4cad-8d61-fe6e9b83ac66',
	'Qneu8xsmWWfF',
	'en-US_AllisonVoice')

	# Get location and confidence from entities
	location_val = find_entity(entities, 'location')
	location_cfd = find_confidence(entities, 'location', location_val)

	# Get datetime and confidence from entities
	datetime_val = find_entity(entities,'datetime')

	# Creating datetime object from the datetime string 
	# returned from wit.ai
	if datetime_val is not None:
		date_val = datetime_val[:10]
		date_val = date_val.replace('-','')
		year = date_val[:4]
		year = int(year)
		day = date_val[6:]
		day = int(day)
		month = date_val[4:6]
		month = int(month)
		time_val = datetime_val[11:16]
		time_val = time_val.replace(':','')
		hour = time_val[:2]
		minute = time_val[3:5]
		hour = int(hour)
		minute = int(minute)

		# Setting timezones
		london = timezone('Europe/London')
		singapore = timezone('Asia/Singapore')
	

	# Default location set to Cambridge, will read from txt
	if (location_val is None
		or compare(location_val, 'Cambridge') == True
		or location_cfd < 0.9
		or location_val == 'weather?'):
		observation = owm.weather_at_place('Cambridge, GB')
		fc = owm.three_hours_forecast('Cambridge, GB')
		if datetime_val is not None:
			date_val1 = datetime(year, month, day, hour, minute, tzinfo=london)

	# Other locations: Currently only supports Singapore
	elif compare(location_val, 'Singapore') == True:
		observation = owm.weather_at_place('Singapore')
		fc = owm.three_hours_forecast('Singapore')
		if datetime_val is not None:
			date_val1 = datetime(year, month, day, hour, minute, tzinfo=singapore)
	else:
		observation = owm.weather_at_place(location_val)
		fc = owm.three_hours_forecast(location_val)
		if datetime_val is not None:
			date_val1 = datetime(year, month, day, hour, minute, tzinfo=london)

	# Weather observation at current time.
	if ((datetime_val is not None
		and datetime.now(london) - date_val1 < timedelta(minutes=1)
		and date_val1.time() != time(00,00))
		or datetime_val is None):

		# Get weather
		w = observation.get_weather()

		# Get components of weather such as temperature, humidity, etc
		status = w.get_detailed_status()
		avg_temp = w.get_temperature('celsius')['temp']
		humidity = w.get_humidity()

		# Output in response format
		text_resp = ("Location in: "
			+ location_val
			+ ".\n"
			+"Weather right now is: "
			+ status
			+ ".\n"
			+ "The temperature is: "
			+ str(avg_temp)
			+ " degrees celsius.\n"
			+ "Humidity is: "
			+ str(humidity)
			+ "%.")
	else:

		clear = 0
		clouds = 0
		rain = 0

		# Weather forecast in 3 hour intervals during working hours.
		for weather in fc.get_forecast():
			if (timedelta(days=0) 
				<= weather.get_reference_time(timeformat='date') - date_val1 
				<= timedelta(days=1)
				and time(9,00) 
				<= weather.get_reference_time(timeformat='date').time()
				<= time(18,00)):
				#print(weather.get_reference_time(timeformat='date'))
				#print(weather.get_reference_time(timeformat='date') - date_val1)
				if weather.get_status() == 'Clear':
					clear += 1
				elif weather.get_status() == 'Clouds':
					clouds += 1
				elif weather.get_status() == 'Rain':
					rain += 1

		# Changing text_resp according to detected weather.
		if clear >= clouds and clear >= rain:
			text_resp = 'Weather is mainly clear during working hours.'
		elif clouds >= clear and clouds >= rain:
			text_resp = 'Weather is mainly cloudy during working hours.'
		elif rain >= clouds and rain >= clear:
			text_resp = 'Weather is mainly rainy during working hours. '
		if rain > 0:
			text_resp += 'Rain is expected. Please prepare for wet weather. '
		else:
			text_resp += 'Rain is not expected. I hope it stays that way.'

	# Playing text_response with Watson tts
	ttsWatson.play('<voice-transformation type="Young"'
		+ ' strength="80%">'
		+ '<speak>'
		+ '<express-as type="GoodNews">'
		+ text_resp
		+ '</express-as>'
		+ '</speak>'
		+ "</voice-transformation>")
	
	return text_resp