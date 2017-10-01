# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:25:04 2017

@author: alexr
"""
import json
from random import shuffle


def find_entity(entities, entity):
    """
    Returns first entity value
    """
    print('Running misc_fn.find_entity')

    # Return None is entity, entities are problematic
    if entity == None or entities == None:
        return None
    if entity not in entities:
        return None

    # Find value of entity detected
    val = entities[entity][0]['value']

    if val is None:
        return None

    if isinstance(val, dict):
        return val['value']
    else:
        return val

def find_confidence(entities, entity, val):
    """
    Finds the confidence of a given entity value
    """
    print('Running misc_fn.find_confidence')

    # Return None is entity, entities are problematic
    if entity == None or entities == None:
        return None
    if entity not in entities:
        return None

    # Find confidence of given entity value
    cfd = entities[entity][0]['confidence']

    if cfd is None:
        return None

    if isinstance(cfd, dict):
        return cfd['value']
    else:
        return cfd

def compare(str1, str2):
    """
    Compare 2 strings and determine if they are the same
    """

    # Ensures strings are lowercase
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
    if isinstance(list1, list):
        shuffle(list1)
        return list1[0]
    else:
        return 'Error, input needs to be a list.'