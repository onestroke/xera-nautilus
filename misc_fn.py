# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:25:04 2017

@author: alexr
"""
import json
from random import shuffle


def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity == None or entities == None:
        return None
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    print('running first_entity_value')
    print('val = ' + val)
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def compare(str1, str2):
    """
    Compare 2 strings and determine if they are the same
    """
    str1 = str(str1)
    str2 = str(str2)
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return True
    else:
        return False

def dump(data, filename):
    """
    Save JSON object to file
    """
    with open(filename, 'w') as f:
        data = json.dump(data, f)


def load(filename):
    """
    Load JSON object from file
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data

def rand_choice(list1):
    """
    Chooses an item randomly from a list
    """
    print(type(list1))
    if type(list1) is list:
        shuffle(list1)
        return list1[0]
    else:
        return 'Error, input needs to be a list'