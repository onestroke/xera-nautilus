import json
import pyowm
from misc_fn import compare, rand_choice, find_entity, find_confidence
from tts_watson.TtsWatson import TtsWatson

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

	# Default location set to Cambridge, will read from txt
	if (location_val is None
		or compare(location_val, 'Cambridge') == True
		or location_cfd < 0.9
		or location_val == 'weather?'):
		observation = owm.weather_at_place('Cambridge, UK')

	# Other locations
	else:
		observation = owm.weather_at_place(location_val)

	# Get weather
	w = observation.get_weather()

	# Get components of weather such as temperature, humidity, etc
	status = w.get_detailed_status()
	max_temp = w.get_temperature('celsius')['temp_max']
	min_temp = w.get_temperature('celsius')['temp_min']
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
		+ " degrees celsius (from "
		+ str(min_temp)
		+ " degrees celsius to "
		+ str(max_temp)
		+ " degrees celsius).\n"
		+ "Humidity is: "
		+ str(humidity)
		+ "%.")

	# Playing response from Watson tts
	ttsWatson.play('<voice-transformation type="Young"'
		+ ' strength="80%">'
		+ '<speak>'
		+ '<express-as type="GoodNews">'
		+ text_resp
		+ '</express-as>'
		+ '</speak>'
		+ "</voice-transformation>")
	
	return text_resp