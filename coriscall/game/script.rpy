$ import random 
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define c = Character("CORI",color="#c3f55b", who_outlines = [(3,"#fd6692",0,1)])
define h = Character("HUNGRI", color="#fd6692", who_outlines =[(3,"#c3f55b",0,1)], what_outlines=[(2,"#efedfd",0,0)])

# outline thickness, colour, x, y
define q = Character("???", color = "#6657a9",what_outlines=[(3,"#efedfd",0,0)])


define hungup = 0
define donesofar = 0
define guided = False
define restarted = False

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
    scene bg dark
    with fade
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
            c "(Wait, I did?)"
    q "..."
    q "right. I was told you wouldn't talk much."
    q "hi, {outlinecolor=#250e6d}{color=#c3f55b}CORI{/color}{/outlinecolor}."
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
    show hungry yapping with smallsquish 
    h "right. I was told you wouldn't talk much."
    show hungry scheming with smallsquish
    h "hi, {color=#c3f55b}CORI{/color}."
    show hungry hungry with smallsquish
    h "you do food delivery at 4:33 am, allegedly. please accept my order. I'm really {color=#fd6692}hungry.{/color}"
    "the hungry bunny would definitely offer guidance, should cori accept the order."
    "(cori would absolutely accept the order.)"
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
    show hungry yapping with smallsquish
    h "{cps=*2}my order is rather simple. I would like to have a meal that is not too heavy and thick. So: light, fluffy and whimsical. I prefer casual style over exquisite dining, but the casual style must be cooked in an expensive kitchen.{/cps}"
    show hungry yapping2 with smallsquish
    h "{cps=*2}The meal must be easily consumed and quickly digestible, and too many details will be a wasted work lost in my stomach. But I can't stand fast food.{/cps}"
    show hungry disgusted with smallsquish
    h "The era of short form content gave me food poisoning."
    c "Wait, what?"
    show hungry hungry with smallsquish 
    h "I'm just an innocent bunny asking for an innocent meal..."
    c "Are we still talking about food?"
    show hungry thumbsup with smallsquish 
    h "we're definitely talking about edible things."
    c "What?"
    show hungry unamused with smallsquish 
    h "you've said \"what\" like four times today."
    show hungry thumbsup with smallsquish
    h "it shouldn't be too difficult to find a meal for me. I'm not that picky."
    h "there are multiple galleri...gallerias in this city."
    c "..."
    c "Bye, Hungry."
    "you hang up on the call. Surely that was a prank."
    # cori turns a corner
    show hungry scheming with smallsquish
    h "hi, {color=#c3f55b}CORI{/color}."
    c "WHAT?"
    show hungry smiling with smallsquish 
    h "I know you have a soft spot for tiny hungry bunnies like me :>"
    h "well, you're pretty soft all over"
    c "What is that supposed to mean?"
    show hungry hungry with smallsquish
    h "I'll tell you if you feed me."
    show hungry sad with smallsquish 
    h "please feed me!!"
    "you hesitate,"
    "and you give in."
    c "Okay. I will."
    show hungry thumbsup with smallsquish
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
    show hungry neutral with smallsquish
    h "I am too HUNGRY. so I will sit here and await your delivery."
    h "..."
    show hungry unamused with smallsquish
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
    c "That still doesn't tell me that much, though."
    c "Why did they have to talk in metaphors :("
    c "Were their requests related to the art's composition? Textures? Colours? Overall style?"
    c "Are they looking for paintings? Sculptures? Music?"
    c "This customer is too difficult."



label just_go_galleria:
    c "The bunny said something about gallerias."
    c "So it might have been recommending I browse in one."
    c "Or maybe it meant a literal store named \"Galleria\"?"
    jump which_galleria

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
    "Strange AI-generated poster about nothing in particular":
        $ global held_flyer
        $ held_flyer = "aislop"
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
        c "Yeah. I hope you like this meal. I got you some [held_food]."
        # TIE UP
    else:
        # got a flyr
        c "Well... I didn't get any food, because none of them seemed to fit."
        c "Sorry."
        c "If it makes you feel better, I saw this funny flyer on my way out."
        if held_flyer == "aislop":
            jump flyer_aislop
        # TIE UP

label flyer_aislop:
    # special ending heh
    c "It looks ai-generated, and also seems to be about nothing in particular."
    c "But that's what makes the flyer funny."
    show hungry neutral with smallsquish
    h "..."
    show hungry disgusted with smallsquish
    h "I think I just lost my appetite."
    c "Wait, what?"
    show hungry angry with smallsquish
    h "you IDIOT! I eat {color=#fd6692}ART!{/color}"
    c "You what?"
    show hungry unamused with smallsquish
    h "get me away from that slop! eww."
    # cori ponders this for a moment. they got everything wrong lol.
    c "Oh. Sorry."

    # cori crumbles it up and throws it in the recycling bin.

    show hungry thumbsup with smallsquish
    h "it's okay. in a way, you've helped me feel less hungry."
    h "ha ha ha ha ha."
    # ending scene: you...win?
    # on the thing: cori is mostly in shock. the hungry looks like they just looked at something gross, and even the recycling bin also has a grossed out face.
    return 


