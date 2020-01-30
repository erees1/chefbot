## bot challenge
* bot_challenge
  - utter_iamabot

# happy path 1
* greet
    - utter_greet
    - action_retrieve_user
* request_recipe
    - recipe_form
    - form{"name": "recipe_form"}
    - form{"name": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - form{"name": null}
    - slot{"satisfied": true}
    - utter_happy_goodbye

## happy path 2
* greet
    - utter_greet
    - action_retrieve_user
* request_recipe
    - recipe_form
    - form{"name": "recipe_form"}
    - form{"name": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - form{"name": null}
    - slot{"satisfied": false}
    - utter_search_again
* affirm
    - form{"name": "recipe_form"}
    - form{"name": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - form{"name": null}
    - slot{"satisfied": true}
    - utter_happy_goodbye


## sad path 1
* greet
    - utter_greet
    - action_retrieve_user
* request_recipe
    - recipe_form
    - form{"name": "recipe_form"}
    - form{"name": null}
    - satisfied_form
    - form{"name": "satisfied_form"}
    - form{"name": null}
    - slot{"satisfied": false}
    - utter_search_again
* deny
    - utter_sad_goodbye