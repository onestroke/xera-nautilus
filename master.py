# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:19 2017

@author: alexr
"""
import sys
from wit1 import Wit
print('i fucking imported from wit1 idiots')


#print(sys.argv)
#if len(sys.argv) != 2:
#    print('usage: python ' + sys.argv[0] + ' <wit-token>')
#    exit(1)

access_token = 'Q5DRP6ZSCTOFVZPEUVNP5OUICEY2K36C'

def test1():
    print('test1 working')
    return None

#def wit_msg(sender_id,message_text):
    
    
def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    # We use the fb_id as equal to session_id
    fb_id = request['session_id']
    text = response['text']
    # send message
    print(text)
    handle.send_message(fb_id, text)

def getJoke(request):
    context = request['context']
    entities = request['entities']

    print(context)
    print(entities)

    print('you are a joke haha')

    return context
    
def getForecast(request):
    context = request['context']
    entities = request['entities']
    
    print(context)
    print(entities)
    
    print('It should be sunny today!')
    
    return context
    

actions = {
    'send': send,
    'getJoke': getJoke,
    'getForecast': getForecast,
}
print(actions)
#client = Wit(access_token=access_token, actions=actions)
client=Wit(access_token=access_token)
#client.access_token=access_token
client.actions=actions
#client.run_actions(session_id=sender_id, message=message_text)
client.interactive()
    

    


