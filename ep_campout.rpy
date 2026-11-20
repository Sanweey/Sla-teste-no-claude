

label scene_ep_campout:

    $ unclickable = True


    hide screen screen_home_post_eventplanner
    show screen blackscreen
    scene blackscreen
    with dissolve

    $ renpy.pause (2.0, hard=True)
    show screen disable_player_action

    if time_of_day_present == 'MORNING':
        stop music fadeout (12.0)
        show overworld_present_1
        hide screen blackscreen
        with dissolve
        show overworld_present_2
        hide overworld_present_1
        with Dissolve (2.0)
        show overworld_present_3
        hide overworld_present_2
        with Dissolve (2.0)
        show overworld_present_4
        hide overworld_present_3
        with Dissolve (2.0)
    elif time_of_day_present == 'AFTERNOON':
        stop music fadeout (10.0)
        show overworld_present_2
        hide screen blackscreen
        with Dissolve (2.0)
        show overworld_present_3
        hide overworld_present_2
        with Dissolve (2.0)
        show overworld_present_4
        hide overworld_present_3
        with Dissolve (2.0)
    elif time_of_day_present == 'EVENING':
        stop music fadeout (8.0)
        show overworld_present_3
        hide screen blackscreen
        with Dissolve (2.0)
        show overworld_present_4
        hide overworld_present_3
        with Dissolve (2.0)
    else:
        stop music fadeout (6.0)
        show overworld_present_4
        hide screen blackscreen
        with Dissolve (2.0)

    image ep_campout_a1 = Movie(channel="movies/scene_ep_campout/ep_campout_a1.webm", play="movies/scene_ep_campout/ep_campout_a1.webm")
    image ep_campout_a2 = Movie(channel="movies/scene_ep_campout/ep_campout_a2.webm", play="movies/scene_ep_campout/ep_campout_a2.webm")

    show overworld_present_1
    hide overworld_present_4
    with Dissolve (2.0)
    show overworld_present_2
    hide overworld_present_1
    with Dissolve (2.0)
    show overworld_present_3
    hide overworld_present_2
    with Dissolve (2.0)
    $ renpy.pause (4.0, hard=True)
    scene blackscreen
    hide overworld_present_3
    with dissolve

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_grass_1.ogg"
    $ renpy.pause (5.0, hard=True)

    hide screen disable_player_action

    play music "sounds/me/m_scene_20.ogg"
    scene ep_campout_01 with dissolve

    $ renpy.pause()

    scene ep_campout_02 with dissolve

    $ renpy.pause()

    scene ep_campout_03 with dissolve

    n "Mmph... Ugh! This is too much. I... I don't think I can do this! Let me go back home... please?!"
    p "Natalie, quit complaining! You act like this is some long journey."
    j "We haven't even walked a mile and you're already whining."
    n "I'm not whining! It's just that this backpack is SO heavy. This is why I don't like camping, so much work for so little relaxation!"
    mc "Sounds like whining to me! Between you and I, I guess I got all the brawn. Ha!"

    scene ep_campout_04 with fade

    n "Well, if you have all the brawn, then that means I have all the beauty, and I'll take that any day!"
    p "I can't say I'd agree with you there, Natalie. Brawn can be quite the attractive feature."
    j "And I wouldn't say ALL the beauty, [mc] is quite the handsome man if I do say so myself."
    mc "Heh... Thanks you two."
    n "Pfft! Whatever! My statement still stands! Let's just keep going before my legs give out!"

    show ep_campout_05a with dissolve

    p "Alright, I'll motivate you every step of the way if it'll help. I know you have the strength to get there."
    n "I know, I know... I'll make it. Don't worry!"

    show ep_campout_05b with dissolve

    mc "And do you need any help, [j1]? You've been carrying that ice box for quite a while."
    j "Hehe... I'm strong enough to carry it myself, but sure, I wouldn't mind some help. Thanks, Sweetie."

    scene ep_campout_06
    hide ep_campout_05a
    hide ep_campout_05b
    with fade

    p "It's not much farther! Right this way... Come on, let's go!"

    stop music fadeout (3.0)

    $ renpy.pause (1.0, hard=True)

    scene blackscreen with dissolve

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_grass_2.ogg"
    $ renpy.pause (5.0, hard=True)

    play music "sounds/me/m_scene_21.ogg"
    scene ep_campout_07 with dissolve

    n "Ah... Yes, FINALLY! We made it! I think that about does it, I've had all my exercise for the week! I think it's time for a LONG nap!"
    mc "You're not THAT tired are you, Natalie? You do like to exaggerate things, don't you?"

    scene ep_campout_08

    n "I'm just kidding, [mc]. I'm just getting a little rest before Penny says..."
    p "Hey, you two! Don't get comfortable just yet! We still have to set up camp!"
    n "That... I can read her like a book, can't I? Hehe!"
    mc "Heh. It seems that way."

    show ep_campout_09a with dissolve

    j "Better listen to Penny, you two! If you want dinner, you're gonna have to earn it!"

    show ep_campout_09b with dissolve

    n "I know, I know! Don't worry, I'll start the fire in no time!"
    mc "Unpacking, putting up the tent and building the fire."
    mc "Looks like you guys got your roles figured out. What would you like me to do?"

    scene ep_campout_10
    hide ep_campout_09a
    hide ep_campout_09b
    with fade

    p "Not much else to do by yourself. Just help one of us out. It'll speed up the process a little bit."
    mc "Sure, Penny. I'll get right on that."

    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    $ unclickable = True
    play music "sounds/me/m_location_6.ogg"
    show screen screen_ep_campout_1 with dissolve
    $ unclickable = False
    jump screen_ep_campout_1


label scene_julia_ep_campout_1_choice:

    hide screen screen_ep_campout_1
    scene blackscreen
    with dissolve

    $ unclickable = False

    $ renpy.pause (2.0, hard=True)

label scene_penny_ep_campout_1_choice:

    hide screen screen_ep_campout_1
    scene blackscreen
    with dissolve

    $ unclickable = False

    $ renpy.pause (2.0, hard=True)

