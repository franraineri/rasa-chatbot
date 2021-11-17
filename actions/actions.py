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
        """  
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")
        mode = tracker.slots.get("mode")

        create_agilebot(agilebot, rol, mode)
        """
        return []

class action_cambiar_rol_agilebot(Action):

    def name(self):
        return "action_cambiar_rol_agilebot"

    def run(self, dispatcher, tracker, domain): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] cambiadno rol de agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
        """  
        agilebot = tracker.slots.get("agilebot")
        rol = tracker.slots.get("role")

        change_agilebot_role(agilebo, rol)
        """
        return []

