# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 03:06:07 2017

@author: alexr
"""

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

from general_interactions_1 import getGreeting, getForecast, test2



#print(sys.argv)
#if len(sys.argv) != 2:
#    print('usage: python ' + sys.argv[0] + ' <wit-token>')
#    exit(1)

access_token = 'GQNHRLJQB5OUUU4ZRZCWCP2MRHJGFTDG'


    
print('Running wit_msg in master.py')

    
def send(request, response):
    # We use the fb_id as equal to session_id
    print('Reponse to be sent= ')
    
    fb_id = request['session_id']
    text = response['text']
    text=str(text)
    print(text)
    # send message
    
    #send_message(fb_id,text)
    
def send_message(recipient_id, message_text):
    print('Sending to fb: '+ message_text)

    #log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": 'EAAawB7MZBDtoBAHVf6TZBhP4094v4m4GwoUI5PsojqvCPNf0EaNgre4okMq1y2yXCC8BxufC15ADVZBHJd62Rwvxmq9VckImAtQwZAnUsxFGdTTf3OLMg7REFm3j2PM9ZANFQu4h9J09UnzhZBySvdxZAb8KEO1dZAhz4Bcj8NZAMvQZDZD'
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
    


# Setup Actions
actions = {
    'send': send,
    'getForecast': getForecast,
    'getGreeting': getGreeting,
    'test2': test2,
}
print('Complete set of actions = ')
print(actions)
#client = Wit(access_token=access_token, actions=actions)
client=Wit(access_token=access_token)
#client.access_token=access_token
client.actions=actions


sender_id='1117609775034736'
message_text='What is the weather in Rome?'

#client.converse(session_id=sender_id, message=message_text,context={})
client.run_actions(session_id=sender_id, message=message_text, context={})
#client.interactive()
    

    


