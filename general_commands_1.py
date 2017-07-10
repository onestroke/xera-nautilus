# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:55:01 2017

@author: alexr
"""

import json
from random import shuffle

import requests
from flask import Flask, request

import sys
from wit2 import Wit
from misc_fn import first_entity_value, compare

#def template(request):
#    context = request['context']
#    entities = request['entities']
#    loc = first_entity_value(entities, 'template')
#    if loc:
#        context['template'] = 'template'
#        if context.get('template1') is not None:
#            del context['template1']
#    else:
#        context['template1'] = True
#        if context.get('template') is not None:
#            del context['template']
#    return context
    
def saveContact(request):
    context = request['context']
    entities = request['entities']
    loc = first_entity_value(entities, 'contact')
    if loc:
        context['template'] = 'template'
        if context.get('missingContact') is not None:
            del context['missingContact']
    else:
        context['missingContact'] = True
        if context.get('template') is not None:
            del context['template']
    return context
    
def sendMessage(request):
    context = request['context']
    entities = request['entities']
    loc = first_entity_value(entities, 'name')
    if loc:
        context['name'] = 'template'
        if context.get('template1') is not None:
            del context['template1']
    else:
        context['template1'] = True
        if context.get('template') is not None:
            del context['template']
    return context
    
