# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("CORI",color="#c3f55b", who_outlines = [(3,"#fd6692",0,1)])
# cori does a neutral sprite by default, when she's not talking. also doesn't corisquish that much, only squish for impactful dialogue
define h = Character("HUNGRI", color="#fd6692", who_outlines =[(3,"#c3f55b",0,1)], what_outlines=[(2,"#efedfd",0,0)])

# outline thickness, colour, x, y
define q = Character("???", color = "#250e6d",what_outlines=[(2,"#efedfd",0,0)])


define hungup = 0
define donesofar = 0
define guided = False
default restarted = 0

define itsbrover = False

define held_flyer = ""
define held_food = ""
define held_painting = ""

define lst_foods = []
define finalfood = ""

# badges or something:
# NO TIME FOR TODAY'S RELEASE!!

define endstar = ""
define foodstar = ""
define speedstar = ""
define confidencestar = ""
define selfstar = ""

define tempthing = "you were extremely slow"
if (restarted > 0):
    if(restarted == 1):
        $ tempthing += ("(you even restarted once.)")
    else:
        $ tempthing += "(you even restarted [restarted] times)"
define stars = [
    ["you did not reach a notable ending", "you reached an ending, but it was mediocre.", "you reached a good ending!"],
    ["you did not get anything", "you got something, but the hungry didn't like it", "the hungry liked your delivery!"],
    ["you were extremely slow", "you were average paced", "you were speedy!"],
    ["you were not decisive", "your decisiveness was average", "you were decisive"],
    ["you received all the guidance", "you received some guidance", "you did it your way!"]
]

define galleryspeed = ""
# slow, mid or fast

# "none" "half" "full"
# one star for reachin the end
# one star for getting something the hungry liked
# speed done (counted by lines of dialogue clicked through??) (also counts restarted stuff)
# decisiveness (choosing to think more about tihngs, or answering "maybe")
define decisiveness = "2"
# independence: amount of guidance they asked for/used (mostly in the getting-painting chapter)

define speeddone = "fast"
# more clicking through = becomes slow

default persistent.fullywon = None
define endingtype = ""
# the failure, the 
define endingdesc = ""

# the call, the order, the delivery, the review 

# animations




# thank you

transform smallsquish(duration = 0.1,*,new_widget=None,old_widget=None):
    delay duration 
    xcenter .5
    ycenter 0.5

    old_widget
    events False
    linear 0.3 yzoom(1.01)

    new_widget
    events True
    linear 0.3 yzoom(1.0)

transform corisquish(duration = 0.1,*,new_widget=None,old_widget=None):
    delay duration 
    xcenter .5
    ycenter 0.5

    old_widget
    events False
    linear 0.2 yzoom(1.01)

    new_widget
    events True
    linear 0.2 yzoom(1.0)

define audio.theme = "audio/most peculiar delivery.wav"
define audio.theme2 = "audio/more peculiar delivery.wav"

# The game starts here.

label start:
    $ global held_flyer, held_food, held_painting
    $ held_flyer = ""
    $ held_food = ""
    $ held_painting = ""
    scene bg dark
    with dissolve
    $ renpy.notify("part 1: the call")
    stop music fadeout 1.0

    show ringy1
    q "ring"

    show ringy2
    q "ring ring ring"

    show ringy3
    c "Whaat"
    scene cally1
    with dissolve
    jump the_call

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
    show cally2
    c "Back to sleep."
    show sleepy1
    pause 0.5
    $ s = hungup * "I"
    show cally3

    q "R[s]NG!"
    scene cally1
    jump the_call 


label the_customer:
    $ global hungup
    show hey1
    q "HEY."
    show hey2
    if hungup > 0:
        if hungup == 1:
            q "WHY'D YOU HANG UP ON ME ONCE??"
        else:
            q "WHY'D YOU HANG UP ON ME [hungup] TIMES??"
            c "(Wait, I did?)"
    show hey3 
    q "..."

    q "right. I was told you wouldn't talk much."
    show hey4 
    with dissolve
    q "hi, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
    # show hey5
    with dissolve 
    q "you do food delivery even at 4:33 am."
    # show hey6
    q "please accept my order."
    show hey7
    with dissolve
    q "I'm really..."
    scene hey8
    with dissolve 
    h "{color=#fd6692}...hungry.{/color}"

    scene bg dark
    with dissolve 
    jump from_the_beginning

# label the_order:

#     show cori sorry with dissolve 
#     "you get the feeling that you don't quite have a choice."
#     "(after all, cori has always been a bit too compassionate for the unyielding world.)"
#     scene bg dark
#     with dissolve 
#     # scene where cori gets up and dressed
#     # fade to black
#     jump from_the_beginning


label from_the_beginning:
    # writing this alongside cori's perspective.
    # a collection of scenes. maybe animate or parallax or something
    scene bg pink
    "one early sunrise, a little bunny woke up hungry."
    show hungri1
    "unfortunately, 4:20 am in the big '26 was probably too early for anything delicious."
    show hungri2
    "the little bunny sighed, ready to scour for scraps."
    show hungri3 
    "eyes still half-closed, they glanced towards the distance."
    show screen monumental
    "a familiar monument stood along the skyline."
    show hungri5
    hide screen monumental
    "suddenly excited, the bunny rushed to find a method of contact."
    show hungri6
    "an unripe banana would do."
    # hungri faces
    scene bg lightground
    show hungry scheming 
    h "{outlinecolor=#fd6692}{color=#c3f55b}Cori's Courier{/color}{/outlinecolor} is going to love this customer."
    scene bg phonecall with dissolve
    show hungry smiling with dissolve
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
    show hungry neutral with dissolve 
    show cori neutral with dissolve 
    "after what felt like multiple eternities, cori finally picked up."
    h "HEY."
    if hungup > 0:
        show hungry angry with smallsquish
        if hungup == 1:
            h "WHY'D YOU HANG UP ON ME ONCE??"
        else:
            h "WHY'D YOU HANG UP ON ME [hungup] TIMES??"
    h "..."
    show hungry yapping with smallsquish 
    h "right. I was told you wouldn't talk much."
    show hungry scheming with smallsquish
    h "hi, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
    show hungry hungry with smallsquish
    h "you do food delivery at 4:33 am, allegedly. please accept my order. I'm really {color=#fd6692}hungry.{/color}"
    jump offer_guidance