label got_nothing_from_galleria:
    c "I'm sorry, but I couldn't find anything that you would like."
    show hungry angry with smallsquish
    h "not that you would KNOW, because you didn't bother to LISTEN to my guidance!"
    h "did you at least bring any options?"
    c "Um. No."
    jump failure_ending


label shops_galleria:
    c "Well, this is the closest galleria."
    c "Except...nothing is open, and nobody has set up stalls yet."
    c "It's too early in the morning."

    c "Well, standing around here stupidly won't help."
    jump shops_what_do

menu shops_what_do:
    c "What should I do?"
    "walk around more":
        jump exploring_shops
    "go back to the hungry bunny":
        jump early_back_from_shops
    "go to the store named Galleria":
        c "I guess I still have time if I go to the nearest store named Galleria."
        c "I just need to be speedy!"
        scene bg dark 
        with fade
        jump named_galleria

label exploring_shops:
    c ""
    # uh idk what to put here. I guess cori could spot some flyers or something??
    # ooh sohuld do image screens yes

label early_back_from_shops:
    c "Hi, hungry bunny."
    show hungry hungry with smallsquish
    h "CORI!! DO YOU HAVE FOOD ALREADY??"
    c "Um. No."
    c "I went to the nearest galleria, but none of the shops have been set up yet. It is too early."
    h "you went to the nearest galleria..."
    h "you..."
    show hungry angry with smallsquish
    h "are you stoopid?"

    c "Um! No?"

    show hungry unamused with smallsquish 
    h "cori, I don't want you to go to any galleria."
    show hungry neutral with smallsquish 
    h "I want you to go to a gallery."
    h "because..."
    c "A... gallery?"
    h "BECAUSE..."
    # cori flashback
    c "Because you eat {color=#fd6692}art.{/color}"
    show hungry shocked with smallsquish 
    h "you're NOT stupid!"
    c "Oh."

    show hungry smiling with smallsquish
    h "it's okay. you can still go to one! you just gotta be speedy."
    c "Okay."

    show hungry unamused with smallsquish 
    h "what are you waiting for? GET GOING!"
    jump ask_for_guidance

menu ask_for_guidance:
    c "Wait, hungry customer."
    "ask \"can you help me?\"":
        $ global guided 
        $ guided = True
        show hungry neutral with smallsquish
        h "..."
        show hungry scheming with smallsquish
        h "anytime, {color=#c3f55b}CORI.{/color}"
        jump slow_gallery_entrance
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
    # TIE UP

label slow_gallery_entrance:
    c "finish this"
    # oo do paintings falling down or something



label understanding_the_order:
    # cori tries to make sense of the order.
    show hungry hungry with smallsquish 
    h "I am too HUNGRY. so I will sit here and await your delivery."
    show hungry thumbsup with smallsquish
    h "but I'll help you on our call!"
    
    # holds up banana phone
    h "first, in case you haven't figured it out by now,"

    show hungry hungry with smallsquish
    h "{color=#fd6692}I want to eat art.{/color}"


    c "You... what?"

    show hungry yapping with smallsquish
    h "additionally, I lied. I'm actually quite picky!"
    c "I could tell."
    show hungry yapping with smallsquish 
    h "and I do NOT wanna eat any art that I have eaten before."
    c "Oh."

    show hungry scheming with smallsquish
    h "thank me, because I HAVE A PLAN."
    c "Thank you?"

    show hungry yapping with smallsquish 
    h "visit an art gallery, go to its storage rooms, describe its paintings, and I'll let you know if anything sounds appetizing."

    c "How am I supposed to get into an art gallery at this hour?"
    c "Also, aren't paintings rather expensive? And aren't you just a stray bunny?"
    
    show hungry shocked with smallsquish 
    h "I am NOT a stray."
    show hungry unamused with smallsquish
    h "I am actually a mystical being, but that's a story for some other dimension."
    show hungry neutral with smallsquish
    h "don't worry about the payment. just get me the painting."

    c "That still sounds difficult. I'm just a mailman."

    show hungry smilling with smallsquish
    h "yea, and I'm just asking for a delivery."

    c "Do you accept other forms of art? Photography, music, furniture, dance?"

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
    c "...Fine."
    c "I'll deliver."
    # just had a lot of dialogue, so this wlil be slow ? or medium?

label no_invading_gallery:
    c "There must be some other way I could get you a painting!"
    show hungry thumbsup with smallsquish
    h "yea maybe."
    show hungry hungry with smallsquish 
    h "...but I'm too hungry to sit here waiting for you to start thinking."
    jump think_more_or_go


menu think_more_or_go:
    c "I understand..."
    "I'll go to the nearest gallery now.":
        # tie up
        jump slow_gallery_entrance
    "Just let me think about it a bit more.":
        # tie up. not too much thinking but a bit of thinking is what will do
        jump slow_gallery_entrance

