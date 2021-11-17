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

class action_crear_agilebot(Action):

    def name(self):
        return "action_crear_agilebot"

    def run(self, dispatcher, tracker, domain, ): # tracker lleva el historial, todo. # dispacher manda mensajes al user # domain es el dominio del agente
        dispatcher.utter_message("[INFO] creando agilebot")     # hay dos trackers distintos. from rasa_sdk import Action, Tracker
      
        exchanges_nuevos = tracker.get_slots('exchanges')
        #  name = tracker.get_slot("name")

        return []
