# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 01:25:04 2017

@author: alexr
"""

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