# ok so there will be 3 types of gallery entrance: quick, normal, slow
# they unlock different art pieces ?? or something? or different dialogue?? and endings??
# if they enter slow, they can only take a painting from the entrance, which is a famous one
# medium, can get something in the middle
# and quick, has time to go to the back and grab something (this is the only way to win through painting option, in the other two, the hungry has eaten those before?)

label got_best_painting_ending:
    show hungry shocked with smallsquish
    h "YOU GOT IT!!"
    show hungry smiling with smallsquish
    h "thank you very much."
    h "I will eat this RIGHT NOW!!"

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
    
    "You are mostly in shock as you watch the hungry bunny physically consume the art."
    
    show hungry scheming with smallsquish
    h "heh heh. that was pretty good."

    show hungry yapping with smallsquish
    h "thank you for contributing to my stomach's collection!"

    c "Oh."
    c "Anytime."

    # it was quick: shows that this player cori is more about action than dialogue/thinking, so the ending is swift as well?

    # make ending screens interactive

    return 

label successful_ending:
    show hungry shocked with smallsquish
    h "YOU GOT IT!!"
    show hungry smiling with smallsquish
    h "thank you very much."
    h "I will eat this RIGHT NOW!!"

    h "chomp chomp chomp"
    c "Wait, you're physically eating the art?!"
    show hungry scheming with smallsquish
    h "yea. you thought it was metaphorical?"
    h "HAHA!"

    show hungry smiling with smallsquish

    h "chomp chomp chomp"

    c "Oh no."
    c "How will I explain this to the art gallery?"

    show hungry scheming with smallsquish
    h "don't worry. I think it will be a loong while before they notice."
    
    h "..."

    show hungry sad with smallsquish
    h "I've had this painting before."

    c "I thought you had said that you haven't?"

    show hungry unamused with smallsquish

    h "I recognized the taste. your description sucked."

    c "But that was a niche gallery!"

    h "yea... thanks for going out and getting food for me."
    
    c "Are you satisfied?"

    show hungry sad with smallsquish
    h "... no."

    c "Oh."
    c "I'm sorry."

    c "Wait. If you physically eat paintings, then how could you have eaten this one before?"
    show hungry yapping with smallsquish 
    h "my consumption transcends the boundaries of time."
    c "What?"
    show hungry neutral with smallsquish
    h "you are a sandwiche enduit."

    c "Oh."
    c "Sorry."

    show hungry scheming with smallsquish
    h "BUT! It's okay."
    h "I know how you can make it up to me :3"

    c "What?"

    h "{color=#fd6692}create{/color} something for me, {color=#c3f55b}CORI!{/color}"
    scene bg dark
    with dissolve
    # TIE UP (idk if I will make this another node or just cliffhanger ending here)

    # next up: cori's creation?? cori's coeur??
    # in every timeline, the Hungry finds a way to mess with cori.





label half_ending:
    show hungry neutral with smallsquish
    h "well, it's not exactly what I wanted..."
    h "but I guess you can't be picky and hungry at the same time."

    h "chomp chomp chomp"

    show hungry disgusted with smallsquish
    h "nevermind, I disagree. I'm hungry, but not hungry enough for THIS thing."

    c ":("
    c "Sorry."

    h "it's the wrong type of meal entirely!"
    c "It's a meal!"
    h "I gave you very particular instructions!"
    c "You said you were not very picky!"
    h "that was obviously a joke! I am VERY PICKY!"
    c "I can tell! But I'd appreciate some explanations!"
    h "you rejected my guidance!"
    # make the sprites move towards each other during this interaction lol

    h "..."
    jump which_explanation

menu which_explanation:
    h "do you want the short explanation, cori, or the long one?"
    "Short":
        jump short_explanation
    "Long":
        jump long_explanation

label short_explanation:
    h "in short, I eat art. you got me food."
    h "you're getting a zero star review."
    c "What?"
    h "hey, you wanted the short explanation."
    scene bg dark
    with fade 
    jump try_again

label long_explanation:
    h "I EAT ART, CORI!"
    h "this food contains some artistry, sure,"
    h "but it's too EDIBLE for me to eat!"
    h "also, if you had accepted my instructions, you would know that I DON'T EAT REPEATS!"
    c "You never repeat a meal?"
    h "there once was a time when I would eat two onigiris every lunch for the entire week."
    c "I had a phase like that too."
    h "but I'm beyond stuff like that now."
    h "I transcend the needs of mortals."
    c "You've made me curious about your life story."
    h "heh."
    h "don't worry, {color=#c3f55b}CORI.{/color}"
    h "I'm sure you'll learn it all."
    scene bg dark
    with dissolve 
    jump try_again 


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
        "cori will forget, but..."
        $ global restarted
        $ restarted = True
        h "I will remember EVERY time she's hung up on me."
        h "among other things. see you there!"
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