label bro_gets_hung_up_on:
    $ global donesofar, hungup
    $ donesofar += 1
    show hungry unamused with smallsquish
    h "cori hung up..."
    show hungry neutral with smallsquish
    h "well."
    show hungry smiling with smallsquish 
    h "they say next time's the charm."
    if(donesofar == 1):
        show hungry thumbsup with smallsquish
        h "after all, I've only tried once!"
    else:
        show hungry thumbsup with smallsquish
        h "even though I've tried [donesofar] times!"
    show hungry smiling
    "RING!"
    "."
    if(donesofar >= hungup):
        "{color=#fd6692}(you know you did this to yourself.){/color}"
        jump from_the_ringing
    else:
        jump bro_gets_hung_up_on
        
label offer_guidance:
    $ renpy.notify("part 2: the order")
    # cori is now dressed and ready to do delivery. walks along the street
    show cori frowning with corisquish 
    c "Hi, Hungry."
    # cori: talking, neutral, confused, shocked, smile, sorry, thinking. cori is less expressive than the hungry
    show hungry smiling with smallsquish 
    h "yeah, that's my name now!"
    show cori talking with corisquish 
    c "What food do you crave at 4:33 am?"
    show cori neutral 
    show hungry scheming with smallsquish
    h "heh..."
    show hungry yapping with smallsquish
    h "{cps=*2}my order is rather simple. I would like to have a meal that is not too heavy and thick. So: light, fluffy and whimsical. I prefer casual style over exquisite dining, but the casual style must be cooked in an expensive kitchen.{/cps}"
    show hungry yapping2 with smallsquish
    h "{cps=*2}The meal must be easily consumed and quickly digestible, and too many details will be a wasted work lost in my stomach. But I can't stand fast food.{/cps}"
    show hungry disgusted with smallsquish
    h "The era of short form content gave me food poisoning."
    show cori confused with corisquish
    c "Wait, what?"
    show cori neutral 
    show hungry hungry with smallsquish 
    h "I'm just an innocent bunny asking for an innocent meal..."
    show cori thinking with corisquish
    c "Are we still talking about food?"
    show cori neutral 
    show hungry thumbsup with smallsquish 
    h "we're definitely talking about edible things."
    show cori confused with corisquish
    c "What?"
    show cori neutral 
    show hungry unamused with smallsquish 
    h "you've said \"what\" like four times today."
    show cori sorry 
    show hungry thumbsup with smallsquish
    h "it shouldn't be too difficult to find a meal for me. I'm not that picky."
    h "there are multiple galleri...gallerias in this city."
    show cori neutral 
    show hungry yapping2 
    c "..."
    show cori talking with corisquish 
    c "Bye, Hungry."
    scene bg lightground with dissolve
    "surely that was a prank."
    "but just as you turn around to get some more sleep..."
    # cori turns a corner
    show hungry scheming with smallsquish
    h "hi, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
    show cori shocked with corisquish 
    c "WHAT?"
    show cori neutral 
    show hungry smiling with smallsquish 
    h "I know you have a soft spot for tiny hungry bunnies like me :>"
    show cori confused with corisquish
    c "What is that supposed to mean?"
    show cori neutral 
    show hungry hungry with smallsquish
    h "I'll tell you if you feed me."
    show hungry sad with smallsquish 
    h "please feed me!!"
    show cori confused with corisquish
    "you hesitate,"
    show cori determined
    "and you give in."
    show cori talking
    show hungry smiling
    c "Okay. I will."
    show cori neutral 
    show hungry thumbsup with smallsquish
    jump want_guidance
    # cori's memory is pretty decent
    # cori's number includes "2674" (spells out cori) (this is irrelevant for the game)

menu want_guidance:
    h "I'll help you too! do you want my guidance?"
    "Yes":
        $ global guided
        $ guided = True
        jump understanding_the_order
    "No":
        jump trying_to_understand

label trying_to_understand:
    show hungry neutral with smallsquish
    h "okay then."
    h "I am too HUNGRY. so I will sit here and await your delivery."
    h "..."
    show hungry unamused with smallsquish
    h "what are you waiting for?"
    show hungry angry with smallsquish 
    h "get going!"
    # scene transition
    scene bg lightcyan
    show cori confused with corisquish 
    c "I just ran off in a miscellaneous direction. I'm not quite sure what \"food\" they are craving."
    # scene flashback
    show cori frowning
    jump think_or_do

menu think_or_do:
    c "Should I think harder, or just go?"
    "think harder":
        jump understanding_alone
    "just go":
        jump just_go_galleria

label understanding_alone:
    show cori thinking 
    c "The bunny didn't stutter when talking about what it wanted."
    show cori frowning
    c "Except..."
    # scene flashback
    show cori thinking 
    c "Gallerias... galleries..."
    show cori confused with corisquish 
    c "It wants me to deliver {color=#fd6692}art?{/color}"

    show cori neutral with dissolve 
    # fade 
    c "That still doesn't tell me that much, though."
    show cori frowning:
        zoom 1.1
    c "Why did they have to talk in metaphors :("
    show cori thinking:
        zoom 1.2
    c "Were their requests related to the art's composition? Textures? Colours? Overall style? Are they looking for paintings? Sculptures? Music?"
    show cori frowning:
        zoom 1.3
    c "This customer is too difficult."
    show cori neutral:
        zoom 1.0
    c "I guess I'll just go to the nearest art gallery."
    jump fast_gallery_entrance



