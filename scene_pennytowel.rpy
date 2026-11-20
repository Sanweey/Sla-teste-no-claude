

label scene_pennytowel:

    $ unclickable = True

    scene blackscreen
    show screen blackscreen
    hide screen screen_home_post_mbedroom
    with dissolve

    $ unclickable = False

    $ renpy.pause (2.0, hard=True)

    image pennytowel_a1 = Movie(channel="movies/scene_pennytowel/pennytowel_a1.webm", play="movies/scene_pennytowel/pennytowel_a1.webm")

label gallery_scene_pennytowel:

    if gallery_in_progress == True:
        play music "sounds/me/m_location_4.ogg"

    scene pennytowel_01
    hide screen blackscreen
    with dissolve

    mc "(That's quite a lot of steam coming from in there. I don't remember our showers staying hot for anything longer than five minutes.)"
    mc "(It wouldn't hurt if I just take a quick look... right? You know, to make sure everything is alright.)"

    scene blackscreen with dissolve

    play sound "sounds/se/se_doorcreek_1.ogg"

    $ renpy.pause (2.0, hard=True)

    scene pennytowel_02b with dissolve

    mc "(The steam is so intense, but I don't hear the shower going. Did we blow a pipe or something?)"

    stop music fadeout (2.0)

    scene pennytowel_02a with Dissolve (3.0)

    play music "sounds/me/m_scene_2.ogg"
    mc "(Oh shit! I guess that's no surprise. Penny was in the shower!)"
    mc "(And is just standing there... with nothing more... than a towel.)"

    scene pennytowel_03 with fade

    p "Julia? Honey, is that you?"
    p "Since you're here, could you hand me my robe?"
    mc "I... I, uh..."

    scene pennytowel_04 with dissolve

    p "Julia? Ummm... Hello? Are you okay?"
    mc "(I, uh... better just shut my mouth and close the door.)"

    stop music fadeout (2.0)
    play sound "sounds/se/se_doorcreek_1.ogg"

    stop music fadeout (2.0)
    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    play sound "sounds/se/se_closedoor_2.ogg"

    $ renpy.pause (2.0, hard=True)

    play music "sounds/me/m_scene_10.ogg"
    scene pennytowel_05 with dissolve

    mc "(Oh, man... I'm still not used to having another person in the house.)"
    mc "(Already accidently walking in on Penny. Seeing her fresh out of the shower.)"

    scene pennytowel_06a with dissolve

    mc "(With that moist shine of the steam covering her whole body.)"

    show pennytowel_06b with Dissolve (1.0)

    mc "(Her big, radiant ass cheeks. Like eyes staring back at me.)"

    show pennytowel_06c with Dissolve (1.0)

    mc "(Her perfectly sized feet. Where even I find that mouth-watering.)"

    show pennytowel_06d with Dissolve (1.0)

    mc "(And her big perky breasts! Her nipples so hard, I bet they could cut steel.)"
    mc "(Sheesh... I'm fantasizing way too much here. But if I had the chance, I'd just...)"

    stop music fadeout (2.0)
    play sound "sounds/se/se_opendoor_4.ogg"
    show pennytowel_a1
    hide pennytowel_06a
    hide pennytowel_06b
    hide pennytowel_06c
    hide pennytowel_06d
    with dissolve

    play sound "sounds/se/se_bodyfall_3.ogg"

    $ renpy.pause (2.8, hard=True)

    scene pennytowel_a1b
    hide pennytowel_a1

    $ renpy.pause (0.5, hard=True)

    play music "sounds/me/m_scene_19.ogg"
    p "Oh, my God! [mc]?! I'm so sorry! You're not hurt, are you?!"
    mc "No... No... Uh, I'm good, Penny!"

    scene pennytowel_07 with fade

    p "Well, thank God! You really shouldn't lean all your weight on the door like that."
    p "Or else you can really hurt yourself. Here... let me help you up."

    scene pennytowel_08

    mc "No, no... I got it, Penny. I've come to realize that I'm quite prone to falling, recently. Heh!"
    p "Hmm... Okay, then. But why would you be coming into here, anyways? Shouldn't you be using your own bathroom?"
    mc "I, uh... Well, you see..."

    scene pennytowel_09

    p "Let me guess, Natalie is hogging it again? Why am I not surprised?!"
    mc "Oh... yep! You got it right on the nose, Penny. That's totally it!"
    p "I swear, she thinks it's like a secondary bedroom for her. She really needs to learn to share."

    scene blackscreen with dissolve

    play sound "sounds/se/se_roll_4.ogg"

    scene pennytowel_10 with dissolve

    p "Oh! And before you go, I've been meaning to talk to you about something, if you don't mind."
    mc "Really? Just between the two of us, huh? What is it?"
    p "Well, it's about the next few months. I know you just got done with a semester full of classes, and I'm sure you're excited to have this free time."
    p "But I just want to make sure that..."

    scene pennytowel_11 with dissolve

    p "Actually, can you turn around for a moment? I'd like to take off this towel and get into something a little more comfy."
    mc "Yeah! Of course, Penny. Go on ahead... I'm still listening."
    p "Good! Now, no peeking! It'll just be a moment!"

    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    scene pennytowel_12 with dissolve

    p "Well, anyways... As I said, I'm sure you're excited to have some free time again."
    p "And as a boy your age, I know you're EAGER to socialize with all the pretty girls around town."
    p "I bet you already have your eye on a few gems... Hmm?"

    scene pennytowel_13a with dissolve

    mc "Yeah, I've definitely met a few beauties. That's for sure!"

    show pennytowel_13c with dissolve
    show pennytowel_13f with dissolve
    show pennytowel_13d with dissolve
    show pennytowel_13g with dissolve
    show pennytowel_13e with dissolve

    $ renpy.pause (0.5, hard=True)

    mc "I just hope I get to see them again. My time with them was... rather brief."

    show pennytowel_13b with dissolve

    p "Well, I'm happy to hear that you're motivated to mingle. I wouldn't want you to be stuck inside all summer."

    scene pennytowel_14
    hide pennytowel_13b
    hide pennytowel_13c
    hide pennytowel_13d
    hide pennytowel_13e
    hide pennytowel_13f
    hide pennytowel_13g
    with dissolve

    mc "No need to worry about that, Penny. My motivations are fueled by curiosity, and I have A LOT of questions I'd like to get answered."
    mc "(Mmmm… And not only that, my curiosity fuels my desire, and I currently have a desire to know something.)"

    if gallery_in_progress == True:
        jump gallery_pennytowl_2

    play sound "sounds/se/se_notif_4.ogg"
    show screen camera_scene_picture_pennytowel_tutorial with dissolve

    $ renpy.pause (2.0, hard=True)

    show camera_picture_tutorial with dissolve

    $ renpy.pause()

    hide camera_picture_tutorial with dissolve

    $ renpy.pause (0.5, hard=True)

    show screen camera_scene_picture_pennytowel
    hide screen camera_scene_picture_pennytowel_tutorial