label scene_natalie_ep_campout_1_choice:

    hide screen screen_ep_campout_1
    scene blackscreen
    with dissolve

    $ unclickable = False

    $ renpy.pause (1.0, hard=True)

    scene ep_campout_11 with dissolve

    mc "Hey, Natalie. I'm looking to be of some use around here."
    mc "Need some help building that fire?"

    scene ep_campout_12

    n "Well, it's actually a one-person job, but if you are looking to take on the easy tasks like me, then be my guest!"
    n "Let's just take our time on it. Wouldn't want to go TOO fast, else we gotta do more work! Hehe!"
    mc "Oh yeah... Good idea. Work smart, not hard. Heheh!"

    stop music fadeout (2.0)
    scene blackscreen with dissolve

    $ renpy.pause (3.0, hard=True)

    play music "sounds/me/m_scene_19.ogg"
    scene ep_campout_13 with dissolve

    mc "So, do you REALLY not like camping, Natalie?"
    n "Eh, it's alright. It's just not my thing, you know."
    n "I can't say I find much enjoyment being in the 'great outdoors'."

    scene ep_campout_14

    mc "What's not to enjoy? Peace and fresh air don’t come often. Also, it's nice to just take a break from our normal lives."
    n "Yeah, that may be what you think..."

    scene ep_campout_15

    n "But there's never any excitement out here."
    n "It's lots of work to just sit around a campfire until it's time to go to bed. Talk about BORING!"
    mc "Oh... excitement, huh? Then if that's what you're looking for..."

    scene ep_campout_16 with fade

    mc "We could always spend the night hunting for the Brightwind Banshee, that is... if she's not already hunting us."
    n "Huh?! What'chu talking about, [mc]?"

    scene ep_campout_17

    mc "Oh, you don't know? It's just a tragic story of a young woman who lived in these woods."
    mc "One night she was brutally murdered by terrible, terrible people. Her eyes were gouged before death!"
    mc "Now, when the moon rises, she wanders blindly, killing anything she can get her hands on."

    scene ep_campout_19

    n "You're... You're kidding... right?"
    mc "I don't know... Tonight, maybe we can go and find out. What do you say?"

    show ep_campout_18a with dissolve

    n "N-Nah, I-I think I'll pass on that, [mc]. It would be a total waste of time. Just another made up story to scare people... probably."

    show ep_campout_18b with dissolve

    mc "Who knows... That's really up for you to decide."
    mc "But if she's real, I'm sure her victims had their doubts too... Just like you. Heheh!"
    n "I don't think... Uhmm..."
    mc "You're looking a little pale there, Natalie. You aren't scared now, are you?"

    scene ep_campout_20
    hide ep_campout_18a
    hide ep_campout_18b

    n "S-Shut up, [mc]. I ain't 'fraid of no ghost. Now, stop with the scary stories and let's get this stupid chore done."
    mc "Alright, Natalie. I was just trying to spruce up your experience a bit, is all."
    n "Yeah.... Well, I'm not falling for it!"

    play sound "sounds/se/se_rock_1.ogg"
    show ep_campout_21a with dissolve

    $ renpy.pause()

    stop sound
    play sound "sounds/se/se_wood_1.ogg"
    show ep_campout_21b with dissolve

    $ renpy.pause()

    stop sound
    play sound "sounds/se/se_lighter_1.ogg"
    show ep_campout_21c with dissolve

    $ renpy.pause()

    scene blackscreen
    hide ep_campout_21a
    hide ep_campout_21b
    hide ep_campout_21c
    with dissolve

    play sound "sounds/se/se_fire_2.ogg"
    scene ep_campout_22 with dissolve

    n "There we go! Now, that's a campfire. We're gonna stay warm all night."
    mc "Yeah, we do make a good team. That thing's gonna burn for hours."

    scene ep_campout_23 with dissolve

    n "Alright, [mc]. I think our job here is done. I'm gonna go hide away and avoid any more manual labor if I can. See ya!"
    mc "Heh... Always trying to avoid work, aren't ya? See ya later, Natalie."

    stop music fadeout (5.0)
    scene blackscreen with dissolve

    $ ep_campout_1_choice = "NATALIE"

    $ renpy.pause (2.0, hard=True)

    jump scene_ep_campout_campfire

#######################################