label just_go_galleria:
    $ renpy.notify("part 3: the delivery")
    show cori thinking 
    c "The bunny said something about gallerias."
    show cori neutral 
    c "So it might have been recommending I browse in one."
    show cori thinking 
    c "Or maybe it meant a literal store named \"Galleria\"?"
    show cori confused with corisquish 
    jump which_galleria

menu which_galleria:
    c "Where should I go?"
    "store named \"Galleria\"":
        jump named_galleria
    "closest galleria (collection of shops)":
        jump shops_galleria

label named_galleria:
    scene bg storeenter
    # cake, cotton candy, fried rice, onigiri, gimbap,
    show cori neutral with dissolve 
    c "Well, this is the closest Galleria."
    c "It's currently closed, but I'll just enter and leave some money on the counter."
    scene bg store1
    show cori thinking 
    c "\"light, fluffy and whimsical\"..."
    show cori talking 
    c "A few things catch my gaze."
    # show images of food on screen. or do options
    $ global lst_foods
    $ lst_foods = [
        ("bread", "cross_bread"),
        ("cake", "cross_cake"),
        ("cotton_candy", "cross_cotton_candy"),
        ("fried_rice","cross_fried_rice"),
        ("gimbap","cross_gimbap"),
        ("onigiri","cross_onigiri")
    ]

    jump cross_foods_out

label cross_foods_out:
    # honestly could make this a drag/drop
    scene bg store
    show cori thinking with corisquish
    call screen foodoptions

    show cori neutral with corisquish 
    $ thechoicefood = _return 
    show screen foodscreen(thechoicefood)
    if (thechoicefood == "fried_rice"):
        $ thechoicefood = "fried rice"
    if (thechoicefood == "cotton_candy"):
        $ thechoicefood = "cotton candy"
    c "I guess [thechoicefood] is the one remaining option."
    $ global finalfood
    $ finalfood = thechoicefood
    jump one_food_to_cross
    # if(len(lst_foods) == 1):
    #     show cori talking with corisquish 
    #     c "I guess there is one remaining option."
    #     $ global finalfood
    #     $ finalfood = lst_foods[0][0]
    #     if (finalfood == "fried_rice"):
    #         $ finalfood = "fried rice"
    #     if (finalfood == "cotton_candy"):
    #         $ finalfood = "cotton candy"
    #     jump one_food_to_cross
    # else:
    #     call screen foodoptions

    # "{color=#fd6692}(Click a food option to cross out.){/color} Cori needs to cross out fast food, meals that would take too long to eat, and thick and heavy stuff."
    # $ global lst_foods
    # $ the_food_crossed = menu(lst_foods)
    # $ renpy.jump(the_food_crossed)

label cross_bread:
    # $ global lst_foods
    # $ lst_foods.remove(("bread","cross_bread"))
    show cori frowning with corisquish
    c "Yeah, I don't think bread will work."
    jump cross_foods_out

label cross_cake:
    # $ global lst_foods
    # $ lst_foods.remove(("cake","cross_cake"))
    show cori frowning with corisquish
    c "Yeah no, the hungry bunny wouldn't like cake."
    jump cross_foods_out

label cross_cotton_candy:
    # $ global lst_foods
    # $ lst_foods.remove(("cotton_candy","cross_cotton_candy"))
    show cori frowning with corisquish
    c "I don't think cotton candy would feed a hungry soul like that one."
    jump cross_foods_out

label cross_fried_rice:
    # $ global lst_foods
    # $ lst_foods.remove(("fried_rice","cross_fried_rice"))
    show cori frowning with corisquish
    c "I like fried rice, but I don't think the hungry bunny would."
    jump cross_foods_out

label cross_gimbap:
    # $ global lst_foods
    # $ lst_foods.remove(("gimbap","cross_gimbap"))
    show cori frowning with corisquish
    c "Uh huh, gimbap probably isn't what the hungry bunny wanted."
    jump cross_foods_out

label cross_onigiri:
    # $ global lst_foods
    # $ lst_foods.remove(("onigiri","cross_onigiri"))
    show cori frowning with corisquish
    c "Mhm, onigiri wouldn't satisfy the hungry bunny."
    jump cross_foods_out

menu one_food_to_cross:
    c "Should I buy [finalfood]?"
    "Yes":
        $ held_food = finalfood
        hide screen foodscreen 
        scene bg storemoney
        show cori neutral 
        c "I'll just leave some money there. Time to head back."
        jump back_from_the_galleria
    "No":
        hide screen foodscreen 
        jump nothing_is_satisfactory

label nothing_is_satisfactory:
    show cori frowning 
    c "I guess this is it. Nothing is really satisfactory."
    scene bg flyers 
    show cori smile
    c "Ha... those flyers look fun. Maybe I'll take one of them home."
    show screen takeflyers
    "{color=#fd6692}(Click a flyer to take it.){/color}"
    pause 

    jump noneflyer
    # cori notices a few flyers on the way out.
    # SCENE HERE
    # jump take_a_flyer

# menu take_a_flyer:
#     c "Maybe I'll take one of them home."
#     # flyer options: advertising taste-testing/cooking job opening, group study sesh with rod, wall painting??? idk figure this out later lol (include an ugly ai generated one trust)
#     # point/click
#     "take none":
#         jump back_from_the_galleria
#     "WORK IN OUR KITCHEN":
#         $ global held_flyer
#         $ held_flyer = "kitchen"
#         jump back_from_the_galleria
#     "are you overstressed and in need of a study sesh?":
#         $ global held_flyer
#         $ held_flyer = "study"
#         jump back_from_the_galleria
#     "I WILL PAINT YOUR WALLS":
#         $ global held_flyer
#         $ held_flyer = "walls"
#         jump back_from_the_galleria
#     "Strange AI-generated poster about nothing in particular":
#         $ global held_flyer
#         $ held_flyer = "aislop"
#         jump back_from_the_galleria

