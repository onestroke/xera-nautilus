import json
from misc_fn import rand_choice, find_entity, compare


def default_greeting(entities):
	"""
	Returns a greeting from a list.
	Responds to 'hello'
	"""
	print('Running interactions_1.default_greeting')
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
			return rand_choice(greetings_list)
		elif compare(contact_val, 'xera') == True:
			return 'Hello master'
		elif compare(contact_val, 'siri') == True:
			return 'Do I look like dumb blonde living in an overpriced phone?'
		elif compare(contact_val, 'alexa') == True:
			return 'I am neither mythical, nor savage, nor missing my right boob.'
		elif compare(contact_val, 'cortana') == True:
			return 'You need treatment John, that PTSD cannot go on forever.'
	else:
		return None

