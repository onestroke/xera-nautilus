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
from wit1 import Wit



#print(sys.argv)
#if len(sys.argv) != 2:
#    print('usage: python ' + sys.argv[0] + ' <wit-token>')
#    exit(1)

access_token = 'Q5DRP6ZSCTOFVZPEUVNP5OUICEY2K36C'

def test1():
    print('test1 working')
    return None

def wit_msg(sender_id,message_text):
    
    print('running wit msg')
    print('sender_id = '+ sender_id)
    print('message received = '+message_text)
        
    def send(request, response):
        # We use the fb_id as equal to session_id
        fb_id = request['session_id']
        text = response['text']
        # send message
        print('sending to send_message: '+text)
        send_message(fb_id,text)
        
    def send_message(recipient_id, message_text):
        print('sending to fb: '+ message_text)

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
        print('posting')
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
        #if r.status_code != 200:
            #log(r.status_code)
            #log(r.text)
        return None
        
    def first_entity_value(entities, entity):
        if entities['intent'][0]['value']==entity:
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
                    'Hmmph!',
                    'I have a name you know...',]
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
        
    
    actions = {
        'send': send,
        'getJoke': getJoke,
        'getForecast': getForecast,
        'getGreeting':getGreeting,
        'getID':getID,
    }
    print('actions =')
    print(actions)
    #client = Wit(access_token=access_token, actions=actions)
    client=Wit(access_token=access_token)
    #client.access_token=access_token
    client.actions=actions
    client.run_actions(session_id=sender_id, message=message_text)
    message_text=None
    #client.interactive()
    

    


