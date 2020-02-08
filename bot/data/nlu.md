## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- hows it going
- hi there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- yes please

## intent:postive
- sounds good
- looks excellent
- yum
- delicous
- nice
- awesome
- brilliant

## intent:negative
- looks horrible
- urgh
- grim

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- I don't

## intent:thankyou
- thanks
- thank you
- cheers

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- who are you?

## intent:request_recipe
- what should I eat?
- give me a recipe?
- what food to cook?
- what should I cook?
- Give me a [quick](duration:30 minutes) recipe for [duck](main)
- Could you give me a recipe for [pasta](main)
- Could you give me a [vegan](dietary) recipe
- I want a [veggie](dietary:vegeterian) dish
- Can I have a [meat](dietary) dish
- I've got [20 mins](duration) please could I have a recipe for [pasta](main)
- please could i have a recipe
- Could you give me something with [chicken](main) in
- yeah please could you give me something with [chicken](main)
- what can I cook in [20 minutes](duration)
- what [chicken](main) dish can I cook
- what can I cook for supper
- What can i cook in [20 minutes](duration)
- can you give me a [rice](main) dish for supper
- what [chicken](main) dish should i cook for tonight

## intent:inform
- [chicken](main)
- how about [pasta](main)
- [asian](main)
- [beef](main)
- [fish](main)
- something with [pork](main)
- [sausages](main)
- I have [25 minutes](duration))
- I've only got [1 hour](duration))
- [30 mins](duration))
- [25 mins](duration)
- something with [chicken](main)
- an hour
- [pasta](main)
- [30 minutes](duration)
- something with [rice](main)
- [30 mins](duration)
- [rice](main)
- [shallots](main)
- [ciabatta loaf](main)
- [mangetout](main)
- [romaine lettuces](main)
- [steak](main)
- [bacon](main)
- [mascarpone](main)
- something with [noodles](main)
- [20 mins](duration)
- [an hour](duration)
- [half an hour](duration)
- something [quick](duration:30 minutes)
- about [45 minutes](duration)
- [40 mins](duration)
- [45 mins](duration)
- [rice](main)
- [40 mins](duration)
- [noodles](main)

## intent:inform_dietary
- [vegan](dietary)
- [veggie](dietary:vegeterian)
- I'm [vegan](dietary)
- I am a [vegeterian](dietary)

## intent:correct_dietary_negative
- Actually I don't have any dietary requirements
- Actually change that, I don't have any dietaries

## intent:change_choices
- Actually can I change my choices
- Can I search for soemthing else
- Can I search again
- can i search for something else
- [ingredients](change_main)
- I want to change [both](change_both)
- [dish](change_main)
- [time to cook](change_duration)
- [duration](change_duration)
- I want to change [duration](change_duration)
- can i change my choices
- cooking [time](change_duration)
- actually i've changed my mind
- [both](change_both)
- [ingrediants](change_main:ingredients)

## synonym:30 minutes
- quick
- fast
- speedy
- snappy

## synonym:vegeterian
- veggie

## lookup:main
  data/food.txt
