# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

LOCALHOST = "localhost"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import addresses
import json
import requests

class action_send_message(Action):
    def name(self):
        return "action_send_message"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
             # hay dos trackers distintos. from rasa_sdk import Action, Tracker
    
        agilebot = tracker.slots.get("agilebot")
        activity_name = tracker.slots.get("activity")
        parameters = tracker.slots.get("parametro")
        intent = tracker.latest_message['intent'].get('name')

        dispatcher.utter_message(intent + "®" + agilebot + "®" + activity_name + "®" + parameters)
        return []

class action_create_agilebot(Action):

    def name(self):
        return "action_create_agilebot"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
             # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("rol")
        mode = tracker.slots.get("modo_agilebot")
        intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(intent + "®" + agilebot + "®" + rol + "®" + mode)
        return []

class action_change_agilebot_role(Action):

    def name(self):
        return "action_change_agilebot_role"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("rol")  
        dispatcher.utter_message(intent + "®" + agilebot + "®" + rol)
        return []


class action_change_agilebot_mode(Action):

    def name(self):
        return "action_change_agilebot_mode"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] cambiando modo de agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        agilebot = tracker.slots.get("agilebot")
        mode = tracker.slots.get("modo_agilebot")  
        dispatcher.utter_message(intent + "®" + agilebot + "®" + mode)
        return []

class action_create_exchange(Action):

    def name(self):
        return "action_create_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        exchange = tracker.slots.get("exchange")
        intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(intent+"®"+ exchange)     
        return []

class action_remove_exchange(Action):

    def name(self):
        return "action_remove_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        exchange = tracker.slots.get("exchange")
        intent = tracker.latest_message['intent'].get('name')

        dispatcher.utter_message(intent+"®"+ exchange)     
        return []

# class action_post_event(Action):
    
#     def name(self):
#         return "action_post_event"
    
#     def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
#         dispatcher.utter_message("[INFO] Posteando un evento") 
    
#         parameters = tracker.slots.get("activity")
#         exchanges = tracker.slots.get("parametro") 

#         json_datos = {"exchange": exchanges; "parameters": parameters}
#         requests.post(url="http://"+ LOCALHOST  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/post-event", json=json_datos)        

#         return[]

class action_change_callback(Action):
        
    def name(self):
        return "action_change_callback"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Cambiando el callback de un agilebot") 
        
        nombre = tracker.slots.get("agilebot") 
        method = tracker.slots.get("metodo")
        exchanges = tracker.slots.get("exchange") 
        intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(intent+"®"+ exchange+"®"+agilebot+"®"+activity)     

        return[]      

class action_remove_agilebot_from_all(Action):
            
    def name(self):
        return "action_remove_agilebot_from_all"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
     #- quiero remover [franraineri](agilebot) de todos los exchanges
        nombre = tracker.slots.get("agilebot") 
        intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(intent+"®"+nombre)     
        return[]      

class action_remove_agilebot_from_some(Action):
            
    def name(self):
        return "action_remove_agilebot_from_some"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        nombre = tracker.slots.get("agilebot") 
        exchanges = tracker.slots.get("exchange") 
        intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(intent+"®"+nombre+"®"+ exchanges)     
        return[]         

class action_add_exchange_subscriber(Action):
            
    def name(self):
        return "action_add_exchange_subscriber"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        nombre = tracker.slots.get("agilebot") 
        exchange = tracker.slots.get("exchange")
        actividad = tracker.slots.get("activity") 
        intent = tracker.latest_message['intent'].get('name')

        dispatcher.utter_message(intent+"®"+ exchange+"®"+nombre+"®"+actividad)     
        return[]          

class action_remove_all_subscribers(Action):

    def name(self):
        return "action_remove_all_subscribers"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        exchange = tracker.slots.get("exchange")
        intent = tracker.latest_message['intent'].get('name')
        dispatcher.utter_message(intent+"®"+ exchange)     
        return[]          