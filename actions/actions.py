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
import json

class action_enviar_un_mensaje(Action):
    def name(self):
        return "action_enviar_un_mensaje"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] enviando un mensaje")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        """  
        agilebot = tracker.slots.get("agilebot")
        activity_name = tracker.slots.get("activity")
        
        send_message(agilebot, activity_name: string, parameters: Dict)
        #¿Cual es el diccionario a enviar en este caso?
        """
        return []

class action_crear_agilebot(Action):

    def name(self):
        return "action_crear_agilebot"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] creando agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")
        mode = tracker.slots.get("mode")

        json_datos = {"agilebotId": agilebot, "role": rol, "mode": mode}
        
        #Falta el pusheo en el Postman

        return []

class action_cambiar_rol_agilebot(Action):

    def name(self):
        return "action_cambiar_rol_agilebot"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] cambiando rol de agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        """
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")  
        json_datos = {"agilebotId": agilebot, "role": rol}

        ##Esto es correcto? Necesito saber si el push reemplaza o como es que se hace.
         """
        return []


class action_cambiar_modo_agilebot(Action):

    def name(self):
        return "action_cambiar_modo_agilebot"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] cambiando modo de agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        """
        
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")  
        json_datos = {"agilebotId": agilebot, "role": rol}
        ##Esto es correcto? Necesito saber si el push reemplaza o como es que se hace.
        """
        return []


# + add_exchange(exchange:string):string

class action_add_exchange(Action):

    def name(self):
        return "action_add_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Agregando un Exchange")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        """
        
        exchange = tracker.slots.get("exchange")
        json_datos = {"exchange": exchange}
        ##Falta la subida al postman
        """

        return []

class action_remove_exchange(Action):

    def name(self):
        return "action_remove_exchange"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Eliminando un Exchange")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        """
        exchange = tracker.slots.get("exchange")
        json_datos = {"exchange": exchange}
        ##Falta la subida al postman
        """

        return []


class action_all_suscribers(Action):

    def name(self):
        return "action_all_suscribers"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Quitando todos los subscriptores a un Exchange.") 
        """
        exchange = tracker.slots.get("exchange")
        json_datos = {"exchange": exchange}
        ##Falta la subida al postman
        """

        return[]



class action_remove_agilebot_from_all(Action):

    def name(self):
        return "action_remove_agilebot_from_all"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Eliminando un agile bot de todos los exchanges") 
        """
        nombre = tracker.slots.get("agilebot")
        json_datos = {"agilebotId": nombre}
        ##Falta la subida al postman
        """

        return[]


class action_remove_agilebot_from_some(Action):

    def name(self):
        return "action_remove_agilebot_from_some"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Eliminando un agile bot de algunos los exchanges") 
        
        """
        nombre = tracker.slots.get("agilebot") 

        LISTADEEXCHANGES = tracker.slots.get("exchange") #Como se trata esto?
        json_datos = {"agilebotId": nombre, COMO LE PASO UNA LISTA U OTRO JSON?}
        ##Falta la subida al postman
        """

        return[]


class action_add_subscriber(Action):

    def name(self):
        return "action_add_subscriber"
    
    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] Agregando subscriptores haci") 
        
        """
        nombre = tracker.slots.get("agilebot") 

        LISTADEEXCHANGES = tracker.slots.get("exchange") #Como se trata esto?
        json_datos = {"agilebotId": nombre, COMO LE PASO UNA LISTA U OTRO JSON?}
        ##Falta la subida al postman
        """

        return[]


"""
# + add_subscriber(exchange_name:str, agilebot: Agilebot, activity_name:string):string
- intent: add_exchange_subscriber
  examples: |
    - subscribir a [franraineri](agilebot) a [move_to_done](exchange) con la actividad [move_to_done](activity)


# + publish(exchange_name: string, parameters: Dict  || List<Subscribers> , n  ):string
- intent: publish_exchange
  examples: |     #que hago con los parametros ?
    - publicar [move_to_done](exchange) con los parametros 
    - publicá el exchange [move_to_done](exchange) con los parametros 
"""