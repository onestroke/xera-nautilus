# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:44:51 2017

@author: alexr
"""

import json
from random import shuffle

import requests
from flask import Flask, request

import sys
from wit2 import Wit

def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity == None or entities == None:
        return None
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def test2(request):

    print('Running test2')
    context = request['context']
    entities = request['entities']
    print('entities = ')
    print(entities)
    print('context = ')
    print(context)
    
    return context
    
def getForecast(request):
    context = request['context']
    entities = request['entities']
    loc = first_entity_value(entities, 'location')
    if loc:
        # This is where we could use a weather service api to get the weather.
        context['forecast'] = 'sunny'
        if context.get('missingLocation') is not None:
            del context['missingLocation']
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']
    return context

def getGreeting(request):

    print('Running getGreeting')
    context = request['context']
    entities = request['entities']
    print('entities = ')
    print(entities)
    print('context = ')
    print(context)
    
    greet_list=['Hello...',
                'Yes...',
                '...(Insert standard greeting)',
                'I can hear you...',
                'Listening...',
                'I hear you...',
                'Hmmph!',]
    shuffle(greet_list)
    
    greet_list1=['Xera hears you!',
                 'Xera is at your service.',
                 'I am at your service.',
                 'Yes?',
                 'Xera is ready!',
                 'I am ready!',
                 'Xera sees you, and is happy to assist.',
                 'It would be an honour to assist you.',]
    shuffle(greet_list1)
    
    loc = first_entity_value(entities, 'contact')
    
    if loc=='xera':
        print('running WithName')
        context['WithName'] = greet_list1[0]
        if context.get('greeting') is not None:
            del context['greeting']
    else:
        print('running standard greeting')
        context['greeting'] = greet_list[0]
        if context.get('WithName') is not None:
            del context['WithName']

        
    return context
    

    






