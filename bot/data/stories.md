## bot challenge
* bot_challenge
  - utter_iamabot

# happy path 1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
    - recipe_form
    - form{"name": "recipe_form"}
    - form{"name": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - form{"name": null}
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_reset_all_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* request_recipe
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "chicken"}
    - form: recipe_form
    - slot{"main": "chicken"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "time2cook"}
* form: inform{"duration_text": "25 mins", "duration": 25}
    - form: recipe_form
    - slot{"time2cook": 1500}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_search_again
* affirm
    - action_reset_main_slot
    - slot{"main": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"dietary": false}
    - slot{"time2cook": 1500}
    - slot{"requested_slot": "main"}
* form: inform{"main": "beef"}
    - form: recipe_form
    - slot{"main": "beef"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: affirm
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_reset_all_slots
    - slot{"main": null}
    - slot{"time2cook": null}
    - slot{"satisfied": null}
    - action_restart


## interactive_story_2
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "beef"}
    - form: recipe_form
    - slot{"main": "beef"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "time2cook"}
* form: inform{"duration_text": "25 mins", "duration": 25}
    - form: recipe_form
    - slot{"time2cook": 1500}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: affirm
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_reset_all_slots
    - slot{"main": null}
    - slot{"time2cook": null}
    - slot{"satisfied": null}
    - action_restart
