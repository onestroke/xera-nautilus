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
from misc_fn import first_entity_value, compare

from datetime import datetime



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
                'Yeah...',]
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
    
    if compare(loc,'xera')==True:
        print('running WithName(XERA)')
        context['WithName'] = greet_list1[0]
        if context.get('greeting') is not None:
            del context['greeting']
    elif compare(loc,'siri')==True:
        print('running WithName(SIRI)')
        context['WithName'] = 'Do I look like dumb blonde living in an overpriced phone?'
        if context.get('greeting') is not None:
            del context['greeting']
    elif compare(loc,'alexa')==True:
        print('running WithName(ALEXA)')
        context['WithName'] = 'I am neither mythical, savage, nor missing my right boob.'
        if context.get('greeting') is not None:
            del context['greeting']
    elif compare(loc,'cortana')==True:
        print('running WithName(CORTANA)')
        context['WithName'] = 'You need treatment John. That PTSD cant go on forever.'
        if context.get('greeting') is not None:
            del context['greeting']
    elif loc!= None and entities['contact'][0]['confidence']>=0.8:
        print('running WithName(Unrecognised Name)')
        context['WithName']='I am not '+ entities['contact'][0]['value'] +'. Hmmph!'
        if context.get('greeting') is not None:
            del context['greeting']
    else:
        print('running greeting')
        context['greeting'] = greet_list[0]
        if context.get('WithName') is not None:
            del context['WithName']

        
    return context
    
def getTime(request):
    context = request['context']
    entities = request['entities']
    context['time'] = str(datetime.now().strftime(%H:%M:%S'))
        
    return context
    
def getDate(request):
    context = request['context']
    entities = request['entities']
    context['date'] = str(datetime.now().strftime('%Y-%m-%d))
        
    return context
    






