# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define c = Character("CORI",color="#c3f55b")
define h = Character("HUNGRI", color="#fd6692")
define q = Character("???", color = "#6657a9")


define hungup = 0
define donesofar = 0
define guided = False

define held_flyer = ""
define held_food = ""

define lst_foods = []
define finalfood = ""

# animations
transform smallsquish(duration = 0.3,*,new_widget=None,old_widget=None):
    delay duration 
    xcenter .5
    ycenter 0.5

    old_widget
    events False
    linear 0.4 yzoom(1.01)

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
        if hungup == 1:
            q "WHY'D YOU HANG UP ON ME ONCE??"
        else:
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
    # a collection of scenes. maybe animate or parallax or something
    scene bg green
    with fade
    "one early sunrise, a little bunny woke up hungry."
    "unfortunately, 4:20 am in the big '26 was probably too early for anything delicious."
    "the little bunny sighed, ready to scour for scraps."
    "eyes still half-closed, they glanced towards the distance."
    "a familiar monument stood along the skyline."
    "suddenly excited, the bunny rushed to find a method of contact."
    "an unripe banana would do."
    # hungri faces
    show hungry scheming 
    h "{color=#c3f55b}Cori's Courier{/color} is going to love this customer."
    # scheming, smiling, angry, hungry
    "ring"
    "ring ring ring"
    "."
    $ global hungup
    if hungup > 1:
        jump bro_gets_hung_up_on
    else:
        show hungry angry with smallsquish
        h "cori hung up??"
        show hungry smiling with smallsquish
        h "they say second time's the charm."
    jump from_the_ringing

label from_the_ringing:
    "after what felt like multiple eternities, cori finally picked up."
    h "HEY."
    if hungup > 0:
        show hungry angry with smallsquish
        h "WHY'D YOU HANG UP ON ME [hungup] TIMES??"
    h "..."
    show hungry neutral with smallsquish 
    h "right. I was told you wouldn't talk much."
    show hungry scheming with smallsquish
    h "hi, {color=#c3f55b}CORI{/color}."
    show hungry hungry with smallsquish
    h "you do food delivery at 4:33 am, allegedly. please accept my order. I'm really {color=#fd6692}hungry.{/color}"
    "the hungry bunny would definitely offer guidance, should cori accept the order."
    "cori would absolutely accept the order."
    jump offer_guidance

label bro_gets_hung_up_on:
    $ global donesofar, hungup
    $ donesofar += 1
    show hungry angry with smallsquish
    h "cori hung up..."
    show hungry neutral with smallsquish
    h "well."
    show hungry smiling with smallsquish 
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
    # cori: talking, neutral, confused, shocked, smile
    show hungry smiling with smallsquish 
    h "yeah, that's my name now!"
    c "What food do you crave at 4:33 am?"
    show hungry scheming with smallsquish
    h "heh..."
    h "my order is rather simple. I would like to have a meal that is not too heavy and thick. So: light, fluffy and whimsical. I prefer casual style over exquisite dining, but the casual style must be cooked in an expensive kitchen."
    h "The meal must be easily consumed and quickly digestible, and too many details will be a wasted work lost in my stomach. But I can't stand fast food. The era of short form content gave me food poisoning."
    c "Wait, what?"
    show hungry hungry with smallsquish 
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
    show hungry scheming with smallsquish
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
    h "..."
    h "what are you waiting for?"
    h "get going!"
    # scene transition

    c "I just ran off in a miscellaneous direction. I'm not quite sure what \"food\" they are craving."
    # scene flashback
    jump think_or_do

menu think_or_do:
    c "Should I think harder, or just go?"
    "think harder":
        jump understanding_alone
    "just go":
        jump just_go_galleria

label understanding_alone:
    c "The bunny didn't stutter when talking about what it wanted."
    c "Except..."
    # scene flashback
    c "Gallerias... galleries..."
    c "It wants me to deliver {color=#fd6692}art?{/color}"

    # fade 

label just_go_galleria:
    c "The bunny said something about gallerias."
    c "So it might have been recommending I browse in one."
    c "Or maybe it meant a literal store named \"Galleria\"?"

menu which_galleria:
    c "Where should I go?"
    "store named \"Galleria\"":
        jump named_galleria
    "closest galleria (collection of shops)":
        jump shops_galleria

label named_galleria:
    # scene
    # cake, cotton candy, fried rice, onigiri, gimbap,
    c "Well, this is the closest Galleria."
    c "It's currently closed, but I'll just enter and leave some money on the counter."
    c "\"light, fluffy and whimsical\"..."
    c "A few things catch my gaze."
    # show images of food on screen. or do options
    $ global lst_foods
    $ lst_foods = [
        ("bread", "cross_bread"),
        ("cake", "cross_cake"),
        ("cotton candy", "cross_cotton_candy"),
        ("fried rice","cross_fried_rice"),
        ("gimbap","cross_gimbap"),
        ("onigiri","cross_onigiri")
    ]

    jump cross_foods_out

label cross_foods_out:
    if(len(lst_foods) == 1):
        c "I guess there is one remaining option."
        $ global finalfood
        $ finalfood = lst_foods[0][0]
        jump one_food_to_cross
    "{color=#fd6692}(Click a food option to cross out.){/color} Cori needs to cross out fast food, meals that would take too long to eat, and thick and heavy stuff."
    $ global lst_foods
    $ the_food_crossed = menu(lst_foods)
    $ renpy.jump(the_food_crossed)