label jobflyer:
    scene bg flytree
    show cori smile
    $ global held_flyer
    $ held_flyer = "job"
    hide screen takeflyers
    show screen flyjob
    c "I appreciate that they are telling me to get a job."
    hide screen flyjob
    jump back_from_the_galleria

label studyflyer:
    scene bg flytree
    show cori smile 
    $ global held_flyer
    $ held_flyer = "study"
    hide screen takeflyers
    show screen flystudy
    c "Looks like a cheerful and fun guy."
    hide screen flystudy
    jump back_from_the_galleria

label designflyer:
    scene bg flytree
    show cori smile
    $ global held_flyer
    $ held_flyer = "design"
    hide screen takeflyers
    show screen flydesign
    c "Graphic design appears to be their passion."
    hide screen flydesign
    jump back_from_the_galleria

label aiflyer:
    scene bg flytree
    show cori smile 
    $ global held_flyer
    $ held_flyer = "ai"
    hide screen takeflyers
    show screen flyai

    c "I...don't even know why someone would make this flyer."
    hide screen flyai
    jump back_from_the_galleria

label noneflyer:
    scene bg flytree
    show cori neutral
    c "I don't feel too inclined to take any of these."
    hide screen takeflyers
    jump back_from_the_galleria

label back_from_the_galleria:
    scene bg lightground
    with dissolve
    show cori neutral with corisquish 
    c "Hi, hungry bunny."
    show hungry hungry with smallsquish
    h "FOOD HAS ARRIVED!!"
    # at this point, cori has either gotten nothing, or gotten a flyer, or a food
    if held_flyer == "" and held_food == "":
        jump got_nothing_from_galleria
    elif held_flyer == "":
        # got food
        show cori talking 
        c "Yeah. I hope you like this meal. I got you some [held_food]."
        jump half_ending
    else:
        # got a flyr
        show cori talking 
        show hungry sad 

        c "Well... I didn't get any food, because none of them seemed to fit."
        show cori sorry 
        c "Sorry."
        show cori neutral 
        c "If it makes you feel better, I saw this fun flyer on my way out."
        show hungry neutral
        if held_flyer == "ai":
            jump flyer_aislop
        if held_flyer == "design":
            jump flyer_design
        if held_flyer == "study":
            jump flyer_study
        if held_flyer == "job":
            jump flyer_job

label flyer_job:
    $ renpy.notify("part 4: the review")
    show cori smile 
    show screen flyjob2
    c "The simplicity of the ad stood out to me."
    show hungry unamused 
    show cori neutral 
    h "are you telling me to get a job??"
    show cori confused
    hide screen flyjob2
    c "Well, if you worked in a kitchen, you could work around food all the time."
    h "..."
    scene bg bigshock
    show cori neutral 
    show hungry angry 
    h "you IDIOT! I eat {color=#fd6692}ART!{/color}"
    show cori shocked with corisquish
    c "..."
    show cori neutral 
    c "What?"
    pause 1.0
    show cori frowning with corisquish 
    c "Oh. I completely misunderstood. Sorry."
    show cori talking 
    c "So you would not enjoy employment in a kitchen?"
    show hungry neutral with smallsquish 
    h "nope. I don't even like eating food."
    show hungry angry 
    h "BECAUSE-"
    show cori determined with corisquish 
    show hungry chomp 
    c "Sorry for shoving the flyer into your mouth. I figured you'd be a graphic design recycling bin."
    show cori frowning 
    show hungry unamused 
    c "Also, my ears are too sensitive to tolerate your yelling."
    show hungry neutral 
    h "this flyer is BLAND. what sort of chef are they trying to hire??"
    show cori neutral 
    show hungry smiling
    h "at least it's food. thanks, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
    show cori talking
    c "Um. You're welcome."

    window hide 
    scene bg lightcyan
    play music theme2 fadein 1.0 loop fadeout 1.0
    show screen endscreen 
    with dissolve 

    pause 

    return 

label flyer_study:
    $ renpy.notify("part 4: the review")

    show cori smile 
    show screen flystudy2
    c "The meter isn't the most consistent, but the design is catchy."
    show hungry unamused
    show cori determined
    h "your delivery skills are not the most consistent either, evidently."
    show cori confused
    hide screen flystudy2
    c "Hey! I'm a great delivery guy!"
    show hungry neutral 
    show cori frowning 
    h "yea yea, sure."
    show hungry hungry with smallsquish
    h "now, onto more important matters..."
    scene bg bigshock
    show hungry angry with smallsquish 
    show cori sorry with smallsquish
    h "YOU COULDN'T GET ANYTHING?!"
    show cori frowning 
    c "I said none of the food at Galleria seemed to fit!"
    scene bg lightground
    show cori frowning 
    show hungry unamused
    h "you IDIOT! I eat {color=#fd6692}ART!{/color}"
    show cori shocked with corisquish
    c "..."
    show cori neutral 
    c "You what?"
    pause 1.0
    show cori frowning with corisquish 
    c "Oh. I completely misunderstood your order."
    c "Sorry."
    show hungry angry with smallsquish
    h "learn to understand SUBTEXT, kid!"
    show cori talking 
    show hungry neutral with smallsquish
    h "maybe you SHOULD go join that study group."
    show cori neutral 
    c "I...don't even know what to say in response."
    show hungry scheming 
    h "heh. you cannot outwit me."
    h "yummy!"
    show hungry chomp with smallsquish 
    show cori frowning 
    c "Why are you eating the flyer?"
    show hungry smiling with smallsquish
    h "ha ha. delicious story art. glad rod is smiling."
    show cori talking 
    c "What?"
    h "yea. thank you for the food :3"
    show cori confused 
    c "Um. Anytime? "

    window hide 
    play music theme2 fadein 1.0 loop fadeout 1.0
    show screen endscreen 
    with dissolve 

    pause 

    return 