label scene_ep_campout_campfire:

    scene ep_campout_24a with Dissolve (2.0)

    $ renpy.pause (2.0, hard=True)

    scene ep_campout_24b with Dissolve (2.0)

    $ renpy.pause (3.0, hard=True)

    scene blackscreen with dissolve

    $ renpy.pause (4.0, hard=True)

    play music "sounds/me/m_scene_24.ogg"
    scene ep_campout_25 with dissolve

    $ renpy.pause()

    show ep_campout_26a with dissolve

    j "Ah... I do love the nightlife of the deep forest. It's so quiet and soothing to the ear."

    show ep_campout_26b with dissolve

    p "Yeah... So very different to that of in town."
    p "But enjoy it while you can, because you never know how long a place like this will last."
    mc "I wouldn't be so worried. You really think this place won't be here anytime soon?"

    scene ep_campout_27
    hide ep_campout_26a
    hide ep_campout_26b
    with fade

    p "Well, look at how much things have changes in a span of twenty years. This town is looking more like a city every day."
    p "Over half the forest has been cut down to make way for more businesses. It's only a matter of time until they have their eyes set on this place."
    n "See, that's why I love the beach. There's no need to worry about that. It's not like you can just cut down the ocean! Hehe!"

    scene ep_campout_28

    p "Look here, Missy. The beach environment is just as fragile as the forest!"
    n "Oh, God! Here we go..."
    p "Without proper care and attention, our little beach can meet the same fate as the other places around here. Destroyed!"
    n "I know... I know, Penny. You don't have to keep repeating yourself..."
    j "Okay! I think it's time we had dinner. Seems everyone's getting a little too 'hangry' around here."

    scene ep_campout_29 with fade

    mc "Good idea, [j1]. Wouldn't want a stupid fight like this to ruin the trip, heh."
    j "You know Penny and Natalie... Always finding one way or another to argue with each other."

    scene ep_campout_30a with dissolve

    j "But you know a big, delicious wiener is more than enough to keep the girls distracted. Hehe!"

    play sound "sounds/se/se_slap_1.ogg"
    show ep_campout_30b with dissolve

    n "Jeez... [j1]! Why do you have to say it like that!"

    stop music fadeout (3.0)
    scene blackscreen
    hide ep_campout_30b
    with dissolve

    $ renpy.pause (3.0, hard=True)

    play music "sounds/me/m_scene_10.ogg"
    scene ep_campout_31 with dissolve

    $ renpy.pause()

    scene ep_campout_32 with dissolve

    p "Ain't nothing like a fire-roasted hotdog on a camping trip. Simple and easy cleanup!"
    j "Yep, and it's nice to take a break from cooking a meal every once in a while."

    scene ep_campout_33

    p "Pfft, don't act like you don't enjoy cooking. You won't ever let me come close to cooking a meal for us at home."
    j "And for good reason, too. Everyone has their skills, I'm just not so sure cooking is one of yours."
    p "You really think so, huh? I beg to differ. How about a second opinion..."

    scene ep_campout_34 with dissolve

    p "Natalie... What do you think? I can find my way around a frying pan, can't I?"
    stop music fadeout (2.0)
    $ renpy.pause (2.0, hard=True)
    j "...Natalie?"

    show ep_campout_a1 with dissolve
    play music "sounds/me/m_thinking.ogg"

    $ renpy.pause()

    j "Hello...? Natalie?!"
    p "Earth to Natalie. Do you read me?"

    show ep_campout_35a with dissolve

    p "Natalie, snap out of it and take that stupid hot dog out of your mouth!"
    p "Can't you be normal for just one night without doing something weird?"

    show ep_campout_35b with dissolve
    hide ep_campout_a2

    n "Huh, what's the problem? This is how I always eat a hot dog! I like to savor it."
    n "Why should you care about the way I eat?"
    p "Well, to us, it looks like you're deepthroating that thing! A little bit inappropriate, don't you think?"

    scene ep_campout_36
    hide ep_campout_35a
    hide ep_campout_35b
    with dissolve

    n "Not my problem... You could look away if you'd like."
    p "Urgh! You seeing this? The nerve of this girl!"
    j "Calm down, Penny. It's okay! Let Natalie eat her dinner however she wants."
    n "Yes! Thank you, [j1]!"
    stop music fadeout (1.0)
    scene blackscreen with dissolve
    $ renpy.pause (1.0, hard=True)
    play music "sounds/me/m_scene_21.ogg"
    scene ep_campout_37 with dissolve

    j "Besides, she may be on to something. Maybe, WE are the ones that have been eating these all wrong."
    n "[j1]? What are you getting at?"
    j "Kids these days always finding new, hip ways to do things. Maybe, I should give it a shot."
    p "OH! I think I understand now..."

    scene ep_campout_38 with dissolve

    p "It's how you savor that tasty fiery flavor. Mind if I give it a try too?"
    $ camera_picture_ready = 0
    if picture_epcampout_1 == 0:
        play sound "sounds/se/se_ding_1.ogg"
        show screen camera_scene_picture_ep_campout_1
        $ renpy.pause (1.0, hard=True)

    show ep_campout_39a with dissolve

    n "Oh, I know what you're doing! Trying to make fun of me for the way I eat?!"

    show ep_campout_39b with dissolve

    j "Go ahead, Honey. Be my guest..."
    p "Thanks, baby. Mmm... I can't wait to get a taste of this big, juicy wiener."
    n "Pfft! That's so mature of you guys! Grow up!"

    show ep_campout_a2 with dissolve

    $ renpy.pause()

    j "Oh, yes... So delicious. I could suck on this baby for hours."
    n "Stop it, guys! This is top level cringe!"
    p "You got that right. Mmph! The juices... So tender... So delicious!"

    if picture_epcampout_1 == 0:
        hide screen camera_scene_picture_ep_campout_1 with dissolve
    else:
        hide screen camera_scene_picture_ep_campout_1

    if camera_picture_ready == 1:
        stop music fadeout (3.0)
        $ renpy.pause (2.0, hard=True)
        play sound "sounds/se/se_camera_1.ogg"
        show whitescreen
        $ renpy.transition (Fade (.10, 0.0, .10, color="#fff"))
        $ renpy.pause (1, hard=True)
        hide whitescreen
        $ renpy.transition (Dissolve (0.5))
        $ renpy.pause (2.0, hard=True)
        scene blackscreen
        hide ep_campout_a1
        with dissolve
        $ renpy.pause (1.0, hard=True)

        play music "sounds/me/m_scene_11.ogg"
        scene ep_campout_40 with dissolve
        p "Huh? What was that?!"
        mc "Oh yeah... This is going to do nicely."
        j "[mc]? Did... Did you just snap a photo?"

        if picture_ep_campout_1 >= 1:
            scene ep_campout_41
            show picture_obtained
            with dissolve
        else:
            scene ep_campout_41 with dissolve

        mc "Yeah, I did. It came out rather well, if I do say so myself."
        mc "I must say, you two are VERY photogenic! Haha!"

        if picture_ep_campout_1 == 0:

            python:
                picture_epcampout1 = Item("Photo", element="clothing", image="gui/inv_epcampout1.png", cost=7)

            $inventory2.add(picture_epcampout1)
            $ picture_epcampout_1 = 1
            $ pictures_developed += 1

        play sound "sounds/se/se_highfive_1.ogg"
        scene ep_campout_42
        hide picture_obtained

        n "Nice one, [mc]! That's what they get for making fun of me!"
        mc "Penny did say to always be ready to capture a memory. This one will stay with me forever!"
        j "Hehe, they caught us off-guard, didn't they?"
        p "Oh, God... What have we done. That's what I get for playing along. Talk about a backfire."

        scene ep_campout_43 with dissolve

        j "Just so you know, that one IS NOT going into the photo album. No sirree!"
        mc "Didn't plan on it. I'm keeping this one for my personal collection!"
        n "Don't let them get their hands on it, [mc]. They'll probably try and delete it!"
        p "You two are TOO much, sometimes. hehe!"

        stop music fadeout (5.0)

        $ renpy.pause (2.0, hard=True)

        scene blackscreen with dissolve

        $ renpy.pause (3.0, hard=True)

    else:

        scene ep_campout_44
        hide ep_campout_a1
        with fade

        n "Okay! Okay! I'll eat however you want me to! Please just... Stop doing whatever it is you're doing!"
        p "You promise?!"
        n "Yes... Yes! I promise! Just take that hot dog out of your mouth."
        n "Seeing your [f3] sucking on a wiener is more than I can ever take!"

        scene ep_campout_45 with dissolve

        p "Good! Then take a bite and swallow like a good girl, okay?"
        n "Yeah... Yeah! As you wish... Penny."
        j "Sorry you had to witness that, [mc]. Just had to teach [n3] a lesson."
        mc "No, no... That was, uhmmm... Good. I was very much entertained... Heh!"

        stop music fadeout (5.0)
        $ renpy.pause (2.0, hard=True)

        scene blackscreen with dissolve

        $ renpy.pause (3.0, hard=True)


    play music "sounds/me/m_scene_10.ogg"
    scene ep_campout_46 with dissolve

    n "Well, I think I've done enough socializing for one night. I think I'll just go hang out in my tent until it's time for bed."
    j "Go right on ahead, Sweetie. I know how much you like your alone time."
    p "It is getting pretty dark, and I do want to get a little hike in before bed."

    play sound "sounds/se/se_cooleropen_1.ogg"
    scene ep_campout_47 with fade

    mc "A hike, huh? At this time of night?"
    p "Yeah, I enjoy the cool air and the dark atmosphere."
    mc "You're not gonna get lost, are you? This place can be a maze, sometimes. Especially, at night."

    scene ep_campout_48 with dissolve

    j "Nah, Penny can handle herself. I'm sure she'll be fine."
    p "Yeah, I won't be gone long. You're always welcome to join, [mc], but I'm sure these two wouldn't mind the company, as well."
    mc "Alright, I'll see what I'm in the mood to do."

    stop music fadeout (2.0)

    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    $ unclickable = True
    play music "sounds/me/m_location_5.ogg"
    show screen screen_ep_campout_2 with dissolve
    $ unclickable = False
    jump screen_ep_campout_2

############################

