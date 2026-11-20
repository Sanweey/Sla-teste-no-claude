
image natstudybj_a1 = Movie(channel="movies/scene_natstudybj/natstudybj_a1.webm", play="movies/scene_natstudybj/natstudybj_a1.webm")
image natstudybj_a2 = Movie(channel="movies/scene_natstudybj/natstudybj_a2.webm", play="movies/scene_natstudybj/natstudybj_a2.webm")
image natstudybj_a3 = Movie(channel="movies/scene_natstudybj/natstudybj_a3.webm", play="movies/scene_natstudybj/natstudybj_a3.webm", loop=False, image="natstudybj_a3a")

label scene_natstudybj:

label gallery_scene_natstudybj:

    if gallery_in_progress == True:
        play music "sounds/me/m_location_4.ogg"

    scene natstudybj_01 with fade
    mc "Hey! Is that your set of flash cards over there?"
    n "Uh-huh... Why do you ask? Do you want to help me study?"
    mc "Yeah, why not?! I don't have any plans for the evening, so I don't mind using my time to help you study."

    scene natstudybj_02 with dissolve

    n "Sounds good to me. I'm sure these will be on the mid-term. It doesn't hurt to get a 'refresher' on them."
    mc "Alright, then let's get started!"
    stop music fadeout (2.0)

    scene blackscreen with dissolve

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_locked_2.ogg"

    $ renpy.pause (2.0, hard=True)

    mc "Okay, let's see here... 'A chemical reaction in which energy is absorbed is called a... what?'"

    play music "sounds/me/m_scene_42.ogg"
    scene natstudybj_03 with dissolve

    n "Irt's cerld... 'Endough...ther-ic'"
    mc "Endothermic? Correct!  Next, 'The measure of the amount of mass in an object?'"

    scene natstudybj_04 with dissolve

    n "Irt's 'Erams', ovi-us-re."
    mc "'Rams'? I can't understand ya, [n1]. You shouldn't speak with your mouth full."

    scene natstudybj_05

    default scene_natstudybj_01 = "Oh, shut up! It's hard enough to talk as it is while I do this. No need to make fun of me!"
    n "[scene_natstudybj_01]"
    mc "I'm just messing around, Natalie. We all know you're good at multi-tasking, haha!"

    scene natstudybj_06

    n "Well, stop trying to make me laugh while I do this, or else I could accidently nibble on it a little too hard, hehe."
    mc "Heh. Alright, I'll keep things professional then. Let's continue..."

    show natstudybj_a1 with dissolve

    $ renpy.pause()

    mc "Okay, here's one. 'A bond that occurs between non-metals and non-metals is called a...?'"
    n "Irt's uh... a 'Co-all-ent bond'?"
    mc "Covalent bond? You got it!"

    show natstudybj_a2 with dissolve
    hide natstudybj_a1

    $ renpy.pause()

    mc "Mmph! Hmm... How about this one? 'A bond where electrons are transfered is called an...?'"
    n "Oast efin-ent-ly an 'Ionic-ond'."
    mc "Y-Yeah. That's... That's..."

    scene natstudybj_07 with hpunch

    mc "Correct! Oh, fuck! Your tonsils are tickling the tip of my cock!"
    mc "It's giving me an overwhelming urge to..."

    $ camera_picture_ready = 0

    scene natstudybj_08 with dissolve

    mc "Unload every ounce into your amazing mouth! Here it comes..."
    show whitescreen with Dissolve (0.3)
    $ renpy.pause (0.5, hard=True)
    hide whitescreen with Dissolve (2.0)

    if camera_picture_ready == 0 and picture_natstudy_1 == 0 and gallery_in_progress == False:
        play sound "sounds/se/se_ding_1.ogg"
        show screen camera_scene_picture_natstudy_1
        $ renpy.pause (1.0, hard=True)
    else:
        $ renpy.pause (0.5, hard=True)

    scene natstudybj_09 with dissolve

    mc "(Holy shit... I coated her entire mouth, and I can feel her tongue swirling around in there.)"
    mc "(Slowly gathering up all the cum. It's ticklish, yet comforting.)"

    hide screen camera_scene_picture_natstudy_1

    if camera_picture_ready == 0 and picture_natstudy_1 == 0:
        $ renpy.pause (0.3, hard=True)
    elif camera_picture_ready == 1:
        $ renpy.pause (0.5, hard=True)
        jump scene_natstudybj_picture

label scene_natstudybj_continued:

    show screen disable_player_action
    show natstudybj_a3 with dissolve

    $ renpy.pause (0.5, hard=True)
    play sound "sounds/se/se_gulp_1.ogg"
    $ renpy.pause (2.0, hard=True)
    hide screen disable_player_action
    mc "Wow... It's so satisfying to watch you so simply swallow my load like that."
    n "I've come to find the taste enjoyable. So, get used to it, because I'm sure this won't be the last."
    mc "I sure hope not!"

    scene natstudybj_10 with dissolve

    n "Well, I think we've done more than enough studying for one night. Thanks for the help, [mc2]. I really appreciate it."
    mc "No problem, Natalie. It's not exactly fun to study, but I do admire the effort you put into making it entertaining for me, heh."
    n "Yep, we end the evening with me being mentally drained, and you physically drained. Something I'm sure we're both happy with, hehe! Goodnight, [mc]."

    if gallery_in_progress == True:
        return

    stop music fadeout (2.0)
    scene blackscreen with dissolve

    call idle_end_post_present from _call_idle_end_post_present_28
    $ time_of_day_present = 'NIGHT'
    $ time_of_day_past = 'NIGHT'
    $ natalie_oralstudies = 2 # done to make people with saves rewatch

    $ renpy.pause (2.0, hard=True)

    $ unclickable = True
    show screen screen_home_post_hallway with dissolve
    $ unclickable = False
    jump screen_home_post_hallway




label scene_natstudybj_picture:

    mc "Hey, Nat. Don't swallow just yet. Take a look up here, and smile for the camera, will ya?"
    scene natstudybj_11 with fade
    n "[mc]?! Are you really trying to take a picture of me, right now?"
    mc "Of course! Penny did teach me to always capture moments you'd wish to never forget, and this is definitely one of them, heh."
    n "Oh, is that so..."
    scene natstudybj_12
    n "Then here you go! One core memory for you to fap to, hehe!"
    $ renpy.pause (0.5, hard=True)
    play sound "sounds/se/se_camera_1.ogg"
    show whitescreen with Dissolve (0.3)
    hide whitescreen with Dissolve (1.0)
    mc "Mhmmm, perfect! That's a keeper, for sure!"
    call natstudypicture_code from _call_natstudypicture_code
    show natstudybj_13a:
        xpos 0
    with dissolve
    n "Now... Can I swallow?"
    show natstudybj_13b:
        xpos 952
    with dissolve
    mc "Yep, don't let me hold you back, Natalie. Enjoy."
    n "Good, because your cum is starting to get everywhere, and I rather not have it go to waste."
    jump scene_natstudybj_continued






label natstudypicture_code:

    python:
        picture_natstudy1 = Item("Photo", element="clothing", image="gui/inv_natstudy1.png", cost=7)

    $inventory2.add(picture_natstudy1)
    $ picture_natstudy_1 = 1
    $ pictures_developed += 1
    return

screen camera_scene_picture_natstudy_1:
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






    ###################
