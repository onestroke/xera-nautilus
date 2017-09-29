import json
from misc_fn import rand_choice


def greetings(val):
	list1 = [
		'Hello!',
		'Hey there!'
	]
	if val == True:
		print(type(list1))
		return rand_choice(list1)
	else:
		return None

