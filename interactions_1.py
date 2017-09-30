import json
from misc_fn import rand_choice, find_entity, compare


def default_greeting(entities):
	print('Running interactions_1.default_greeting')
	greetings_list = [
		'Hello!',
		'Hey there!'
	]

	greetings_val = find_entity(entities, 'greetings')
	contact_val = find_entity(entities, 'contact')
	if greetings_val == 'true':
		if contact_val is None:
			return rand_choice(greetings_list)
		elif compare(contact_val, 'xera') == True:
			return 'Hello master'
	else:
		return None

