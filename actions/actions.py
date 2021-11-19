# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from agiletalk.src.mundo_sintetico.user_defined import addresses
import json
import requests

class action_send_message(Action):
    def name(self):
        return "action_send_message"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] enviando un mensaje")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
    
        agilebot = tracker.slots.get("agilebot")
        activity_name = tracker.slots.get("activity")
        
        #send_message(agilebot, activity_name: string, parameters: Dict)
        #¿Cual es el diccionario a enviar en este caso?

        return []

class action_create_agilebot(Action):

    def name(self):
        return "action_create_agilebot"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] creando agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")
        mode = tracker.slots.get("mode")

        json_datos = {"agilebotId":  str(agilebot), "role": str(rol), "mode": str(mode)}
        print(requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/create-agilebot", json=json_datos))

        return []

class action_change_agilebot_role(Action):

    def name(self):
        return "action_change_agilebot_role"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] cambiando rol de agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")  
        json_datos = {"agilebotId": str(agilebot), "role": str(rol)}
        requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/change-agilebot-role", json=json_datos)



class action_change_agilebot_mode(Action):

    def name(self):
        return "action_change_agilebot_mode"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] cambiando modo de agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
      
        agilebot = tracker.slots.get("agilebot")
        mode = tracker.slots.get("mode")  
        json_datos = {"agilebotId": str(agilebot), "role": str(mode)}
        requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/change-agilebot-mode", json=json_datos)        
        return []

class action_create_exchange(Action):

    def name(self):
        return "action_create_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Agregando un Exchange")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker

        exchange = tracker.slots.get("exchange")
        json_datos = {"exchange": str(exchange)}
        requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/create-exchange", json=json_datos)        
        return []

class action_remove_exchange(Action):

    def name(self):
        return "action_remove_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Eliminando un Exchange")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        exchange = tracker.slots.get("exchange")
        json_datos = {"exchange": str(exchange)}
        requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/remove-exchange", json=json_datos)        

        return []


class action_all_suscribers(Action):

    def name(self):
        return "action_all_suscribers"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Quitando todos los subscriptores a un Exchange.") 
        
        exchange = tracker.slots.get("exchange")
        json_datos = {"exchange": str(exchange)}
        #requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/action-all-suscribers", json=json_datos)        

        return[]



class action_remove_agilebot_from_all(Action):

    def name(self):
        return "action_remove_agilebot_from_all"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Eliminando un agilebot de todos los exchanges") 
        
        nombre = tracker.slots.get("agilebot")
        json_datos = {"agilebotId": str(nombre)}
        #requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/remove-agilebot-from-all", json=json_datos)        
        
        return[]


class action_remove_agilebot_from_some(Action):

    def name(self):
        return "action_remove_agilebot_from_some"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Eliminando un agilebot de algunos los exchanges") 
        
        nombre = tracker.slots.get("agilebot") 
        exchanges = tracker.slots.get("exchange") #Como se trata esto?
        exchanges = exchanges.split(",")

        #json_datos = {"agilebotId": str(nombre), "exchange": exchanges}
        #requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/remove-agilebot-from-some", json=json_datos)        

        return[]


class action_add_exchange_subscriber(Action):

    def name(self):
        return "action_add_exchange_subscriber"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Agregando subscriptores haci") 
        
        nombre = tracker.slots.get("agilebot") 
        activity = tracker.slots.get("activity")
        exchanges = tracker.slots.get("exchange") 

        #json_datos = {"agilebotId": str(nombre), "exchange": exchanges}
        #requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/remove-agilebot-from-some", json=json_datos)        

        return[]

class action_publish_exchange(Action):
    
    def name(self):
        return "action_publish_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] ") 
        
        nombre = tracker.slots.get("agilebot") 
        activity = tracker.slots.get("activity")
        exchanges = tracker.slots.get("exchange") 

        #json_datos = {"agilebotId": str(nombre), "exchange": exchanges}
        #requests.post(url="http://"+ str(addresses.FLASK_HOST)  + ":" + str(addresses.FLASK_PORT) + "/dispatcher/create-exchange", json=json_datos)        

        return[]

"""
+ publish(exchange_name: string, parameters: Dict  || List<Subscribers> , n  ):string
- intent: publish_exchange
  examples: |     #que hago con los parametros ?
    - publicar [move_to_done](exchange) con los parametros 
    - publicá el exchange [move_to_done](exchange) con los parametros 
"""