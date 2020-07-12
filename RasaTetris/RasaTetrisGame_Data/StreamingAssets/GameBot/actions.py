# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.domain import Domain


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        domain = Domain.load("domain.yml")
       
          
        d = str(domain.intents)
        dispatcher.utter_message(json_message=d)
        
        # print("Intent_Ranking", tracker.latest_message['intent_ranking'])
        
        a = str(tracker.latest_message['intent_ranking'])
        dispatcher.utter_message(json_message=a)
       
        return []
