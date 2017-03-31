# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""
import os
import json
from random import shuffle

import requests
from flask import Flask, request

import sys
from wit2 import Wit

from general_interactions_1 import getGreeting



#print(sys.argv)
#if len(sys.argv) != 2:
#    print('usage: python ' + sys.argv[0] + ' <wit-token>')
#    exit(1)

access_token = 'UYXK6GEJCHUI4KNSGO2P6Z3CLZL2KZ7T'

def test1():
    print('master.py working')
    return None

def wit_msg(sender_id,message_text):
    
    print('Running wit_msg in master.py')
    print('Sender_id = '+ sender_id)
    print('Message received = ' + message_text)
        
    def send(request, response):
        # We use the fb_id as equal to session_id
        print('Reponse to be sent= ')
        
        fb_id = request['session_id']
        text = response['text']
        print(text)
        # send message
        print('Sending to send_message: '+text)
        send_message(fb_id,text)
        
    def send_message(recipient_id, message_text):
        print('Sending to fb: '+ message_text)
    
        #log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))
    
        params = {
            "access_token": os.environ["PAGE_ACCESS_TOKEN"]
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        print('Posting to messenger now...')
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
        #if r.status_code != 200:
            #log(r.status_code)
            #log(r.text)
        return None
        
    def first_entity_value(entities, entity):
        if entities==None:
            return None
        elif entities['intent'][0]['value']==entity:
            return True
        else:
            return None
    
    def getJoke(request):
    #    context = request['context']
    #    entities = request['entities']
       # 
       #     print(context)
       #     print(entities)
       # 
       #     print('you are a joke haha')
       # 
        return context
        
    def getForecast(request):
        context = request['context']
        entities = request['entities']
    
    
        loc = first_entity_value(entities, 'location')
        if loc:
            context['forecast'] = 'sunny'
            if context.get('missingLocation') is not None:
                del context['missingLocation']
        else:
            context['missingLocation'] = True
            if context.get('forecast') is not None:
                del context['forecast']
    
        return context
        
    
        
    def getID(requests):
        print('running getID')
        context = request['context']
        entities = request['entities']


        
        
        
        return context
        
    
    actions = {
        'send': send,
        'getJoke': getJoke,
        'getForecast': getForecast,
        'getGreeting':getGreeting,
        'getID':getID,
    }
    print('Complete set of actions = ')
    print(actions)
    #client = Wit(access_token=access_token, actions=actions)
    client=Wit(access_token=access_token)
    #client.access_token=access_token
    client.actions=actions
    
    client.run_actions(session_id=sender_id, message=message_text)
    message_text=None
    
    #client.interactive()
    

    


