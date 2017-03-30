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

def find_entity(entities, entity):
    print('running f_e_v')
    if entities==None:
        print('return none')
        return None
    elif entities[entity][0]['value']!=None:
        value=entities[entity][0]['value']
        print('return '+value)
        return value
    else:
        print('return none')
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
        
def getID(requests):
    print('running getID')
    context = request['context']
    entities = request['entities']
  
    return context