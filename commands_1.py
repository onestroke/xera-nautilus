import json
import pyowm
from misc_fn import compare, rand_choice, find_entity, find_confidence

def weather_forecast(entities):
	"""
	Gets current weather from Open Weather Map (OWM) in given location.
	"""
	print('Running commands_1.weather_forecast')

	# Get data from OWM with API key
	owm = pyowm.OWM('e324e0ba4da528c80606bdd257fd54d7')

	# Get location and confidence from entities
	location_val = find_entity(entities, 'location')
	location_cfd = find_confidence(entities, 'location', location_val)

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
	weather = ("Location in: "
		+ location_val
		+ ".\n"
		+"Today's weather is: "
		+ status
		+ ".\n"
		+ "The temperature is: "
		+ str(avg_temp)
		+ " (from "
		+ str(min_temp)
		+ " to "
		+ str(max_temp)
		+ ").\n"
		+ "Humidity is: "
		+ str(humidity)
		+ ".")

	return weather