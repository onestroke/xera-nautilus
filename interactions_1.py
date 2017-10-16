import json
from misc_fn import rand_choice, find_entity, compare
from tts_watson.TtsWatson import TtsWatson


def default_greeting(entities):
	"""
	Returns a greeting from a list.
	Responds to 'hello'
	"""
	print('Running interactions_1.default_greeting')

	# Access to Watson text-to-speech
	ttsWatson = TtsWatson('c1073568-6269-4cad-8d61-fe6e9b83ac66',
	'Qneu8xsmWWfF',
	'en-US_AllisonVoice')

	greetings_list = [
		'Hello!',
		'Hey there!'
	]

	# Gets greetings and names from entities
	greetings_val = find_entity(entities, 'greetings')
	contact_val = find_entity(entities, 'contact')

	# Gets greeting string depending on contact detected.
	if greetings_val == 'true':
		if contact_val is None:
			text_resp = rand_choice(greetings_list)
		elif compare(contact_val, 'emily') == True:
			text_resp = 'Hello master'
		elif compare(contact_val, 'siri') == True:
			text_resp = 'Do I look like a dumb blonde living in an overpriced phone?'
		elif compare(contact_val, 'alexa') == True:
			text_resp = 'I am neither mythical, nor savage, nor missing my right boob.'
		elif compare(contact_val, 'cortana') == True:
			text_resp = 'You need treatment John, that PTSD cannot go on forever.'
		else:
			text_resp = 'I am not ' + contact_val + '!'
	else:
		return None

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

