# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define c = Character("CORI",color="#c3f55b")
define h = Character("HUNGRI", color="#fd6692")
define q = Character("???", color = "#6657a9")


define hungup = 0
define donesofar = 0
define guided = False

# animations
transform smallsquish(duration = 0.3,*,new_widget=None,old_widget=None):
    delay duration 
    xcenter .5
    ycenter 0.5

    old_widget
    events False
    linear 0.4 yzoom(1.01)

    # Spin the new displayable.
    new_widget
    events True
    linear 0.4 yzoom(1.0)


# The game starts here.

label start:

    # These display lines of dialogue.

    q "ring"

    q "ring ring ring"

    c "Whaat"
    
    jump the_call

    # This ends the game.

    return

menu the_call:
    "you're getting a call. answer it?"
    
    "Yes":
        # hungry stuff here
        jump the_customer
    "No":
        $ global hungup
        $ hungup += 1
        jump the_call2
label the_call2:
    c "Back to sleep."
    q "RING!"
    jump the_call 


label the_customer:
    $ global hungup
    q "HEY."
    if hungup > 0:
        q "WHY'D YOU HANG UP ON ME [hungup] TIMES??"
    q "..."
    q "right. I was told you wouldn't talk much."
    q "hi, {color=#c3f55b}CORI{/color}."
    q "you do food delivery even at 4:33 am."
    q "please accept my order."
    q "I'm really..."
    h "{color=#fd6692}...hungry.{/color}"

    jump the_order

label the_order:
    c "Oh..."
    "you get the feeling that you don't quite have a choice."
    "(after all, cori has always been a bit too compassionate for the unyielding world.)"
    scene bg dark
    with fade
    # scene where cori gets up and dressed
    # fade to black
    jump from_the_beginning


label from_the_beginning:
    # writing this alongside cori's perspective.
    # a collection of scenes
    "one early sunrise, a little bunny woke up hungry."
    "unfortunately, 4:20 am in the big '26 was probably too early for anything delicious."
    "the little bunny sighed, ready to scour for scraps."
    "eyes still half-closed, they glanced towards the distance."
    "a familiar monument stood along the skyline."
    "suddenly excited, the bunny rushed to find a method of contact."
    "a ripe banana would do."
    # hungri face
    h "{color=#c3f55b}Cori's Courier{/color} is going to love this customer."
    "ring"
    "ring ring ring"
    "."
    $ global hungup
    if hungup > 1:
        jump bro_gets_hung_up_on
    else:
        h "cori hung up??"
        h "they say second time's the charm."
    jump from_the_ringing

label from_the_ringing:
    "after what felt like multiple eternities, cori finally picked up."
    h "HEY."
    if hungup > 0:
        h "WHY'D YOU HANG UP ON ME [hungup] TIMES??"
    h "..."
    h "right. I was told you wouldn't talk much."
    h "hi, {color=#c3f55b}CORI{/color}."
    h "you do food delivery at 4:33 am, allegedly. please accept my order. I'm really {color=#fd6692}hungry.{/color}"
    "the hungry bunny would definitely offer guidance, should cori accept the order."
    "cori would absolutely accept the order."
    jump offer_guidance

label bro_gets_hung_up_on:
    $ global donesofar, hungup
    $ donesofar += 1
    h "cori hung up..."
    h "well."
    h "they say next time's the charm."
    if(donesofar == 1):
        h "after all, I've only tried once!"
    else:
        h "even though I've tried [donesofar] times!"
    "RING!"
    "."
    if(donesofar >= hungup):
        "{color=#fd6692}(you know you did this to yourself.){/color}"
        jump from_the_ringing
    else:
        jump bro_gets_hung_up_on
        
label offer_guidance:
    # cori is now dressed and ready to do delivery. walks along the street
    c "Hi, Hungry."
    h "yeah, that's my name now!"
    c "What food do you crave at 4:33 am?"
    h "heh..."
    h "my order is rather simple. I would like to have a meal that is not too heavy and thick. So: light, fluffy and whimsical. I prefer casual style over exquisite dining, but the casual style must be cooked in an expensive kitchen."
    h "The meal must be easily consumed and quickly digestible, and too many details will be a wasted work lost in my stomach. But I can't stand fast food. The era of short form content gave me food poisoning."
    c "Wait, what?"
    h "I'm just an innocent bunny asking for an innocent meal..."
    c "Are we still talking about food?"
    h "we're definitely talking about edible things."
    c "What?"
    h "you've said \"what\" like four times today."
    h "it shouldn't be too difficult to find a meal for me. I'm not that picky."
    h "there are multiple galleri...gallerias in this city."
    c "..."
    c "Bye, Hungry."
    "you hang up on the call. Surely that was a prank."
    # cori turns a corner
    h "hi, {color=#c3f55b}CORI{/color}."
    c "WHAT?"
    h "I know you have a soft spot for tiny hungry bunnies like me :>"
    h "well, you're pretty soft all over"
    c "What is that supposed to mean?"
    h "I'll tell you if you feed me."
    h "please feed me!!"
    "you hesitate,"
    "and you give in."
    c "Okay. I will."
    jump want_guidance
    # cori's memory is pretty decent
    # cori's number includes "2674" (spells out cori)

menu want_guidance:
    h "I'll help you too! do you want my guidance?"
    "Yes":
        $ global guided
        $ guided = True
        jump understanding_the_order
    "No":
        jump trying_to_understand

label trying_to_understand:
    h "I am too HUNGRY. so I will sit here and await your delivery."
    h "let me know if you need any help!"

label understanding_the_order:
    # cori tries to make sense of the order.
    h "I am too HUNGRY. so I will sit here and await your delivery."
    h "but I'll help you on our call!"
    # holds up banana phone


# okay going to basically plan out the whole story RIGHT NOW
# 1. cori gets a prank call. basically has to accept it; it will infinite loop
# 2. short options, hungry asks for art delivery, random of a few options. in short, cori is forced to accept
# 3. hungry asks if cori wants guidance
# 4. yes guidance: cori takes hungri's very vague instructions
# 5. no guidance: cori goes and does stuff
# 6. (both end up the same)
# endings: cori succeeds, cori partially succeeds, cori fails and the hungry continues to be hungry. and secret ending where cori finds out some things :)

# cori is not a shapeshifter in this one, she's just in food delivery mode

# visual style: very blocky, pop, loose/messy