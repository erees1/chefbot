## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_4
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
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
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 1}
    - form: recipe_form
    - slot{"duration": 3600}
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
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "pasta"}
    - form: recipe_form
    - slot{"main": "pasta"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration_text": "30 minutes", "duration": 30}
    - form: recipe_form
    - slot{"duration": 1800}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: postive
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* deny
    - utter_goodbye_neutral
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "rice"}
    - form: recipe_form
    - slot{"main": "rice"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration_text": "30 mins", "duration": 30}
    - form: recipe_form
    - slot{"duration": 1800}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
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
* form: affirm
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_restart

## interactive_story_1
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
    - slot{"requested_slot": "duration"}
* form: inform{"duration_text": "25 mins", "duration": 25}
    - form: recipe_form
    - slot{"duration": 1500}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
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
    - action_reset_main_duration_slots
    - slot{"main": null}
    - slot{"duration": null}
    - slot{"satisfied": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"dietary": false}
    - slot{"requested_slot": "main"}
* form: inform{"main": "chicken"}
    - form: recipe_form
    - slot{"main": "chicken"}
    - slot{"requested_slot": "duration"}
* form: inform{"duration_text": "30 mins", "duration": 30}
    - form: recipe_form
    - slot{"duration": 1800}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: affirm
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye

## interactive_story_1
* request_recipe{"duration": 20}
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "rice"}
    - form: recipe_form
    - slot{"main": "rice"}
    - slot{"requested_slot": "dietary"}
* form: inform_dietary{"dietary": "vegeterian"}
    - form: recipe_form
    - slot{"dietary": "vegeterian"}
    - slot{"requested_slot": "duration"}
* form: inform{"duration_text": "20 mins", "duration": 20}
    - form: recipe_form
    - slot{"duration": 1200}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: affirm
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* request_recipe{"main": "rice"}
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"main": "rice"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 1}
    - form: recipe_form
    - slot{"duration": 3600}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: postive
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_restart

## interactive_story_1
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
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 45}
    - form: recipe_form
    - slot{"duration": {"value": 2700, "unit": "second"}}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: deny
    - form: satisfied_form
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* change_choices
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_which_slot_to_change
* change_choices{"change_main": "ingredients"}
    - action_reset_main_slot
    - slot{"main": null}
    - slot{"satisfied": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - action_listen
    - slot{"dietary": false}
    - slot{"duration": {"value": 2700, "unit": "second"}}
    - slot{"requested_slot": "main"}
* form: inform{"main": "chicken"}
    - recipe_form
    - slot{"main": "chicken"}
    - slot{"satisfied": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: postive
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "rice"}
    - form: recipe_form
    - slot{"main": "rice"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 40}
    - form: recipe_form
    - slot{"duration": {"value": 2400, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* change_choices
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_which_slot_to_change
* change_choices{"change_duration": "time"}
    - action_reset_duration_slot
    - slot{"duration": null}
    - slot{"satisfied": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - action_listen
    - slot{"main": "rice"}
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 30}
    - recipe_form
    - slot{"duration": {"value": 1800, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
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
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* request_recipe{"main": "chicken"}
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"main": "chicken"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 40}
    - form: recipe_form
    - slot{"duration": {"value": 2400, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* change_choices
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_which_slot_to_change
* change_choices{"change_both": "both"}
    - action_reset_main_duration_slots
    - slot{"main": null}
    - slot{"duration": null}
    - slot{"satisfied": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - action_listen
    - slot{"dietary": false}
    - slot{"requested_slot": "main"}
* form: inform{"main": "rice"}
    - recipe_form
    - slot{"main": "rice"}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 45}
    - form: recipe_form
    - slot{"duration": {"value": 2700, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
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
    - action_restart

## interactive_story_1
* greet
    - utter_greet
    - action_retrieve_user
    - utter_should_bot_get_recipe
* affirm
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"requested_slot": "main"}
* form: inform{"main": "rice"}
    - form: recipe_form
    - slot{"main": "rice"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 40}
    - form: recipe_form
    - slot{"duration": {"value": 2400, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* change_choices
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_which_slot_to_change
* change_choices{"change_both": "both"}
    - action_reset_main_duration_slots
    - slot{"main": null}
    - slot{"duration": null}
    - slot{"satisfied": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - action_listen
    - slot{"dietary": false}
    - slot{"requested_slot": "main"}
* form: inform{"main": "noodles"}
    - recipe_form
    - slot{"main": "noodles"}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 90}
    - recipe_form
    - form{"name": "recipe_form"}
    - slot{"main": false}
    - slot{"dietary": false}
    - slot{"duration": {"value": 5400, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* form: postive
    - form: satisfied_form
    - slot{"satisfied": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_happy_goodbye
    - action_restart

## interactive_story_1
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
* form: change_choices{"main": "chicken"}
    - form: recipe_form
    - slot{"main": "chicken"}
    - slot{"requested_slot": "dietary"}
* form: deny
    - form: recipe_form
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 1}
    - form: recipe_form
    - slot{"duration": {"value": 3600, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - slot{"satisfied": null}
    - slot{"requested_slot": "satisfied"}
* change_choices
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_which_slot_to_change
* change_choices{"change_duration": "time"}
    - action_reset_duration_slot
    - slot{"duration": null}
    - slot{"satisfied": null}
    - recipe_form
    - form{"name": "recipe_form"}
    - action_listen
    - slot{"main": "chicken"}
    - slot{"dietary": false}
    - slot{"requested_slot": "duration"}
* form: inform{"duration": 90}
    - recipe_form
    - slot{"duration": {"value": 5400, "unit": "second"}}
    - slot{"satisfied": false}
    - slot{"change_main": null}
    - slot{"change_duration": null}
    - slot{"change_both": null}
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
    - action_restart