label camera_picture_taking_pennytowel:
    show screen camera_scene_picture_pennytowel
    pause
    jump camera_picture_taking_pennytowel

label scene_pennytowel_continued:

    hide screen camera_scene_picture_pennytowel with dissolve

    $ renpy.pause (2.0, hard=True)

label gallery_pennytowl_2:

    scene pennytowel_15 with fade

    mc "(Hmmm... Even though class is over, I think I know of a way to put my photo skills to good use.)"
    mc "(One quick, unnoticed snap wouldn't hurt. It would easily satisfy that urge, heh.)"
    p "Well, it sounds like your summer will be jam-packed, and full of adventure."

    show pennytowel_16a with dissolve

    p "Sorry if it sounds like I'm grilling you. I just wanted to make sure you're fully utilizing your time."
    p "Youth and limitless freedom don't last forever. It's important to have a good balance of leisure and responsibility."

    show pennytowel_16b with dissolve

    mc "Don't worry, Penny. I'm sure I can strike a good balance of the two."

    scene pennytowel_17
    hide pennytowel_16a
    hide pennytowel_16b
    with fade

    mc "But everyone has their flaws, and I'm no different."
    mc "For now, I'll be trying to take advantage of any opportunities that I'm given."

    scene pennytowel_18a with dissolve

    $ renpy.pause(2.0, hard=True)

    play sound "sounds/se/se_camera_1.ogg"
    show pennytowel_18b with Dissolve (0.15)
    hide pennytowel_18b with Dissolve (0.15)

    $ renpy.pause (3.0, hard=True)

    scene pennytowel_19 with fade

    p "Flaws, huh? It's funny that you word it in such a way."
    mc "Hmm? What do you mean by that?"
    p "I wouldn't call your 'urges' a flaw. I know I felt just the same way at your age."
    p "Pent up emotions... guilt from said emotions, but everything you're feeling is natural."
    p "Julia and I have NO problem with you doing what you got to do. Especially, during prime summertime!"

    scene pennytowel_20

    p "So, let's say if you find a pretty girl, and you both are in the mood..."
    p "Don't be afraid to bring her home. You're an adult. Your space is your own, and we both respect that."
    mc "Haha... I don't know about all that, Penny. Not sure if I'm comfortable doing THAT within earshot of the whole house."

    scene pennytowel_21 with dissolve

    p "Hey! There's a reason why we turned the entire downstairs into a finished basement. I'm sure very little sound, if any, will be making it through those walls."
    p "And if Natalie complains, I'll just tell her to turn up that damn stereo of hers. Hehe!"
    mc "Heh! Ummm, thanks for the comforting words. I'll keep that in mind."
    p "No problem, [mc]. Julia and I just want to make you feel at ease here. This is your home, too."
    p "We don't want you to feel like you're being held back. We sure weren't!"

    scene pennytowel_22 with fade

    p "Well, I've said more than a mouthful! I'll leave you be, as I need to take what little time I have and relax."
    p "My next set of classes are just around the corner. No Summer break for me!"
    mc "Okay, you get some much-needed rest then, Penny. I'll see you later."

    scene pennytowel_23 with fade

    mc "(Either Penny is a lot less of a hard-ass outside the classroom or [j2]'s kindness has really rubbed off on her over the years.)"
    mc "(Interesting to know that she's comfortable enough discussing such personal topics.)"

    scene pennytowel_24 with dissolve

    mc "(As for the photo, it certainly answered the burning question I had in my mind.)"
    mc "(That she rocks a nicely trimmed bush.)"

    if gallery_in_progress == True:
        return

    show camera_picture_tutorial2 with dissolve

    $ renpy.pause()

    hide camera_picture_tutorial2 with dissolve

    $ renpy.pause (1.0, hard=True)

    stop music fadeout (3.0)
    scene blackscreen with dissolve

    $ renpy.pause (2.0, hard=True)

    python:
        picture_penny1 = Item("Photo", element="clothing", image="gui/inv_picturepenny1.png", cost=7)

    $inventory2.add(picture_penny1)
    $ picture_penny_1 = 1
    $ pictures_developed += 1

    $ gallery_event_pennytowel = 1
    $ artifact_ability_questline_penny = 1

    if artifact_ability_questline_nadia == 1 and artifact_ability_questline_kimberly == 1 and artifact_ability_questline_penny == 1:
        $ artifact_ability_questline = "JULIA_ON_SWING"


    $ unclickable = True

    show screen screen_home_post_mbedroom with dissolve
    scene blackscreen

    $ unclickable = False

    jump screen_home_post_mbedroom