label scene_penny_ep_campout_2_choice:

    $ unclickable = True
    scene blackscreen
    hide screen screen_ep_campout_2
    with dissolve

    $ renpy.pause(2.0, hard=True)

    scene ep_campout_49 with dissolve

    mc "Hey, Penny. I'd like to take you up on that offer."
    mc "A hike sounds pretty good, right now. If you don't mind..."

    scene ep_campout_50

    p "Of course! You sure you're up to the task? The woods can be a bit spooky at this time of night."
    mc "Pfft! It's not the first time I've been here after dark, you know. It's just nature!"

    scene ep_campout_51 with dissolve

    p "Alright, Well... Let's get going then. I'm a fast hiker. You better keep up!"
    mc "I'm quick on my feet. There's no way I'll be slowing you down."
    p "Hehe! We'll see about that!"

    stop music fadeout (3.0)
    scene blackscreen with dissolve

    $ renpy.pause (5.0, hard=True)

    play music "sounds/me/m_scene_20.ogg"
    scene ep_campout_52 with dissolve

    $ renpy.pause()

    scene ep_campout_53 with dissolve

    p "I do enjoy these long walks in the deep, dark forest. Just hearing all the different wildlife is something special."
    mc "Yeah, it is quite nice. You seem to know where you're going. You do these often?"
    p "Well, whenever I can. I spent a lot of time here growing up. Lots of memories..."
    p "I know these woods like the back of my hand. It can be quite magical, at times."

    show ep_campout_54a with dissolve

    mc "Magical, huh? Why would you use a word like that in a place like this?"

    show ep_campout_54b with dissolve

    p "I just know of some places around here that fit that description quite well."
    mc "Really... Uhmmm... Like what?"

    scene ep_campout_55
    hide ep_campout_54a
    hide ep_campout_54b
    with dissolve

    p "Come! It's not too far. Follow me and I'll show you!"
    mc "Alright, I'm right behind ya!"
    mc "(She's not talking about what I think she's talking about, is she?)"

    scene blackscreen with dissolve

    $ renpy.pause (3.0, hard=True)

    scene ep_campout_56 with dissolve

    p "Alright, we're here! It's beautiful, isn't it?"
    mc "Oh, yeah... It is quite... magical."

    scene ep_campout_57 with dissolve

    p "Seeing as the whole other side of town has been deforested, it's the only natural body of water we have left."
    mc "Interesting, I never knew this place was here."
    p "Yeah, not many do, thank God!"

    play sound "sounds/se/se_splash_1.ogg"
    scene ep_campout_58

    mc "(I was worried she was talking about somewhere else. Somewhere ACTUALLY magical, heh.)"
    p "Oh! That's surprising!"
    p "Summer is just beginning, but this water is already quite warm."

    stop music fadeout (2.0)
    show ep_campout_59a with dissolve

    p "Hey, [mc]..."
    $ renpy.pause (1.0, hard=True)
    play music "sounds/me/m_scene_11.ogg"
    p "Wanna go for a little swim?"

    show ep_campout_59b with dissolve

    mc "What... Really?! A swim? At this time of night?"
    p "Yeah, why not? It'll be quick and we'll be dry by the time we get back."

    scene ep_campout_60
    hide ep_campout_59a
    hide ep_campout_59b
    with fade

    mc "Well, sure! I could go for a nice swim!"
    p "Great! This is gonna be fun. Just strip down to your boxers and let's hop right on in!"

    play sound "sounds/se/se_zipper_2.ogg"
    scene ep_campout_61 with fade

    $ renpy.pause()

    scene ep_campout_62 with dissolve

    $ renpy.pause()

    play sound "sounds/se/se_water_1.ogg"
    scene ep_campout_63 with vpunch

    $ renpy.pause()

    play sound "sounds/se/se_splash_3.ogg"
    scene ep_campout_64 with dissolve

    $ renpy.pause()

    scene ep_campout_65 with dissolve

    p "Ah... Yes... SO refreshing. I really needed that."

    $ renpy.pause (1.0, hard=True)

    stop music fadeout (2.0)

    scene blackscreen with dissolve

    $ renpy.pause (2.0, hard=True)

    play music "sounds/me/m_scene_24.ogg"
    scene ep_campout_66 with dissolve

    mc "This was such a good idea. Very soothing indeed, I'm glad you suggested it."
    p "Oh yeah, I could never pass up an opportunity for a nice, relaxing dip."
    mc "Well, I'm relieved knowing you're confident enough to strip down and just hop in a lake in the middle of the night."
    p "This is nothing, [mc]. You may not realize, but I'm a lot more adventurous than you give me credit for."

    show ep_campout_67a with dissolve

    mc "Really... How so? What exactly have you done that could be so 'adventurous' in a place like this?"

    show ep_campout_67b with dissolve

    p "Hmm... What's it to you, [mc]? Why the sudden interest?"
    mc "Oh, I don't know... Just curious, is all?"

    scene ep_campout_68
    hide ep_campout_67a
    hide ep_campout_67b

    p "Well, if you have to know, this really isn't the first time I've been in this lake."
    p "Nor is swimming in my bra and panties the most risqué."

    scene ep_campout_69 with dissolve

    p "I used to come out here, shed off all my clothes..."
    p "And spend my day jumping off a few rocks here and there, swim a few laps or just lie around in the buff."
    mc "Skinny dipping, huh? I'm sure that was a lot of fun."

    scene ep_campout_70 with dissolve

    p "Very much so. I would just float around for hours on end with the water lapping at my bare skin."
    mc "Oh yeah... I'm sure that would feel quite nice."

    scene ep_campout_71

    mc "BUT I'm sure that's all in the past. You've grown up and I'm sure you don't do things like that anymore."
    p "And what makes you say that? That's pretty presumptuous of you to think I wouldn't."

    scene ep_campout_72

    mc "Well, if it's something you still do, then what's stopping you now?"
    p "There's an obvious explanation to why I'm not. You know that."
    mc "You think so? Because I don't really see the harm in it. It is dark, after all."
    p "Hmm... Well..."

    scene ep_campout_73 with dissolve

    p "It has been quite some time since I did it. I certainly wouldn't mind getting a little more comfortable..."
    mc "So, why don't you then?"

    show ep_heart_2_1:
        alpha 0.0 xpos 20 ypos 270
        linear 2.0 alpha 1.0 xpos 20 ypos 328
    show ep_heart_2_2:
        alpha 0.0 xpos 399 ypos 386
        linear 2.0 alpha 1.0 xpos 399 ypos 328
    show ep_heart_1_1:
        alpha 0.0 xpos 782 ypos 270
        linear 2.0 alpha 1.0 xpos 782 ypos 328
    show ep_heart_1_2:
        alpha 0.0 xpos 1161 ypos 386
        linear 2.0 alpha 1.0 xpos 1161 ypos 328
    show ep_heart_1_3:
        alpha 0.0 xpos 1541 ypos 270
        linear 2.0 alpha 1.0 xpos 1541 ypos 328
    with dissolve

    $ renpy.pause (4.0, hard=True)

    if relationship_status_present_penny >= 1:
        show ep_heart_3_1:
            xpos 20 ypos 328
        with dissolve

    if relationship_status_present_penny >= 2:
        show ep_heart_3_2:
            xpos 399 ypos 328
        with dissolve

    if relationship_status_present_penny >= 3:
        show ep_heart_3_3:
            xpos 782 ypos 328
        with dissolve

    if relationship_status_present_penny >= 4:
        show ep_heart_3_4:
            xpos 1161 ypos 328
        with dissolve

    if relationship_status_present_penny >= 5:
        show ep_heart_3_5:
            xpos 1541 ypos 328
        with dissolve

    if relationship_status_present_penny < 2:
        play sound "sounds/se/se_buzzer_2.ogg"
        $ renpy.pause()
    else:
        play sound "sounds/se/se_chime_1.ogg"
        ic "You meet the requirements to progress, but the continuation of this scene hasn't been created yet. It will soon. Sorry!"

    hide ep_heart_1_1
    hide ep_heart_1_2
    hide ep_heart_1_3
    hide ep_heart_1_4
    hide ep_heart_1_5
    hide ep_heart_2_1
    hide ep_heart_2_2
    hide ep_heart_2_3
    hide ep_heart_2_4
    hide ep_heart_2_5
    hide ep_heart_3_1
    hide ep_heart_3_2
    hide ep_heart_3_3
    hide ep_heart_3_4
    hide ep_heart_3_5
    with dissolve

    $ renpy.pause (2.0, hard=True)

    if relationship_status_present_penny >= 3:
        jump scene_penny_ep_campout_2_choice_continued_1
    else:
        stop music fadeout (1.0)
        scene blackscreen with dissolve
        $ renpy.pause (0.5, hard=True)
        play music "sounds/me/m_scene_22.ogg"
        scene ep_campout_74 with dissolve

        p "Well, because that would be HIGHLY inappropriate! What would [j3] say if she found out?"
        p "That is one conversation I would very much like to avoid."
        mc "(Damn it... I was SO close. She almost gave in to the idea.)"

        scene ep_campout_75 with fade

        p "Anyways, we've been out here long enough."
        p "I think it's about time we head back before they start getting worried."
        mc "Alright, fine... If you say so."

        scene ep_campout_76a with dissolve

        p "Oh, and don't go telling everyone about our little spot, okay? I wouldn't want everyone to find out about it."

        show ep_campout_76b with dissolve

        mc "Yeah, yeah... Of course, Penny. It'll be our little secret."

        if wforest_present_lake == 0:
            play sound "sounds/se/se_notif_1.ogg"
            show newlocation_wforest_lake with dissolve
            $ renpy.pause()
            hide newlocation_wforest_lake with dissolve
            $ renpy.pause (0.5, hard=True)
            $ wforest_present_lake = 1

        p "Good! Now, come on... Get dressed and let's head out!"

        stop music fadeout (2.0)

        scene blackscreen
        hide ep_campout_76b
        with dissolve

        $ renpy.pause (4.0, hard=True)


    play music "sounds/me/m_scene_20.ogg"
    scene ep_campout_77 with dissolve

    $ renpy.pause()

    scene ep_campout_78 with fade

    j "There you guys are! I was wondering when you were going to get back."
    p "Sorry we were gone for so long, baby. We just took a little detour, is all."
    j "Did you have fun, Sweetie? I know Penny can be a little adventurous when she's out and about in nature."
    mc "Oh yeah! It was pretty fun. A nice and refreshing hike does the body good."

    scene ep_campout_79 with dissolve

    p "*Muah* Hope we didn't make you worry. I know how you can get sometimes."
    j "Hehe! Not at all. I was far too busy drinking to have the time to dwell on that particular 'what if'."
    j "I'm just glad you both made it back safe, and had a good time."

    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    scene ep_campout_80 with dissolve

    j "Alright, well... I think that just about does it for today. I'm tipsy and exhausted."
    p "Yeah, it is getting to be about that time. Wouldn't do us good tomorrow if we stay up any later than this."
    mc "Same... I'm getting tired, as well. I think I'll go and hit the sack."

    scene ep_campout_81 with fade

    mc "(So exhausted... Today has been a long day, but it was pretty damn fun to get away from it all once in a while.)"
    mc "(I'm gonna sleep like a baby tonight. That's for sure.)"

    show ep_campout_82a with dissolve

    p "Alright, we're off to bed. Goodnight you two!"
    j "Goodnight! Don't let the bedbugs bite!"

    show ep_campout_82b with dissolve

    n "Yeah, yeah... Goodnight [j1]! Goodnight, Penny!"

    show ep_campout_82c with dissolve

    mc "Night everyone..."

    stop music fadeout (3.0)

    scene blackscreen
    hide ep_campout_82a
    hide ep_campout_82b
    hide ep_campout_82c
    with dissolve

    $ renpy.pause (2.0, hard=True)

    show ep_campout_83 with dissolve

    $ renpy.pause (3.0, hard=True)

    scene blackscreen with dissolve

    $ renpy.pause (3.0, hard=True)

    if ep_campout_1_choice == "NATALIE":
        jump ep_campout_night_natalie
    elif ep_campout_1_choice == "JULIA":
        jump ep_campout_night_julia
    elif ep_campout_1_choice == "PENNY":
        jump ep_campout_night_penny