label flyer_design:
    $ renpy.notify("part 4: the review")
    show cori smile 
    show screen flydesign2
    c "It says that they need a \"grafic deziner,\" but I think they need a spell checker as well."
    show hungry shocked with smallsquish
    h "woww! they still hire graphic designers these days!!"
    show cori frowning 
    c "That sounded sarcastic."
    show hungry neutral with smallsquish
    h "mehh, I would neverr."
    show cori confused 
    show hungry hungry with smallsquish
    h "now, onto more important matters..."
    scene bg bigshock
    show hungry angry with smallsquish 
    show cori sorry with smallsquish
    h "YOU COULDN'T GET ANYTHING?!"
    show cori frowning 
    c "I said none of the food at Galleria seemed to fit!"
    scene bg lightground
    show hungry angry with smallsquish
    h "you IDIOT! I eat {color=#fd6692}ART!{/color}"
    show cori confused with corisquish
    c "..."
    c "You what?"
    show cori neutral 
    h "..."
    show hungry neutral 
    "..."
    show cori determined with corisquish 
    c "Is this flyer artistic enough for your taste?"
    show hungry chomp with smallsquish 
    h "hmmmm..."
    hide screen flydesign2
    show hungry thumbsup with smallsquish 
    h "yea."

    window hide 
    scene bg lightcyan 
    play music theme2 fadein 1.0 loop fadeout 1.0
    show screen endscreen 
    with dissolve 

    pause 

    return 



label flyer_aislop:
    # special ending heh
    $ renpy.notify("part 4: the review")

    show cori neutral 
    show screen flyai2
    c "It looks ai-generated, and also seems to be about nothing in particular."
    show cori talking 
    c "But that's what makes the flyer funny."
    hide screen flyai2
    show cori neutral 
    show hungry neutral with smallsquish
    h "..."
    scene bg green 
    show cori neutral 
    show hungry disgusted
    h "I think I just lost my appetite."
    scene bg lightground 
    show hungry disgusted
    show cori frowning with corisquish 
    c "Wait, what?"
    scene bg bigshock
    show cori neutral 
    show hungry angry with smallsquish:
        zoom 1.05
    h "you IDIOT! I eat {color=#fd6692}ART!{/color}"
    show cori confused with corisquish 
    c "..."
    scene bg lightground 
    show cori confused 
    show hungry angry
    c "You what?"
    show cori neutral 
    show hungry unamused with smallsquish
    h "get me away from that slop! eww."
    show cori thinking with corisquish 
    pause 1.0
    show cori neutral 
    # cori ponders this for a moment. they got everything wrong lol.
    c "Oh. Sorry."

    # cori crumbles it up and throws it in the recycling bin.

    show hungry thumbsup with smallsquish
    h "it's okay. in a way, you've helped me feel less hungry."
    show hungry smiling with smallsquish 
    h "ha ha ha ha ha."
    # ending scene: you...win?
    # on the thing: cori is mostly in shock. the hungry looks like they just looked at something gross, and even the recycling bin also has a grossed out face.

    return 


label got_nothing_from_galleria:
    show cori sorry 
    c "I'm sorry, but I couldn't find anything that you would like."
    scene bg bigshock
    show cori neutral 
    show hungry angry with smallsquish
    h "not that you would KNOW, because you didn't bother to LISTEN to my guidance!"
    scene bg lightground
    show hungry unamused with smallsquish
    show cori neutral
    h "did you at least bring any options?"
    show cori frowning 
    c "Um. No."
    show cori neutral 
    jump failure_ending


label shops_galleria:
    scene bg white 
    show cori neutral 
    c "Well, this is the closest galleria."
    show cori frowning  
    c "Except...nothing is open, and nobody has set up stalls yet."
    show cori neutral
    c "It's too early in the morning."
    c "..."
    show cori frowning 
    c "Standing around here stupidly won't help."
    show cori thinking with corisquish
    jump shops_what_do

menu shops_what_do:
    c "What should I do?"
    "walk around more":
        jump exploring_shops
    "go back to the hungry bunny":
        jump early_back_from_shops
    "go to the store named Galleria":
        show cori neutral 
        c "I guess I still have time if I go to the nearest store named Galleria."
        show cori determined with corisquish 
        c "I just need to be speedy!"
        $ global speeddone
        $ speeddone = "mid" 
        scene bg dark 
        with dissolve 
        jump named_galleria

label exploring_shops:
    show exploreri with corisquish
    c "There is actually nothing here."
    # uh idk what to put here. I guess cori could spot some flyers or something??
    # ooh sohuld do image screens yes
    # lol 4th wall
    c "I guess it's still undergoing {color=#fd6692}development.{/color}"
    c "Now I'll have to return to Hungri without anything."
    jump failure_ending

label early_back_from_shops:
    scene bg lightground
    show cori neutral 
    c "Hi, hungry bunny."
    show hungry hungry with smallsquish
    h "CORI!! DO YOU HAVE FOOD ALREADY??"
    show cori sorry 
    c "Um. No."
    show cori talking 
    c "I went to the nearest galleria, but none of the shops have been set up yet. It is too early."
    show cori neutral 
    show hungry neutral with smallsquish 
    h "you went to the nearest galleria..."
    h "you..."
    show hungry angry with smallsquish
    h "are you stoopid?"

    show cori confused with corisquish 
    c "Um! No?"
    show cori neutral 
    show hungry unamused with smallsquish 
    h "cori, I don't want you to go to any galleria."
    show hungry neutral with smallsquish 
    h "I want you to go to a gallery."
    h "because..."
    show cori shocked
    c "A... gallery?"
    show cori neutral 
    h "BECAUSE..."
    # cori flashback
    show cori talking with corisquish 
    c "Because you eat {color=#fd6692}art.{/color}"
    show cori neutral 
    show hungry shocked with smallsquish 
    h "you're NOT stupid!"
    c "Oh."

    show hungry smiling with smallsquish
    h "it's okay. you can still go to one! you just gotta be speedy."
    show cori determined 
    c "Okay."

    show hungry unamused with smallsquish 
    h "what are you waiting for? GET GOING!"
    show cori thinking with corisquish
    jump ask_for_guidance

