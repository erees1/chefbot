# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import db_fetch
import requests

# Link to database
db_api = db_fetch.API()


def send_option(dispatcher: CollectingDispatcher, tracker: Tracker):
    search_params = get_params(dispatcher, tracker)

    db_api.set_search_params(search_params)
    recipe = db_api.get_next_recipe()

    # Get the input channel so bot doesn't send something that cant be shown
    input_channel = tracker.get_latest_input_channel()

    if recipe is None:
        dispatcher.utter_message(template='utter_nomatches')
        sent = False
    elif recipe == 'End':
        dispatcher.utter_message(template='utter_no_more_matches')
        sent = False
    else:
        if input_channel == 'socketio':
            img_message = {
                "type": "image",
                "payload": {
                    "title": recipe['dish'],
                    "src": recipe['pic'],
                    "url": recipe['url']
                }
            }
        else:
            img_message = recipe['dish']
        dispatcher.utter_message(attachment=img_message)
        sent = True

    return sent


def send_ingredients(dispatcher: CollectingDispatcher, tracker: Tracker):
    recipe = db_api.get_current_recipe()

    ingredients = recipe['ingredients']
    ingredients = ingredients.replace('\n', ' \n - ')
    ingredients = ' - ' + ingredients
    dispatcher.utter_message(template='utter_ingredients_required')
    dispatcher.utter_message(text=ingredients)


def send_link(dispatcher: CollectingDispatcher, tracker: Tracker):
    recipe = db_api.get_current_recipe()
    input_channel = tracker.get_latest_input_channel()
    if input_channel == 'socketio':
        # message = {
        #     "type": "template",
        #     "payload": {
        #         "template_type":
        #         "generic",
        #         "elements": [{
        #             "title":
        #             "",
        #             "buttons": [{
        #                 "title": "Here is the link to the recipe",
        #                 "url": recipe['url']
        #             }]
        #         }]
        #     }
        # }
        # dispatcher.utter_message(attachment=message)

        message = (f"Here is the link to the full recipe: "
                   f"[{recipe['dish']}]({recipe['url']})")
        dispatcher.utter_message(text=message)
    else:
        dispatcher.utter_message(
            text=f'Here is the link to the full recipe {recipe["url"]}')


def get_params(dispatcher: CollectingDispatcher, tracker: Tracker):
    search_params = {
        'main': tracker.get_slot('main'),
        'dietary': tracker.get_slot('dietary'),
        'time2cook': tracker.get_slot('duration')
    }
    return search_params


def check_matches(dispatcher: CollectingDispatcher, tracker: Tracker, value,
                  slot):
    search_params = get_params(dispatcher, tracker)
    search_params[slot] = value
    if db_api.are_matches(search_params):
        # dispatcher.utter_message(template='utter_confirm')
        value = value
    else:
        if slot == 'main':
            dispatcher.utter_message(template='utter_no_main_match')
        elif slot == 'duration':
            dispatcher.utter_message(template='utter_no_time2cook_match')
        else:
            dispatcher.utter_message(template='utter_nomatches')
        value = None

    return value


class ActionSendOption(Action):
    def name(self) -> Text:
        return "action_send_option"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        send_option(dispatcher, tracker)

        return []


class ActionSendIngredients(Action):
    def name(self) -> Text:
        return "action_send_ingredients"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        send_ingredients(dispatcher, tracker)

        return []


class ResetMainSlot(Action):
    def name(self):
        return "action_reset_main_slot"

    def run(self, dispatcher, tracker, domain):
        print('Reseting main slot')
        return [SlotSet("main", None), SlotSet("satisfied", None)]


class ResetMainDurationSlots(Action):
    def name(self):
        return "action_reset_main_duration_slots"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("main", None),
            SlotSet("duration", None),
            SlotSet("satisfied", None)
        ]


class ResetDurationSlot(Action):
    def name(self):
        return "action_reset_duration_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("duration", None), SlotSet("satisfied", None)]


class ResetDietarySlot(Action):
    def name(self):
        return "action_reset_dietary_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("dietary", None), SlotSet("satisfied", None)]


class RestartAction(Action):
    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        # do something here

        return [Restarted()]


class ActionRetrieveUser(Action):
    def name(self) -> Text:
        return "action_retrieve_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.sender_id
        print('User ID retrieved:', user_id)

        # dispatcher.utter_message(f'Hello user: {user_id}')

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
            'main': [
                self.from_entity(entity='main'),
                self.from_intent(intent="deny", value=False),
                self.from_entity(entity='dietary'),
                self.from_text()
            ],
            'duration': [
                self.from_entity(entity='duration'),
            ],
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
        entities = tracker.latest_message['entities']
        print(entities)
        ent = {}
        for entity in entities:
            entity_name = entity['entity']
            if entity_name in ent:
                ent[entity_name].append(entity['value'])
            else:
                ent[entity_name] = [entity['value']]

        if 'dietary' in ent or 'duration' in ent and 'main' not in ent:
            value = False
        elif 'main' in ent:
            value = check_matches(dispatcher, tracker, ent['main'], 'main')
        else:
            value = check_matches(dispatcher, tracker, value, 'main')
        return {'main': value}

    def validate_dietary(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ):
        value = check_matches(dispatcher, tracker, value, 'dietary')
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
        print('validating time2cook on value', value)

        if isinstance(value, dict):
            # Then already been extracted
            norm_duration = value
        else:
            entities = tracker.latest_message['entities']

            # Get the entities extracted by both duckling and CRFExtractor
            ent = {e['extractor']: e for e in entities}
            if 'DucklingHTTPExtractor' in ent:
                # Then pull directly
                norm_duration = ent['DucklingHTTPExtractor'][
                    'additional_info']['normalized']
            else:
                # Ping the duckling server
                duration = ent['CRFEntityExtractor']['value']
                data = {'locale': 'en_GB', 'text': duration}
                # Run the duration for the duckling server
                response = requests.post('http://0.0.0.0:8000/parse',
                                         data=data)
                norm_duration = response.json()[0]['value']['normalized']

            norm_duration = check_matches(dispatcher, tracker, norm_duration,
                                          'time2cook')

        return {'duration': norm_duration}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,
               domain: Dict[Text, Any]):

        print('User preferences collected, submitting recipe form')
        db_api.reset_history()
        return [
            SlotSet("satisfied", False),
            SlotSet("change_main", None),
            SlotSet("change_duration", None),
            SlotSet("change_both", None)
        ]


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
                self.from_intent(intent="negative", value=False),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="postive", value=True)
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
            sent = send_option(dispatcher, tracker)
            if sent is False:
                value = False
            elif sent is True:
                value = None
        elif value is True:
            send_ingredients(dispatcher, tracker)
            send_link(dispatcher, tracker)

        return {'satisfied': value}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,
               domain: Dict[Text, Any]):
        return []