###########################################


label ep_campout_night_natalie:

    image ep_campout_a3 = Movie(channel="movies/scene_ep_campout/ep_campout_a3.webm", play="movies/scene_ep_campout/ep_campout_a3.webm")

    n "[mc]..."

    $ renpy.pause (2.0, hard=True)

    n "Psst! Hey... [mc]!"

    $ renpy.pause (2.0, hard=True)

    scene ep_campout_84a with dissolve

    $ renpy.pause (1.0, hard=True)

    play music "sounds/me/m_scene_16.ogg"
    show ep_campout_84b with Dissolve (3.0)

    n "[mc]? Psst! A-Are you awake in there?"
    mc "Huh... Mmph... W-Who is it...?"

    scene blackscreen
    hide ep_campout_84b
    with dissolve

    $ renpy.pause (1.0, hard=True)

    scene ep_campout_85 with dissolve

    $ renpy.pause (0.5, hard=True)

    n "It's just me. I-Uh... Came to check in on ya. Is everything okay in here?"
    mc "Uh... Yeah? I was actually sound asleep. You shouldn't even be awake right now."
    n "I-Uhmmm... Couldn't sleep. So, I thought I'd stop by and see how you were doing."
    n "Mind if I come in for a bit?"
    mc "No, go on ahead..."

    scene ep_campout_86 with fade

    mc "But tell me, what's the REAL reason you're in here, huh? It's not like you to take my well-being into consideration."
    n "Alright, you caught me! I just wanted to hang out. Just the two of us... [f5] to [f4], you know?"

    stop music fadeout (0.5)
    play sound "sounds/se/se_run_1.ogg"

    scene ep_campout_87 with hpunch

    $ renpy.pause (2.0, hard=True)

    play music "sounds/me/m_scene_22.ogg"
    scene ep_campout_88 with hpunch

    $ renpy.pause (0.5, hard=True)
    n "Oh, my God! What was that! Did you hear that?! There's something out there!"
    mc "Uh... Yeah, I did. But we're in the middle of the forest. It's probably just some critter passing by."

    scene ep_campout_89 with dissolve

    n "Are you sure? But what if it's... you know..."
    mc "Wait a minute... You're scared, aren't you?"
    mc "You're afraid the big bad Brightwind Banshee is gonna get ya, huh?"
    n "Y-Yeah... So, what if I am?!"

    scene ep_campout_90

    mc "You know, I was just kidding, Natalie. I was just trying to bring a little excitement while we're out here."
    mc "There's nothing to worry about. That local folktale is just a myth."
    n "B-But... What if it's not, huh? You've seen all those scary movies! The doubters are always the one's that get picked off first."
    mc "Oh, Jeez... Now you're just being ridiculous!"

    scene ep_campout_91

    n "This is all your fault, [mc]. If you didn't tell me that story, I'd be sound asleep in my tent right now!"
    mc "Well, what do you want me to do? It's not like I can convince you enough to calm down."
    n "I know what you're gonna do..."

    scene ep_campout_92

    n "You're gonna let me sleep in here tonight! No way am I going back out there alone."
    mc "Pfft! Alright, if it'll make you stop whining and go to sleep, then that's fine with me."

    scene ep_campout_93 with dissolve

    n "Good, and thanks. My anxiety is bad enough as it is. I wouldn't be able to sleep another wink, otherwise."
    mc "Eh... I get it, Natalie. Just get some sleep. Goodnight!"
    n "Night, [mc]..."

    stop music fadeout (2.0)
    scene blackscreen with dissolve
    $ renpy.pause (2.0, hard=True)

    scene ep_campout_24b with dissolve

    $ renpy.pause (2.0, hard=True)

    scene ep_campout_24a with Dissolve (2.0)

    $ renpy.pause (2.0, hard=True)

    scene blackscreen with dissolve

    $ renpy.pause (3.0, hard=True)

    play music "sounds/me/m_scene_20.ogg"
    scene ep_campout_94 with dissolve

    $ renpy.pause()

    #soundeffect

    $ renpy.pause (2.0, hard=True)

    scene ep_campout_95a with dissolve

    j "Wakey wakey, [mc]. The sun has risen and morning has sprung."
    j "It's time to get up and start packing."

    show ep_campout_95b with dissolve

    n "*Yawn* - (Blah, morning already? At least I was able to sleep.)"
    n "(I better get up before I pass out, again.)"

    scene ep_campout_a3a with fade
    hide ep_campout_95b

    n "(Huh? What the hell is that I'm feeling?)"
    n "(A squirrel didn’t' somehow find its way in here, did it?)"

    stop music fadeout (5.0)
    show ep_campout_a3

    $ renpy.pause (3.5, hard=True)

    scene ep_campout_a3b
    hide ep_campout_a3

    $ renpy.pause (1.0, hard=True)

    show ep_heart_2_1:
        alpha 0.0 xpos 20 ypos 270
        linear 2.0 alpha 1.0 xpos 20 ypos 328
    show ep_heart_2_2:
        alpha 0.0 xpos 399 ypos 386
        linear 2.0 alpha 1.0 xpos 399 ypos 328
    show ep_heart_2_3:
        alpha 0.0 xpos 782 ypos 270
        linear 2.0 alpha 1.0 xpos 782 ypos 328
    show ep_heart_1_2:
        alpha 0.0 xpos 1161 ypos 386
        linear 2.0 alpha 1.0 xpos 1161 ypos 328
    show ep_heart_1_3:
        alpha 0.0 xpos 1541 ypos 270
        linear 2.0 alpha 1.0 xpos 1541 ypos 328
    with dissolve

    $ renpy.pause (4.0, hard=True)

    if relationship_status_present_natalie >= 1:
        show ep_heart_3_1:
            xpos 20 ypos 328
        with dissolve

    if relationship_status_present_natalie >= 2:
        show ep_heart_3_2:
            xpos 399 ypos 328
        with dissolve

    if relationship_status_present_natalie >= 3:
        show ep_heart_3_3:
            xpos 782 ypos 328
        with dissolve

    if relationship_status_present_natalie >= 4:
        show ep_heart_3_4:
            xpos 1161 ypos 328
        with dissolve

    if relationship_status_present_natalie >= 5:
        show ep_heart_3_5:
            xpos 1541 ypos 328
        with dissolve


    $ renpy.pause (0.5, hard=True)

    if relationship_status_present_natalie >= 3:

        play sound "sounds/se/se_chime_1.ogg"
        $ renpy.pause()

        hide ep_heart_1_1
        hide ep_heart_1_2
        hide ep_heart_1_3
        hide ep_heart_1_4
        hide ep_heart_1_5
        hide ep_heart_2_1
        hide ep_heart_2_2
        hide ep_heart_2_3
        hide ep_heart_2_4
        hide ep_heart_2_5
        hide ep_heart_3_1
        hide ep_heart_3_2
        hide ep_heart_3_3
        hide ep_heart_3_4
        hide ep_heart_3_5
        with dissolve
        jump ep_campout_night_natalie_continued

    else:

        play sound "sounds/se/se_buzzer_2.ogg"
        $ renpy.pause()

        hide ep_heart_1_1
        hide ep_heart_1_2
        hide ep_heart_1_3
        hide ep_heart_1_4
        hide ep_heart_1_5
        hide ep_heart_2_1
        hide ep_heart_2_2
        hide ep_heart_2_3
        hide ep_heart_2_4
        hide ep_heart_2_5
        hide ep_heart_3_1
        hide ep_heart_3_2
        hide ep_heart_3_3
        hide ep_heart_3_4
        hide ep_heart_3_5
        with dissolve

        play music "sounds/me/m_scene_21.ogg"
        n "(Oh, my God...)"

        scene ep_campout_96 with dissolve

        n "(Has [mc] been grasping onto my breast all night long?!)"
        n "(Mmph! This is what I get for not wearing a bra to bed, but who does that?!)"

        scene ep_campout_97 with dissolve

        n "(Shit! I can't let him wake up and see me like this. It'll be WAY too awkward. For the both of us...)"
        n "(Just gotta move him over... Nice and slow...)"

        scene ep_campout_98 with dissolve

        n "(There we go... It's like it never happened.)"
        n "*Phew* - (That was a close one.)"

        scene blackscreen with dissolve

        $ renpy.pause (2.0, hard=True)

        scene ep_campout_99 with dissolve

        mc "*Yawn* - What time is it?"
        n " Good morning, Sleepyhead. It's time to get up, that's what time it is."
        mc "Mmph... Okay. After all that, were you able to sleep well last night?"
        n "Yeah, I did actually. Thanks for letting me stay in here. I wouldn't have been able to, otherwise."
        mc "*Yawn* - Yeah... No problem."

        scene ep_campout_100

        mc "Mmph... But why in the hell does my hand feel all sore suddenly?"
        mc "My muscles feel like they've been going at it all night. I must have slept on it wrong."
        n "Yeah... That's OBVIOUSLY the case. I'm sure you'll be fine."

        scene ep_campout_101 with dissolve

        n "I'm just gonna go ahead and sneak out of here."
        n "Best to avoid any odd questions [j4] and Penny may have for us if they found out we slept in the same tent."
        mc "Yeah, good idea, Natalie. I'll see ya in a bit."
        n "See ya, [mc]."

        stop music fadeout (2.0)
        scene blackscreen with dissolve

        jump ep_campout_end