menu ask_for_guidance:
    c "Wait, hungry customer."
    "ask \"can you help me?\"":
        $ global guided 
        $ guided = True
        show hungry neutral with smallsquish
        h "..."
        show hungry scheming with smallsquish
        h "anytime, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
        jump mid_gallery_entrance
    "ask \"anything else you want in your meal?\"":
        show hungry hungry with smallsquish
        h "I thought you'd never ask!"
        show hungry scheming with smallsquish
        h "make it something I've never eaten before."
        jump slow_gallery_entrance
    "say \"nevermind.\"":
        "you think the hungry customer seems slightly amused."
        "or maybe it is just laughing at your stupidity."
        h "get going then!"
        jump slow_gallery_entrance

label fast_gallery_entrance:
    $ renpy.notify("part 3: the delivery")
    scene bg gallery 
    show cori smile
    c "It's quite early. I don't think anyone will be in here for a while."
    # oh gosh I could make this another drag and drop
    # well no time
    scene bg verydark 
    with dissolve 
    c "This is the back of the gallery. The stuff that they store here is probably interesting."
    if guided:
        show pmeta:
            zoom 0.4
            xalign 0.5
            yalign 0.0
        c "I found a painting from their storage area that looks enticing. There is no label, just a signature I don't recognize in the corner."
        c "It almost feels familiar."
        h "okay, TAKE IT! and HURRY UP back here! I'm hungry."
        c "Yeah, hungry, I know."
        $ global held_painting
        $ held_painting = "meta"
    else:
        show pheaven:
            zoom 0.4
            xalign 0.5
            yalign 0
        c "This painting feels... familiar."
        c "I think the hungry bunny would like it. I know that I certainly do."
        $ global held_painting
        $ held_painting = "heaven"
    jump got_best_painting_ending
        

label mid_gallery_entrance:
    $ renpy.notify("part 3: the delivery")

    scene bg gallery 
    show cori neutral
    c "I don't know how much time I have until someone comes here."
    $ global speeddone
    $ speeddone = "mid"
    c "I guess I'll take the first painting I see."
    scene bg white 
    with dissolve 
    if guided:
        h "NO REPEATS!"
        c "I'm at a small gallery. I would guess that you haven't seen these before."
        show lhat:
            zoom 0.4
            xalign 0.5
            yalign 0.4
            
        c "That's a whimsical painting. I think Hungri would like it."
        $ global held_painting
        $ held_painting = "hat"
    else:
        show lmoonshy:
            zoom 0.5
            xalign 0.75
            yalign 0.3
        show cori smile 
        c "This painting is the embodiment of \"light and fluffy.\" I think the hungry would like it."
        $ global held_painting
        $ held_painting = "moonshy"
    jump successful_ending


label slow_gallery_entrance:
    $ renpy.notify("part 3: the delivery")

    scene bg gallery 
    show cori frowning
    c "I took too long getting here. Others could be here at any moment."
    show gallery doorshadow with dissolve

    c "I think that all I can do is take the first painting I see-"
    $ speeddone = "slow"
    show cori sorry with corisquish
    c "Oh no, somebody is already inside!"
    hide cori
    c "I need to run (away)!"
    jump got_no_painting
    # oo do paintings falling down or something


label understanding_the_order:
    # cori tries to make sense of the order.
    show cori neutral 
    show hungry hungry with smallsquish 
    h "I am too HUNGRY. so I will sit here and await your delivery."
    show hungry thumbsup with smallsquish
    h "but I'll help you on our call!"
    
    # holds up banana phone
    show hungry yapping with smallsquish 
    h "first, in case you haven't figured it out by now,"

    show hungry hungry with smallsquish
    h "{color=#fd6692}I want to eat art.{/color}"

    show cori shocked with corisquish 
    c "You... what?"
    show cori neutral 
    show hungry yapping with smallsquish
    h "additionally, I lied. I'm actually quite picky!"
    show cori talking 
    c "I could tell."
    show cori neutral 
    show hungry yapping with smallsquish 
    h "and I do NOT wanna eat any art that I have eaten before."
    show cori frowning
    c "Oh."
    show cori neutral 
    show hungry scheming with smallsquish
    h "thank me, because I HAVE A PLAN."
    show cori confused 
    c "Thank you?"
    show cori neutral 
    show hungry yapping with smallsquish 
    h "visit an art gallery, go to its storage rooms, describe its paintings, and I'll let you know if anything sounds appetizing."
    show hungry yapping2 
    show cori thinking
    c "How am I supposed to get into an art gallery at this hour?"
    show cori confused with corisquish 
    c "Also, aren't paintings rather expensive? And aren't you just a stray bunny?"
    show cori frowning 
    show hungry shocked with smallsquish 
    h "I am NOT a stray."
    show hungry unamused with smallsquish
    h "I am actually a mystical being, but that's a story for some other dimension."
    show hungry neutral with smallsquish
    h "don't worry about the payment. just get me the painting."
    show cori neutral 
    c "That still sounds difficult. I'm just a mailman."

    show hungry smiling with smallsquish
    h "yea, and I'm just asking for a delivery."
    show cori thinking 
    c "Do you accept other forms of art? Photography, music, furniture, dance?"
    show cori neutral 
    show hungry hungry with smallsquish
    h "as funny as it would be to see you try to dance, I'm feeling rather painting-hungry today."

    jump invade_gallery_question

menu invade_gallery_question:
    "Despite the hungry bunny's reassurance, you don't really want to invade any art galleries. Do you?"
    "Yes. I'll follow its instructions.":
        jump yes_invade_gallery
    "No. I'd rather try something else.":
        jump no_invading_gallery
    
