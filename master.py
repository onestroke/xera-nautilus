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
        print('sending to app.py: '+text)
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
        
        context['forecast']="sunny"
        print('getForecast returns = ')
        print(context)
        print(entities)
        
        return context
        
    def getGreeting(request):
        context = request['context']
        entities = request['entities']
        
        greet_list=['Hello!',
                    'Xera is at your service.',
                    'At your service.',
                    'Yes?',
                    'Greetings!',
                    'I am listening...',
                    'Listening.',
                    'I read you',
                    'Reading you loud and clear.',]
        shuffle(greet_list)
        context['greeting'] = greet_list[0]

        return context
        
    
    actions = {
        'send': send,
        'getJoke': getJoke,
        'getForecast': getForecast,
        'getGreeting':getGreeting,
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
    

    