image epcampout_natalietitjob_a1a = Movie(channel="movies/scene_ep_campout/epcampout_natalietitjob_a1a.webm", play="movies/scene_ep_campout/epcampout_natalietitjob_a1a.webm")
image epcampout_natalietitjob_a1b = Movie(channel="movies/scene_ep_campout/epcampout_natalietitjob_a1b.webm", play="movies/scene_ep_campout/epcampout_natalietitjob_a1b.webm")
image epcampout_natalietitjob_a2a = Movie(channel="movies/scene_ep_campout/epcampout_natalietitjob_a2a.webm", play="movies/scene_ep_campout/epcampout_natalietitjob_a2a.webm")
image epcampout_natalietitjob_a2b = Movie(channel="movies/scene_ep_campout/epcampout_natalietitjob_a2b.webm", play="movies/scene_ep_campout/epcampout_natalietitjob_a2b.webm")

label ep_campout_night_natalie_continued:

    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    play music "sounds/me/m_scene_21.ogg"
    scene epcampout_natalietitjob_01 with hpunch

    n "[mc]? Hey, [mc]..."
    scene epcampout_natalietitjob_01 with hpunch
    n "[mc1], wake up! It's morning time!"
    mc "Hrrmmmmm... Huh?! Aww... Damn it, [n1]. Couldn't you have woken my up a little more gently? I didn't need to an elbow to the gut."
    n "Well, my bad. I didn't mean to interrupt your beauty sleep."

    scene epcampout_natalietitjob_02

    n "But it looks like you're awake now. Seeing as you have a good grip on reality, if you know what I mean. Hehe!"
    mc "Oh, shit! I, uh... Didn't realize I was doing that all night, heh. You don't mind it, do you?"
    n "Nah, not at all. You were really using the whole kitchen with all the 'spooning' and 'cupping' you were doing..."

    scene epcampout_natalietitjob_03

    n "It makes me wonder what you could have possibly been dreaming about. Were you dreaming about me, [mc1]?"
    mc "Who said I was dreaming about anything, huh? Maybe, I felt your cold, erect nipples and instinctively tried to keep you warm."
    n "Yeah. That could be it, but..."

    play sound "sounds/se/se_cloth_2.ogg"
    scene epcampout_natalietitjob_04 with vpunch

    n "Seeing as I can feel your massive erection through these thick jeans, I'm more inclined to go with my theory due to such HARD evidence."
    mc "You got me there. Heh!"
    $ renpy.pause (0.5, hard=True)
    n "Well, seeing that we're both already in such an awkward position..."

    play sound "sounds/se/se_cloth_3.ogg"
    scene epcampout_natalietitjob_05

    n "We may as well put two and two together, and embrace it. Go ahead and take your cock out. A quick titty-fuck should do the trick."
    mc "Wait... Are you being serious, right now? What if [j1] or Penny hear us?!"

    scene epcampout_natalietitjob_06 with dissolve

    n "It'll be real quick! If I wasn't such a 'scaredy-cat', I'd be sleeping in my own tent, and you wouldn't have woken up in such a stressful situation."
    n "Besides, my breasts are freezing from all this morning air. I could really use some body heat to warm them up, hehe!"

    scene epcampout_natalietitjob_07 with fade

    mc "Mhmmm, I can definitely help you with that, Natalie..."

    show epcampout_natalietitjob_08a:
        xpos 952
    with dissolve

    mc "My cock is already hot to the touch. I'll be able to warm these babies up in no time."

    scene epcampout_natalietitjob_08b
    hide epcampout_natalietitjob_08a
    with dissolve

    n "Good! Then get to pumpin'. All the friction should give the warmth I'm looking for."
    $ renpy.pause (0.5, hard=True)

    scene epcampout_natalietitjob_09 with dissolve

    mc "Mmph! How's that, [n9]? Does it feel as good for you as it does for me?"
    n "Holy shit! Your cock really is like a piping hot rod! You're weren't kidding, were you?"
    mc "See, I told you. As soon as you offered these beautiful breasts to me. It's like a switch turned on in my brain, and knew exactly what you wanted, heh."

    show epcampout_natalietitjob_a1a with dissolve

    $ renpy.pause()

    n "A switch, huh? I guess there's no limitations to what turns you on. Even when it involves your own [n8]?"

    show epcampout_natalietitjob_a1b with dissolve
    hide epcampout_natalietitjob_a1a

    $ renpy.pause()

    mc "Hey... Tits are tits. Just like the cozy feeling you get from [myyrbr] warm cock, I get from your soft breasts. It feels good no matter who it's attached to!"

    show epcampout_natalietitjob_a2a with dissolve
    hide epcampout_natalietitjob_a1b

    $ renpy.pause()

    n "Well, obviously I don't disagree with you there. Seeing as I've been fine with all we've done... So far."

    show epcampout_natalietitjob_a2b with dissolve
    hide epcampout_natalietitjob_a2a

    $ renpy.pause()

    mc "(Fuck... This feels just absolutely amazing. I REALLY want to prolong this moment, but I know we can't because...)"

    $ renpy.pause (0.5, hard=True)

    p "[mc]? Hey, [mc]! Hello...?!"

    stop music fadeout (1.0)

    scene blackscreen
    hide epcampout_natalietitjob_12b
    with dissolve

    $ renpy.pause (0.5, hard=True)

    play music "sounds/me/m_scene_49.ogg"

    scene epcampout_natalietitjob_13a
    hide epcampout_natalietitjob_a2b
    with dissolve

    p "With all that scrounging around in there, I know you heard [j3] tell you it's time to wake up."
    j "Yeah, you're not gonna get out of doing your part of the packing, Sweetie. Don't make me send Penny in there after ya!"

    show epcampout_natalietitjob_13b with Dissolve (2.0)

    mc "Y-Yeah! I-I know! I know! I'll be out in a little bit. I'm just cleaning up in here! Fluffin' my pillows! Okay?!"

    scene epcampout_natalietitjob_10 with vpunch

    mc "(Oh fuck! What terrible timing! I can't, nor shouldn't hold it in any longer. I'm about to burst!)"
    n "{i}Cleaning up, huh? More like you're about to make a mess...{/i}"

    scene epcampout_natalietitjob_11

    n "{i}How about we try and avoid that?{/i}"
    n "{i}I'll take one for the team, and get a nice, warm shot to the chest!{/i}"

    scene epcampout_natalietitjob_12a with dissolve

    mc "Mmph! (Holy shit! I'm... I'm cumming!)"

    show epcampout_natalietitjob_12b with Dissolve (2.0)

    n "(Mhmmm... So slimy, yet so cozily warm. I actually like it, hehe!)"

    $ renpy.pause (0.5, hard=True)

    p "Uhmmm... You're making quite a lot of noise in there. Are you okay?"

    show epcampout_natalietitjob_14a:
        xpos 0
    with dissolve

    mc "Y-Yeah, don't worry! I'm totally fine. I just need a moment alone, and I'll be right out, okay?"

    show epcampout_natalietitjob_14b:
        xpos 952
    with dissolve

    j "You know what, Honey? I think we may have interrupted his morning... business, if you know what I mean."
    p "Oh...? OH! Yeah, you're probably right..."

    $ renpy.pause (0.5, hard=True)

    p "Alright, Sweetie. We hear you loud and clear. You go ahead and finish up on whatever you're doing in there."
    p "We'll get back to packing up our things..."

    scene epcampout_natalietitjob_15
    hide epcampout_natalietitjob_14a
    hide epcampout_natalietitjob_14b
    with fade

    j "Hehe! That almost got awkward, didn't it?"
    p "Yeah, I guess we should have known better... Whoops!"
    $ renpy.pause (0.5, hard=True)
    n "Are... Are they finally gone?"
    mc "Yeah, looks like it. Man, that was a little too close."

    scene epcampout_natalietitjob_17 with fade

    mc "I don't mean to kick you out, but it might be best if you make your way back to your tent."
    mc "Seeing as they probably still think you're in there. Hopefully, they don't catch ya moving over."

    scene epcampout_natalietitjob_18 with fade

    n "Eh! Sneaking past them should be easy enough. In all honesty, I'd say it's more difficult trying to hide this massive cumshot you left me on my chest than not getting caught."
    mc "Pfft! I wouldn't say it's THAT big of load, is it?"

    scene epcampout_natalietitjob_19 with dissolve

    n "I don't know. You tell me, [mc1]? It definitely feels like it is."
    mc "Yeah... I guess it is. All that spooning through the night really got me packing a lot of juice."
    $ renpy.pause (0.5, hard=True)
    mc "I suppose you'll be cleaning that off now, right?"
    n "Mhmmm... Nah! I'd rather take advantage of this pearl necklace you gave me. It'll keep me warm until we get home."
    mc "God damn, Nat. That's hot just thinking about it, heh."

    $ ep_campout_natalietitjob = 1

    stop music fadeout (2.0)
    scene blackscreen with dissolve

    jump ep_campout_end



        ###############

