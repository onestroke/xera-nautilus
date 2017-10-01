import pyowm

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