label cross_bread:
    $ global lst_foods
    $ lst_foods.remove(("bread","cross_bread"))
    c "Yeah, I don't think bread will work."
    jump cross_foods_out

label cross_cake:
    $ global lst_foods
    $ lst_foods.remove(("cake","cross_cake"))
    c "Yeah no, the hungry bunny wouldn't like cake."
    jump cross_foods_out

label cross_cotton_candy:
    $ global lst_foods
    $ lst_foods.remove(("cotton candy","cross_cotton_candy"))
    c "I don't think cotton candy would feed a hungry soul like that one."
    jump cross_foods_out

label cross_fried_rice:
    $ global lst_foods
    $ lst_foods.remove(("fried rice","cross_fried_rice"))
    c "I like fried rice, but I don't think the hungry bunny would."
    jump cross_foods_out

label cross_gimbap:
    $ global lst_foods
    $ lst_foods.remove(("gimbap","cross_gimbap"))
    c "Uh huh, gimbap probably isn't what the hungry bunny wanted."
    jump cross_foods_out

label cross_onigiri:
    $ global lst_foods
    $ lst_foods.remove(("onigiri","cross_onigiri"))
    c "Mhm, onigiri wouldn't satisfy the hungry bunny."
    jump cross_foods_out

menu one_food_to_cross:
    c "Should I buy [finalfood]?"
    "Yes":
        $ held_food = finalfood
        c "I'll just leave some money there. Time to head back."
        jump back_from_the_galleria
    "No":
        jump nothing_is_satisfactory

label nothing_is_satisfactory:
    c "I guess this is it. Nothing is really satisfactory."
    # cori notices a few flyers on the way out.
    c "Ha... those flyers look fun."
    jump take_a_flyer

menu take_a_flyer:
    "Maybe I'll take one of them home."
    # flyer options: advertising taste-testing/cooking job opening, group study sesh with rod, wall painting??? idk figure this out later lol (include an ugly ai generated one trust)
    "take none":
        jump back_from_the_galleria
    "WORK IN OUR KITCHEN":
        $ global held_flyer
        $ held_flyer = "kitchen"
        jump back_from_the_galleria
    "are you overstressed and in need of a study sesh?":
        $ global held_flyer
        $ held_flyer = "study"
        jump back_from_the_galleria
    "I WILL PAINT YOUR WALLS":
        $ global held_flyer
        $ held_flyer = "walls"
        jump back_from_the_galleria

label back_from_the_galleria:
    c "Hi, hungry bunny."
    show hungry hungry with smallsquish
    h "FOOD HAS ARRIVED!!"
    # at this point, cori has either gotten nothing, or gotten a flyer, or a food
    if held_flyer == "" and held_food == "":
        jump got_nothing_from_galleria
    elif held_flyer == "":
        # got food
        c "Yeah. I hope you like this meal."
        # TIE UP
    else:
        # got a flyr
        c "Well... I didn't get any food, because none of them seemed to fit."
        c "Sorry."
        c "If it makes you feel better, I saw this funny flyer on my way out."
        # TIE UP

label got_nothing_from_galleria:
    c "I'm sorry, but I couldn't find anything that you would like."
    show hungry angry with smallsquish
    h "not that you would KNOW, because you didn't bother to LISTEN to my guidance!"
    h "did you at least bring any options?"
    c "Um. No."
    jump failure_ending


label shops_galleria:
    c "Well, this is the closest galleria."


label understanding_the_order:
    # cori tries to make sense of the order.
    show hungry hungry with smallsquish 
    h "I am too HUNGRY. so I will sit here and await your delivery."
    h "but I'll help you on our call!"
    
    # holds up banana phone
    h "first, in case you haven't figured it out by now,"
    h "{color=#fd6692}I want to eat art.{/color}"


label successful_ending:
    h "YOU GOT IT!!"
    h "thank you very much."
    h "I will eat this RIGHT NOW!!"

    h "chomp chomp chomp"
    c "Wait, you're physically eating the art?!"
    h "yea. you thought it was metaphorical?"
    h "HAHA!"
    h "chomp chomp chomp"





label half_ending:
    h "well, it's not exactly what I wanted..."
    h "but I guess you can't be picky and hungry at the same time."

label failure_ending:
    h "seriously? you couldn't get ANYTHING?"
    h "I guess I will starve today."
    h "goodbye, {color=#c3f55b}CORI.{/color}"
    h "I know we'll meet again."

    # try again cutscene
    jump try_again

menu try_again:
    "if you could run through time again, would you?"
    "Yes":
        scene bg dark 
        with dissolve
        jump start
    "Maybe":
        jump indecision
    "No":
        jump actually_over

label actually_over:
    "No?"
    show hungry smiling with smallsquish
    h "I wouldn't either, but that's just repeating that statement."
    h "how unfortunate that {color=#c3f55b}my courier{/color} couldn't win!"
    return 
    # scenes

label indecision:
    # bonus indecision
    "\"Maybe\"?"
    show hungry angry with smallsquish
    h "if you can't decide, I will."
    h "see you at the beginning, {color=#c3f55b}my little courier.{/color} "


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