###########################

transform camera_scene_picture_animation:
    alpha 0.5
    easeout 0.5 alpha 1.0
    alpha 1.0
    easein 0.5 alpha 0.5
    repeat

transform camera_scene_picture_animation2:
    alpha 1.0


screen camera_scene_picture_pennytowel_tutorial:
    imagebutton:
        focus_mask True
        xpos 1668 ypos 690
        idle "comp_photo_start_g"

    imagebutton:
        focus_mask True
        xpos 15 ypos 690
        idle "comp_photo_start_g"


screen camera_scene_picture_pennytowel:
    imagebutton:
        focus_mask True
        xpos 1668 ypos 690
        idle "comp_photo_start_g"
        hover im.MatrixColor("computer/photos/comp_photo_start_h.png", im.matrix.brightness(0.15))
        at camera_scene_picture_animation
        action Jump("scene_pennytowel_continued") activate_sound "sounds/se/se_click_1.ogg"

    imagebutton:
        focus_mask True
        xpos 15 ypos 690
        idle "comp_photo_start_g"
        hover im.MatrixColor("computer/photos/comp_photo_start_h.png", im.matrix.brightness(0.15))
        at camera_scene_picture_animation
        action Jump("scene_pennytowel_continued") activate_sound "sounds/se/se_click_1.ogg"









####################
