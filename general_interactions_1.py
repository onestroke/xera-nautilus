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
from wit1 import Wit

def first_entity_value(entities, entity):
        if entities==None:
            return None
        elif entities['intent'][0]['value']==entity:
            return True
        else:
            return None

def getGreeting(request):
    print('running greeting')
    context = request['context']
    entities = request['entities']
    print('######################################################')
    print('entities = ')
    print(entities)
    print('######################################################')
    
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
    
    loc1 = first_entity_value(entities, 'siri')
    loc2 = first_entity_value(entities, 'alexa')
    loc3 = first_entity_value(entities, 'cortana')
    loc4 = first_entity_value(entities, 'xera')
   
    
    if loc1 or loc2 or loc3:
        print('running otherbot')
        context['otherbot'] = True
        if context.get('greeting') is not None:
            del context['greeting']
    elif loc4:
        print('running xera')
        context['greeting'] = greet_list1[0]
    else:
        print('running standard greeting')
        context['greeting'] = greet_list[0]
        if context.get('otherbot') is not None:
            del context['otherbot']
        
    return context
        
def getID(requests):
    print('running getID')
    context = request['context']
    entities = request['entities']
  
    return context