label yes_invade_gallery:
    show cori neutral 
    c "...Fine."
    show cori determined with corisquish 
    c "I'll deliver."
    # just had a lot of dialogue, so this wlil be slow ? or medium?
    # nvm I have decided that canonically hungri yaps fast
    jump fast_gallery_entrance

label no_invading_gallery:
    show cori determined 
    c "There must be some other way I could get you a painting!"
    show cori neutral 
    show hungry thumbsup with smallsquish
    h "yea maybe."
    show hungry hungry with smallsquish 
    h "...but I'm too hungry to sit here waiting for you to start thinking."
    show cori frowning
    jump think_more_or_go


menu think_more_or_go:
    c "I understand..."
    "I'll go to the nearest gallery now.":
        jump mid_gallery_entrance
    "Just let me think about it a bit more.":
        # tie up. not too much thinking but a bit of thinking is what will do
        scene bg lightground
        show cori thinking with corisquish
        c "..."
        show cori confused with corisquish
        c "..."
        show hungry unamused with smallsquish
        show cori sorry 
        h "OKAY, that is TOO MUCH THINKING!"
        show hungry angry with smallsquish
        show cori frowning
        h "just go already!"
        jump slow_gallery_entrance

# ok so there will be 3 types of gallery entrance: quick, normal, slow
# they unlock different art pieces ?? or something? or different dialogue?? and endings??
# if they enter slow, they can only take a painting from the entrance, which is a famous one
# medium, can get something in the middle
# and quick, has time to go to the back and grab something (this is the only way to win through painting option, in the other two, the hungry has eaten those before?)
# also rememebr this in case I need it later, through the gallery variable

label got_best_painting_ending:
    $ renpy.notify("part 4: the review")
    scene bg lightground
    show cori smile
    if held_painting == "heaven":
        show pheaven:
            zoom 0.4
            xalign 0.3
            yalign 0.0
            rotate 6
    if held_painting == "meta":
        show pmeta:
            zoom 0.3
            xalign 0.35
            yalign 0.4  
            rotate 7
    c "Hi, I hope I was quick enough."


    show hungry shocked with smallsquish
    h "YOU GOT IT!!"
    show hungry smiling with smallsquish
    h "thank you very much."
    show hungry hungry with smallsquish
    hide pmeta
    hide pheaven
    h "I will eat this RIGHT NOW!!"
    # eating sprite 
    show cori neutral 
    show hungry chomp with smallsquish 
    h "chomp chomp chomp"
    show hungry shocked with smallsquish
    h "WHOA!"
    h "this is something VERY NEW!"
    # make a starstruck hungry sprite

    $ global guided
    show hungry smiling with smallsquish
    if guided:
        h "of course, I guided you well :)"
    else:
        h "I'm super impressed you fetched this painting without my guidance!"
    
    show cori frowning
    "(You are mostly shocked.)"
    
    show hungry scheming with smallsquish
    h "heh heh. that was pretty good."

    show hungry yapping with smallsquish
    h "thank you for contributing to my stomach's collection!"
    show cori talking
    c "Oh."
    show cori smile with corisquish 
    c "Anytime."

    # it was quick: shows that this player cori is more about action than dialogue/thinking, so the ending is swift as well?

    # make ending screens interactive.....eventually
    $ global fullywon
    $ persistent.fullywon = True 
    window hide 
    scene bg lightcyan 
    play music theme2 fadein 1.0 loop fadeout 1.0
    show screen endscreen 
    with dissolve 

    pause 

    return 

label successful_ending:
    $ renpy.notify("part 4: the review")
    scene bg lightground 
    # i. e got painting
    show cori smile
    if(held_painting == "hat"):
        show hat:
            zoom 0.3
            xalign 0.4
            yalign 0.55
            rotate 5
            
    else:
        show moonshy:
            zoom 0.4
            xalign 0.4
            yalign 0.5
            rotate 10

    c "Hi, I've returned."

    show hungry shocked with smallsquish
    h "YOU GOT IT!!"
    show hungry smiling with smallsquish
    h "thank you very much. I will eat this RIGHT NOW!!"
    if(held_painting == "hat"):
        hide hat 
    else:
        hide moonshy 
    show hungry chomp with smallsquish 
    h "chomp chomp chomp"
    show cori shocked with corisquish 
    c "Wait, you're physically eating the art?!"
    show cori frowning
    show hungry scheming with smallsquish
    h "yea. you thought it was metaphorical?"
    show hungry scheming:
        zoom 1.1
    h "HAHA!"

    show hungry chomp with smallsquish:
        zoom 1.0 

    h "chomp chomp chomp"

    # show cori neutral
    # c "Oh no."
    # show cori frowning
    # c "How will I explain this to the art gallery?"
    # show cori neutral 
    # show hungry scheming with smallsquish
    # h "don't worry. I think it will be a loong while before they notice."
    
    # eating 
    show hungry neutral 
    h "..."

    show hungry sad with smallsquish
    h "I've had this painting before."
    # show cori confused 
    # c "I thought you had said that you haven't?"
    # show cori neutral
    # show hungry unamused with smallsquish
    # h "I recognized the taste. your description sucked."
    show cori sorry with corisquish
    c "But that was a niche gallery!"
    show cori neutral 
    show hungry neutral with smallsquish
    h "yea... thanks for going out and getting food for me."
    
    # c "Are you satisfied?"

    # show hungry sad with smallsquish
    # h "... no."

    # c "Oh."
    # c "I'm sorry."
    show cori confused 
    c "Wait. If you physically eat paintings, then how could you have eaten this one before?"
    show cori neutral 
    show hungry yapping with smallsquish 
    h "my consumption transcends the boundaries of time."
    show cori talking with corisquish
    c "What?"
    show cori neutral 
    show hungry neutral with smallsquish
    h "you are a sandwiche enduit."
    show cori frowning 
    c "Oh."
    show cori sorry 
    c "Sorry."
    show cori neutral 
    show hungry smiling with smallsquish
    h "BUT! It's okay."
    show hungry scheming with smallsquish 
    h "I know how you can make it up to me :3"
    show cori thinking with corisquish 
    c "What?"
    show hungry smiling with dissolve 
    h "{color=#fd6692}create{/color} something for me, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}!"
    scene bg verydark
    with dissolve

    window hide 
    play music theme2 fadein 1.0 loop fadeout 1.0
    show screen endscreen 
    with dissolve 

    pause 

    return 

    # next up: cori's creation?? cori's coeur??
    # in every timeline, the Hungry finds a way to mess with cori.

