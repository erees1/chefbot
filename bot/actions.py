# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import db_fetch

# Link to database
db_api = db_fetch.API()


def send_option(dispatcher: CollectingDispatcher, tracker: Tracker):
    search_params = {
        'main': tracker.get_slot('main'),
        'dietary': tracker.get_slot('dietary'),
        'duration': tracker.get_slot('duration')
    }

    db_api.set_search_params(search_params)
    recipe = db_api.get_next_recipe()

    if recipe is None:
        dispatcher.utter_message(text='No matches')
    else:
        img_message = {
            "type": "image",
            "payload": {
                "title": recipe['dish'],
                "src": recipe['pic'],
                "url": recipe['url']
            }
        }
        dispatcher.utter_message(attachment=img_message)

    return []


def send_ingredients(dispatcher: CollectingDispatcher, tracker: Tracker):
    recipe = db_api.get_current_recipe()

    dispatcher.utter_message(template='utter_ingredients_required')
    dispatcher.utter_message(text=f"{recipe['ingredients']}")


class ActionRetrieveUser(Action):
    def name(self) -> Text:
        return "action_retrieve_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.sender_id
        print(user_id)

        dispatcher.utter_message(f'Hello user: {user_id}')

        return []


class RecipeForm(FormAction):
    def name(self) -> Text:
        return "recipe_form"

    @staticmethod
    def required_slots(tracker: Tracker):
        '''List of slots bot needs to fill'''
        return ['main', 'dietary', 'duration']

    def slot_mappings(self):
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        mappings = {
            'main': [self.from_entity(entity='main'),
                     self.from_text()],
            'duration':
            [self.from_entity(entity='duration'),
             self.from_text()],
            'dietary': [
                self.from_entity(entity='dietary'),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="affirm", value=True)
            ],
        }

        return mappings

    def validate_main(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ):

        return {'main': value}

    def validate_dietary(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ):
        return {'dietary': value}

    def validate_duration(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ):
        '''
        Extract the entity using the Duckling extractor
        '''
        entities = tracker.latest_message['entities']
        extracted_by_duckling = [
            e for e in entities if e['entity'] == 'duration'
            and e['extractor'] == 'DucklingHTTPExtractor'
        ]
        try:
            norm_duration = extracted_by_duckling[0]['additional_info'][
                'normalized']['value']
        except Exception:
            norm_duration = value
        return {'duration': norm_duration}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,
               domain: Dict[Text, Any]):
        print('Submitting form')
        dispatcher.utter_message(template='utter_submit')
        send_option(dispatcher, tracker)
        return []


class SatisfiedForm(FormAction):
    def name(self) -> Text:
        return "satisfied_form"

    @staticmethod
    def required_slots(tracker: Tracker):
        '''List of slots bot needs to fill'''
        return ['satisfied']

    def slot_mappings(self):
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        mappings = {
            'satisfied': [
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="affirm", value=True)
            ]
        }

        return mappings

    def validate_satisfied(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ):
        if value is False:
            send_option(dispatcher, tracker)
            value = None

        if value is True:
            send_ingredients(dispatcher, tracker)
            value = True

        return {'satisfied': value}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,
               domain: Dict[Text, Any]):
        return []