label ep_campout_end:

    $ renpy.pause (4.0, hard=True)

    play music "sounds/me/m_scene_20.ogg"
    scene ep_campout_102 with dissolve

    j "You got it? Because from here... It doesn't look like you do."
    p "I got it... Just give me a second. And... There we go!"
    mc "Ahh... Alright, I'm up! Good morning, [j1]. Good morning, Penny."

    show ep_campout_103a with dissolve

    j "Oh! Well, good morning, Sweetie!"
    p "Ah, you're up. Well, once Natalie is up, we can start packing up and head on out."

    show ep_campout_103b with dissolve

    n "Present! I'm ready whenever you guys are. The sooner we start packing, the sooner we get out of here!"

    scene ep_campout_104
    hide ep_campout_103a
    hide ep_campout_103b
    with fade

    j "Then it looks like the gang's all here. I hope you guys had fun."
    n "It was... alright. But I'm looking forward to getting back to civilization, at last!"
    mc "It was just one day, Natalie. Was it really that bad?"
    p "She had fun; she just won't admit it. I can tell."
    j "Well, let's get started. This stuff won't pack itself. We'll be home in no time!"

    stop music fadeout (2.0)

    scene blackscreen with dissolve

    call idle_end_post_present from _call_idle_end_post_present_1
    call end_of_day_post_present from _call_end_of_day_post_present
    call day_of_week_present_forward from _call_day_of_week_present_forward_2
    $ time_of_day_present = 'MORNING'

    $ renpy.pause (5.0, hard=True)

    $ unclickable = True
    show screen screen_home_post_pbedroom with dissolve
    $ unclickable = False
    jump screen_home_post_pbedroom



























































