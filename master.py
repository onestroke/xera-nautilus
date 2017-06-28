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

from general_interactions_1 import test2, getGreeting, getForecast, getTime, getDate
#from general_commands_1 import
from misc_fn import dump, load


#print(sys.argv)
#if len(sys.argv) != 2:
#    print('usage: python ' + sys.argv[0] + ' <wit-token>')
#    exit(1)

access_token = 'GQNHRLJQB5OUUU4ZRZCWCP2MRHJGFTDG'

def test1():
    """Show that app.py can call master.py"""
    
    print('master.py working')
    return None

def wit_msg(sender_id,message_text):
    """Function called by app.py. From FB_ID of sender and message received, 
    sends responses to FB"""
    
    print('Running wit_msg in master.py')
    print('Sender_id = '+ sender_id)
    print(type(sender_id))
    print('Message received = ' + message_text)
    
    print('appending to logs.txt')
    try: logs = load('logs.txt')
    except ValueError:
        logs = []
    if logs == None:
        logs = []
    logs.append((sender_id,message_text))
    dump(logs,'logs.txt')
    
    def log(message):  # simple wrapper for logging to stdout on heroku
        print(str(message))
        sys.stdout.flush()
        
    def getFullTest(request):
        context = request['context']
        entities = request['entities']
        #fd = load('FullDiagnostic.txt')
        #print(fd)
        #for entry in fd:
        #    entry=str(entry)
        #    wit_msg(1117609775034736,entry)
        context['results'] = 'pass'
        return context     
    def send(request, response):
        """Sends response to FB"""
        
        # We use the fb_id as equal to session_id
        print('Reponse to be sent= ')
        
        fb_id = request['session_id']
        text = response['text']
        print(text)
        
        # send message
        print('Sending to send_message: '+text)
        send_message(fb_id,text)
        
    def send_message(recipient_id, message_text):
        """Sends response to FB"""
        
        print('Sending to fb: '+ message_text)
    
        log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))
    
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
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)
        return None
        
    

    # Setup Actions
    actions = {
        'send': send,
        'getForecast': getForecast,
        'getGreeting': getGreeting,
        'test2': test2,
        'getTime': getTime,
        'getDate': getDate,
        'getFullTest': getFullTest,
    }
    print('Complete set of actions = ')
    print(actions)
    #client = Wit(access_token=access_token, actions=actions)
    client=Wit(access_token=access_token)
    #client.access_token=access_token
    client.actions=actions
    print('reading from logs.txt')
    file = open('logs.txt','r') 
    print(file.read())
    file.close
    print(message_text)
    resp1=client.message(message_text)
    print(resp1)
    client.run_actions(session_id=sender_id, message=message_text)
    message_text=None
    
    #client.interactive()
    

    