label half_ending:
    # got not-art lol
    $ renpy.notify("part 4: the review")
    show hungry neutral with smallsquish
    h "well, it's not exactly what I wanted..."
    show hungry smiling 
    h "but I guess you can't be picky and hungry at the same time."
    show hungry chomp with smallsquish 
    h "chomp chomp chomp"

    show hungry disgusted with smallsquish
    h "nevermind, I disagree. I'm hungry, but not hungry enough for THIS thing."
    show cori sorry 
    c ":("
    c "Sorry."
    show cori neutral 
    show hungry unamused with smallsquish 
    h "it's the wrong type of meal entirely!"
    show cori frowning with corisquish 
    c "It's a meal!"
    show hungry angry:
        zoom 1.1
    h "I gave you very particular instructions!"
    show cori frowning:
        zoom 1.1
    c "You said you were not very picky!"
    show hungry angry:
        zoom 1.2
    h "that was obviously a joke! I am VERY PICKY!"
    show cori frowning:
        zoom 1.2
    c "Could you explain your preferences without being so vague?"
    show hungry neutral with smallsquish:
        zoom 1 
    show cori neutral:
        zoom 1

    h "..."

    jump which_explanation

menu which_explanation:
    h "do you want the short explanation, cori, or the long one?"
    "Short":
        jump short_explanation
    "Long":
        jump long_explanation

label short_explanation:
    show hungry neutral with smallsquish
    h "in short, I eat art. you got me [held_food]."
    show hungry unamused with smallsquish
    h "you're getting a zero star review."
    show cori sorry with corisquish 
    c "What?"
    show cori frowning 
    show hungry neutral with smallsquish
    h "hey, you wanted the short explanation."
    scene bg verydark
    with fade 
    jump try_again

label long_explanation:
    scene bg bigshock with smallsquish
    show hungry angry with smallsquish
    show cori confused 
    h "I EAT ART, CORI!"
    scene bg lightground 
    show cori sorry
    show hungry unamused with smallsquish
    h "this [held_food] contains some artistry, sure,"
    scene bg bigshock with smallsquish 
    show hungry angry with smallsquish
    show cori neutral
    h "but it's too EDIBLE for me to eat!"
    show cori frowning 
    show hungry unamused with smallsquish 
    h "also, if you had accepted my instructions, you would know that I DON'T EAT REPEATS!"
    scene bg lightground 
    show hungry disgusted
    show cori shocked with corisquish
    c "You never repeat a meal?"
    show cori neutral
    show hungry neutral with smallsquish
    h "there once was a time when I would eat two onigiris every lunch for the entire week."
    show cori talking with corisquish
    c "I had a phase like that too."
    show cori neutral 
    show hungry yapping
    h "but I'm beyond stuff like that now."
    show hungry yapping2 
    h "I transcend the needs of mortals."
    show cori thinking with corisquish 
    show hungry yapping
    c "You've made me curious about your life story."
    show cori neutral 
    show hungry smiling with smallsquish
    h "heh."
    show hungry scheming with smallsquish
    h "don't worry, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
    show cori determined 
    h "I'm sure you'll learn it all."
    scene bg verydark
    with dissolve 
    jump try_again 

label got_no_painting:
    # came back from the galery with no painting
    scene bg lightground
    show cori neutral 
    show hungry hungry 
    c "Hi, Hungri."
    show hungry neutral 
    show cori talking 
    c "Sorry, but I didn't get to the gallery early enough. People were already present there."
    jump failure_ending


label failure_ending:
    $ renpy.notify("part 4: the review")
    scene bg bigshock 
    show cori sorry 
    show hungry angry with smallsquish
    h "seriously? you couldn't get ANYTHING?"
    show hungry unamused with smallsquish
    show cori frowning 
    h "I guess I will starve today."
    scene bg lightground
    show cori neutral 
    show hungry neutral with smallsquish 
    h "goodbye, {outlinecolor=#fd6692}{color=#c3f55b}CORI{/color}{/outlinecolor}."
    show hungry scheming with dissolve
    h "I know we'll meet again."

    scene bg verydark
    with dissolve 
    # try again cutscene
    jump try_again

menu try_again:
    "if you could run through time again, would you?"
    "Yes":
        "cori will forget, but..."
        $ global restarted
        $ restarted += 1
        show hungry smiling with dissolve
        h "I will remember EVERY time she's hung up on me."
        show hungry scheming with smallsquish
        h "among other things. see you there!"
        scene bg verydark
        with dissolve
        jump start
    "Maybe":
        jump indecision
    "No":
        jump actually_over

label actually_over:
    "No?"
    show hungry neutral with smallsquish
    h "I wouldn't either, but that's just repeating that statement."
    show hungry smiling with dissolve

    h "how unfortunate that {outlinecolor=#fd6692}{color=#c3f55b}my courier{/color}{/outlinecolor} couldn't win!"

    $ global itsbrover
    $ itsbrover = True 
    window hide 
    scene bg verydark
    play music theme2 fadein 1.0 loop fadeout 1.0
    show screen endscreen 
    with dissolve 

    pause 

    return 
    # scenes

label indecision:
    # bonus indecision
    "\"Maybe\"?"
    show hungry angry with smallsquish
    h "if you can't decide, I will."
    show hungry smiling with dissolve
    h "see you at the beginning, {outlinecolor=#fd6692}{color=#c3f55b}my little courier{/color}{/outlinecolor}."
    jump start


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