##############################


screen camera_scene_picture_ep_campout_1:
    if camera_picture_ready == 0:
        imagebutton:
            focus_mask True
            xpos 1668 ypos 690
            idle "comp_photo_start_g"
            hover im.MatrixColor("computer/photos/comp_photo_start_h.png", im.matrix.brightness(0.15))
            at camera_scene_picture_animation
            action SetVariable("camera_picture_ready", 1) activate_sound "sounds/se/se_click_1.ogg"

        imagebutton:
            focus_mask True
            xpos 15 ypos 690
            idle "comp_photo_start_g"
            hover im.MatrixColor("computer/photos/comp_photo_start_h.png", im.matrix.brightness(0.15))
            at camera_scene_picture_animation
            action SetVariable("camera_picture_ready", 1) activate_sound "sounds/se/se_click_1.ogg"


screen screen_ep_campout_1:
    imagemap:
        ground "screen_ep_campout_1_g"




    #Julia

    imagebutton:
        focus_mask True
        xpos 175 ypos 308
        idle "julia_ep_campout_1_choice_g"
        hover At("julia_ep_campout_1_choice_g", atl_highlight)
        if unclickable == False:
            action Call ("ep_campout_scene_deny") hovered ShowTransient("label_julia") unhovered Hide("label_julia")


    #Natalie

    imagebutton:
        focus_mask True
        xpos 710 ypos 472
        idle "natalie_ep_campout_1_choice_g"
        hover At("natalie_ep_campout_1_choice_g", atl_highlight)
        if unclickable == False:
            action Jump ("scene_natalie_ep_campout_1_choice") hovered ShowTransient("label_natalie") unhovered Hide("label_natalie")


    #Penny

    imagebutton:
        focus_mask True
        xpos 1314 ypos 545
        idle "penny_ep_campout_1_choice_g"
        hover At("penny_ep_campout_1_choice_g", atl_highlight)
        if unclickable == False:
            action Call ("ep_campout_scene_deny") hovered ShowTransient("label_penelope") unhovered Hide("label_penelope")


label screen_ep_campout_1:
    show screen screen_ep_campout_1
    pause
    jump screen_ep_campout_1

####################################


label ep_campout_scene_deny:
    $ unclickable = True
    ic "This choice and scene has not been created yet."
    $ unclickable = False
    return


##############################
screen screen_ep_campout_2:
    imagemap:
        ground "screen_ep_campout_2_g"


    #Julia

    imagebutton:
        focus_mask True
        xpos 129 ypos 160
        idle "julia_ep_campout_2_choice_g"
        hover At("julia_ep_campout_2_choice_g", atl_highlight)
        if unclickable == False:
            action Jump ("scene_ep_campout_juliacampfire") hovered ShowTransient("label_julia") unhovered Hide("label_julia")



    #Natalie

    imagebutton:
        focus_mask True
        xpos 1427 ypos 466
        idle "natalie_ep_campout_2_choice_g"
        hover At("natalie_ep_campout_2_choice_g", atl_highlight)
        if unclickable == False:
            action Call ("ep_campout_scene_deny") hovered ShowTransient("label_natalie") unhovered Hide("label_natalie")

    imagebutton:
        idle "fm_ep_campout_2_light_01"
        focus_mask True
        xpos 1169 ypos 198
        at campout_flashlight_1

    #Penny

    imagebutton:
        focus_mask True
        xpos 879 ypos 67
        idle "penny_ep_campout_2_choice_g"
        hover At("penny_ep_campout_2_choice_g", atl_highlight)
        if unclickable == False:
            action Jump ("scene_penny_ep_campout_2_choice") hovered ShowTransient("label_penelope") unhovered Hide("label_penelope")



label screen_ep_campout_2:
    show screen screen_ep_campout_2
    pause
    jump screen_ep_campout_2
