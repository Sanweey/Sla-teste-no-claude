

label scene_jobasement:

    $ unclickable = True
    show blackscreen
    scene blackscreen
    hide screen overworld_present
    hide screen screen_home_post_pbedroom
    with dissolve
    $ unclickable = False

    $ renpy.pause (0.5, hard=True)

    image jobasement_a1 = Movie(channel="movies/scene_jobasement/jobasement_a1.webm", play="movies/scene_jobasement/jobasement_a1.webm")
    image jobasement_a2 = Movie(channel="movies/scene_jobasement/jobasement_a2.webm", play="movies/scene_jobasement/jobasement_a2.webm")
    image jobasement_a3a = Movie(channel="movies/scene_jobasement/jobasement_a3a.webm", play="movies/scene_jobasement/jobasement_a3a.webm", loop=False)
    image jobasement_a3b = Movie(channel="movies/scene_jobasement/jobasement_a3b.webm", play="movies/scene_jobasement/jobasement_a3b.webm", loop=False)
    image jobasement_a4 = Movie(channel="movies/scene_jobasement/jobasement_a4.webm", play="movies/scene_jobasement/jobasement_a4.webm")

    scene jobasement_01 with dissolve
    hide blackscreen

    mc "(Damn... what a crazy day, but I can FINALLY take these shoes off.)"
    mc "(I still don't know how to process all this, but right now...)"

    scene jobasement_02

    mc "(All I need to do is act like nothing's different.)"
    mc "(I'm too tired to make any big decisions.)"

    scene jobasement_03 with dissolve

    mc "(Just going to lie down in a comfortable bed...)"
    mc "(And get some good-ass sleep for once.)"

    stop music fadeout (3.0)
    $ renpy.pause (2.0, hard=True)

    scene blackscreen with Dissolve (1.0)

    $ renpy.pause (5.0, hard=True)

    play music "sounds/me/m_scene_32.ogg"

    $ renpy.pause (1.0, hard=True)

    show jobasement_quote with Dissolve (2.0)

    $ renpy.pause()

    show screen disable_player_action
    hide jobasement_quote with Dissolve (2.0)

    $ renpy.pause (3.0, hard=True)

    scene jobasement_a1 with Dissolve (1.0)

    $ renpy.pause (2.0, hard=True)
    hide screen disable_player_action
    mc "(Mmph.... Fire... Death...)"
    show screen disable_player_action

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_lightning_1.ogg"
    show whitescreen with Fade(.10, 0.0, .10, color="#fff")
    hide artifact_a3a
    hide artifact_a3b
    hide artifact_a3c
    $ renpy.pause (1.0, hard=True)

    show blackscreen
    play music "sounds/se/se_fire_1.ogg"
    show screen artifact_vision_1
    hide whitescreen
    with Dissolve (0.3)

    $ vision_artifact = 1

    $ renpy.pause (4.5, hard=True)

    ##############

    stop music fadeout (1.0)
    show whitescreen
    with Fade(.10, 0.0, .10, color="#fff")
    hide screen artifact_vision_1

    $ renpy.pause (1.0, hard=True)

    scene blackscreen
    hide whitescreen
    with Dissolve (1.0)

    hide screen disable_player_action
    mc "(Ergh... Fall... Paralyze...)"
    show screen disable_player_action

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_lightning_2.ogg"
    show whitescreen with Fade(.10, 0.0, .10, color="#fff")

    $ vision_artifact = 1
    $ renpy.pause (1.0, hard=True)

    show screen artifact_vision_3
    scene blackscreen
    hide whitescreen
    with Dissolve (0.3)

    $ renpy.pause (4.5, hard=True)

    ################

    stop music
    show whitescreen
    with Fade(.10, 0.0, .10, color="#fff")
    hide screen artifact_vision_3

    $ renpy.pause (1.0, hard=True)

    scene blackscreen
    hide whitescreen
    with Dissolve (1.0)

    hide screen disable_player_action
    mc "(Mmph! Revenge... Murder...)"
    show screen disable_player_action

    $ renpy.pause (2.0, hard=True)


    play sound "sounds/se/se_lightning_1.ogg"
    show whitescreen
    hide screen artifact_vision_3
    with Fade(.10, 0.0, .10, color="#fff")

    $ renpy.pause (1.0, hard=True)

    $ vision_artifact = 1
    $ renpy.pause (1.0, hard=True)

    show screen artifact_vision_2
    scene blackscreen
    hide whitescreen
    with Dissolve (0.3)

    $ renpy.pause (1.5, hard=True)
    play music "sounds/se/se_gun_1.ogg"
    $ renpy.pause (3.0, hard=True)
    stop music
    $ renpy.pause (1.5, hard=True)

    show whitescreen with Fade(.10, 0.0, .10, color="#fff")
    hide screen artifact_vision_2

    $ vision_artifact = 1

    scene jobasement_a1
    hide whitescreen
    with Dissolve (1.0)

    $ renpy.pause (2.0, hard=True)

    hide screen disable_player_action

    mc "(Misfortune... Secrets... Regret...)"
    mc "([j1]...)"
    show screen disable_player_action

    $ renpy.pause (3.0, hard=True)

    play sound "sounds/se/se_magicdef_1.ogg"
    show artifact_a3a with Dissolve (0.3)

    show artifact_a3b with Dissolve (0.8)
    hide artifact_a3a

    scene artifact_a3a with Dissolve (0.3)
    hide artifact_a3b

    play sound "sounds/se/se_lightning_1.ogg"
    show whitescreen with Dissolve (0.3)
    hide artifact_a3a
    scene jobasement_a2
    hide whitescreen
    with Dissolve (0.3)

    $ renpy.pause (0.5, hard=True)

    scene jobasement_a2b
    voice "sounds/se/se_bodyfall_3.ogg"

    $ renpy.pause (3.0, hard=True)

    hide screen disable_player_action
    mc "Fuck! Aghh!! SHIT!"

    $ renpy.pause (1.0, hard=True)

    play sound "sounds/se/se_doorcreek_1.ogg"

    $ renpy.pause (3.0, hard=True)

    play music "sounds/me/m_scene_35.ogg"
    show jobasement_05a with Dissolve (1.0)

    hide screen disable_player_action

    $ renpy.pause (1.0, hard=True)
    j "{i}Y-You see anything, [o1]? I definitely heard something. I just know it!{/i}"
    o "{i}Not yet... It doesn't look like anything's out of the ordinary. Are you su...{/i}"

    show jobasement_05b with dissolve

    mc "God damn it, that hurt. What the fuck is happening now?"

    j "{i}*Gasp* - You hear that?!{/i}"
    o "{i}Yeah... I did, [j9]. There's definitely someone here.{/i}"

    scene jobasement_06
    hide jobasement_05a
    hide jobasement_05b
    with dissolve

    o "{i}Okay... There's no backing down now. Ready to teach the intruder a lesson?{/i}"
    j "{i}Y-Yeah! I'm ready. He messed with the wrong house! Let's show him what's up!{/i}"
    o "{i}Okay... on my mark.{/i}"

    scene jobasement_a3c with fade

    $ renpy.pause (1.0, hard=True)

    show jobasement_a3a

    play sound "sounds/se/se_doorcreek_1.ogg"
    $ renpy.pause (2.35, hard=True)
    scene jobasement_a3d
    hide jobasement_a3a

    $ renpy.pause (2.0, hard=True)

    stop music fadeout (3.0)
    o "{i}Three... Two... ONE!{/i}"

    $ renpy.pause (1.0, hard=True)

    show jobasement_a3b

    $ renpy.pause (1.7, hard=True)
    scene jobasement_a3e
    hide jobasement_a3b

    $ renpy.pause (0.5, hard=True)

    play music "sounds/me/m_scene_22.ogg"
    o "Stop right there, criminal scum!"
    j "Prepare to meet your maker, intruder!"
    mc "(OH SHIT! WHAT THE FUCK?!)"

    $ renpy.pause (1.0, hard=True)

    scene jobasement_07 with dissolve

    j "Wait a minute... [mc]?"
    o "What... the hell... are you doing here?"
    mc "Hey... ladies. Uh, why don't we put down the foreign objects before someone gets hurt."
    mc "That someone being me... of course. Heh?"

    stop music fadeout (2.0)
    scene blackscreen with dissolve

    $ renpy.pause (1.0, hard=True)

    play music "sounds/me/m_scene_19.ogg"
    scene jobasement_08 with dissolve

    j "Phew... Thank God it didn't go any further than it did. I'd feel horrible!"
    o "Yeah, a second longer and we may have busted your skull right open!"
    o "What are you doing down here anyway?"
    mc "(Mmph... I'd like to know that answer myself.)"
    j "Isn't it obvious, [o1]? [mc] here needed a place to sleep and found refuge here."

    scene jobasement_09

    mc "Y-Yeah! That's exactly the reason why I'm here! Just needed a safe place to rest. I didn't mean to intrude!"
    o "No matter the reason... sleeping in a someone's humid basement in your boxers is creepy."
    j "But where do you expect him to go? Our tiny little town doesn't even have a motel."
    j "Can't he just crash in our bedroom for the night? I'm sure we can manage something."
    o "No way! [g3] would freak if she found out we snuck some guy into the house in the middle of the night."

    show jobasement_10a with dissolve

    j "Well... if we REALLY can't bring him inside the house, then maybe we'll just have to make do with what we got."
    mc "Make do? What do you mean by that?"

    show jobasement_10b with dissolve

    o "You're trying REALLY hard to make this work..."
    o "Fine! Have it your way. What do you have in mind?"

    scene jobasement_11
    hide jobasement_10a
    hide jobasement_10b
    with dissolve

    j "{i}So what I was thinking... *Whisper* - *Whisper - *Whisper* {/i}"
    o "{i}Oh, okay... That's simple enough. I'd be okay with that. Sure.{/i}"
    mc "(Mmph... What the hell is going on? Sent back against my will with nothing but my boxers!)"

    scene jobasement_31

    mc "(And for what purpose? I'm constantly flying blind here.)"
    mc "(Urghh! Shit! This isn't just embarrassing, it's frustrating. I just don't know what I'm supposed to do.)"

    scene blackscreen with dissolve

    play sound "sounds/se/se_roll_4.ogg"
    $ renpy.pause (1.0, hard=True)

    scene jobasement_12 with dissolve

    mc "Hmm? Uh... Julia? What are you doing exactly?"
    j "Oh, nothing! Just putting together a little something for you."

    play sound "sounds/se/se_blowup_1.ogg"
    scene jobasement_13 with dissolve

    j "We understand you're from out of town and I can see why you're having trouble finding a place to sleep."
    j "And since we can't just bring you inside, we want to at least make you comfortable."
    mc "Oh! Well... thanks, girls. It's very kind of you to help me out. Heh..."

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_blowup_1.ogg"
    scene blackscreen with dissolve

    $ renpy.pause (3.0, hard=True)

    j "There we go! That should do it! You'll have a much better night's sleep now!"

    $ renpy.pause (0.5, hard=True)

    scene jobasement_14 with dissolve

    o "[j9]... sometimes, you're just TOO nice. You know that?"
    o "I mean... a guy you just met is camping out in your basement. I'm surprised you aren't at least a little cautious."
    j "Oh, shut up, Olivia! It obviously isn't like that."

    scene jobasement_15a with dissolve

    o "Well, you thought Nathan was a nice guy, and that didn't turn out so hot, huh?"

    show jobasement_15b with Dissolve (2.0)

    o "I'm just saying that your judge of character isn't ALWAYS on the mark."

    scene jobasement_16a
    hide jobasement_15b
    with dissolve

    j "Well, that was a simple mistake... okay? I learned my lesson. [mc] here isn't like that asshole."
    mc "Y-Yeah, no need to worry about me. I don't have some kind of ulterior motive."

    show jobasement_16b with Dissolve (2.0)

    mc "(Right now, all I have with me is my imagination... heh.)"

    play sound "sounds/se/se_sketch_1.ogg"
    show sketchbook_bttf_quest_unlocked with dissolve

    $ renpy.pause()

    play sound "sounds/se/se_sketch_2.ogg"
    hide sketchbook_bttf_quest_unlocked with dissolve

    $ renpy.pause (1.0, hard=True)

    scene blackscreen
    hide jobasement_16b
    with dissolve

    $ renpy.pause (1.0, hard=True)

    scene jobasement_17 with dissolve

    o "Well, either way... your bed is good to go. That pool floatie is old. Hopefully, there isn't any holes in it."
    j "It should be fine, I just hope it's comfortable enough. Just think of it as a crappy, old air mattress. Hehe!"

    scene jobasement_18 with fade

    o "Alright, Julia... We've done more than enough for him. It's time we head back upstairs and get some beauty sleep of our own. Okay?!"
    j "Okay... Okay! You don't have to be so pushy. I'm coming!"
    mc "Well, thanks for the help, girls. I'll jump right on in. You won't hear a peep from me."

    scene jobasement_19

    o "Good! I would rather avoid getting in trouble with [g3]. She may be a heavy sleeper, but if she found out you were sleeping in the basement, I'm not so sure she'd be okay with it."
    o "Well, that's enough of that. We're off to bed... Nighty night, [mc]."
    j "Goodnight, [mc]! Sleep tight! I'll come by in the morning."
    mc "Night, Olivia... Night, Julia."

    stop music fadeout (3.0)
    scene blackscreen with dissolve

    play sound "sounds/se/se_closedoor_2.ogg"

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_locked_2.ogg"

    $ renpy.pause (2.0, hard=True)

    play music "sounds/me/m_scene_5.ogg"
    scene jobasement_20 with dissolve

    $ renpy.pause (0.5, hard=True)

    mc "(Locked the door, huh? Well, it does make sense.)"
    mc "(To them I'm just some fresh face chilling in their basement. It was nice of them to help me out, though.)"

    scene jobasement_21 with dissolve

    mc "(Well, there isn't much else to do other than to go back to sleep.)"
    mc "(I'm just not too sure where I'm supposed to go from here.)"

    scene jobasement_22 with dissolve

    mc "(Whatever... I'm still super exhausted. Best to not worry about it until the morning.)"

    stop music fadeout (3.0)

    $ renpy.pause (2.0, hard=True)

    scene blackscreen with dissolve

    $ renpy.pause (4.0, hard=True)

    play music "sounds/se/se_alarm_1.ogg"
    $ renpy.pause (2.0, hard=True)

    show screen disable_player_action
    scene jobasement_25 with Dissolve (3.0)

    $ renpy.pause (2.0, hard=True)

    scene jobasement_a4a
    show screen jobasement_alarmclock
    with dissolve

    $ renpy.pause (4.0, hard=True)

    show jobasement_a4

    $ renpy.pause (1.0, hard=True)

    stop music
    play sound "sounds/se/se_click_2.ogg"
    scene jobasement_a4b
    hide jobasement_a4
    hide screen jobasement_alarmclock

    $ renpy.pause (2.0, hard=True)

    scene blackscreen with dissolve

    $ renpy.pause (0.5, hard=True)

    play music "sounds/me/m_scene_21.ogg"
    scene jobasement_23 with dissolve

    hide screen disable_player_action

    n "I thought I heard something down here! [mc]? What the hell are you doing?!"
    mc "Mmph... What? What's going on?"
    n "You tell me? You're supposed to sleep ON the bed... not UNDER it!"

    scene jobasement_24 with dissolve

    mc "(Oh? What the hell?! I'm back? Already?)"
    n "I know this is a basement, but is it really THAT hot down here that you need to sleep on the cold floor?"
    mc "Y-Yeah, that's the reason why I was there... sure. You know me, I don't like to sweat in my sleep."
    n "Sounds like you need to invest in a fan. It's summertime, you know how humid it can get here."

    scene jobasement_26 with fade

    n "Well, either way... next time, turn off that damn alarm clock... will ya? I won't always be here to do it for you."
    n "It won't be long until science class starts. Ugh... not looking forward to it. Who knows, maybe I'll drop out."
    mc "Natalie, you better not! If I can get through and pass photography, you can get through that."

    scene jobasement_27

    n "Pfft! Science at this level I'm sure is leaps and bounds more difficult than just taking some pretty pictures!"
    n "I just hope my teacher doesn't put me to sleep. The subject is boring enough as it is."

    scene jobasement_28 with dissolve

    n "Oh, and don't forget... Penny was your teacher. We both know how much she loves you. She wouldn't fail you no matter how terrible you did."
    n "Anyways, I have some stuff to do. I'll see you later, [mc]. Oh, and good morning!"
    mc "Heh... Good morning, Natalie. See ya."

    stop music fadeout (2.0)
    scene blackscreen with dissolve

    $ renpy.pause (2.0, hard=True)

    play music "sounds/me/m_scene_17.ogg"
    scene jobasement_29 with dissolve

    mc "(Ugh... Well, thank God I'm back home.)"
    mc "(Otherwise, I'm not so sure what I would have done come morning.)"

    scene jobasement_30 with dissolve

    mc "(Well... whatever is going on, I'm gonna need some more answers.)"
    mc "(This thing has a mind of its own, and I don't want to get caught with my pants down... again!)"

    stop music fadeout (2.0)
    scene blackscreen with dissolve
    show blackscreen

    $ unclickable = True
    $ artifact_ability_questline = 'EXPERIENCE_NEW_TIMELINE'
    $ time_of_day_present = 'AFTERNOON'
    $ gallery_event_jobasement = 1
    $ sketchbook_bttf_active = 1
    $ deny_timepass = False
    call idle_end_post_present from _call_idle_end_post_present_2
    call day_of_week_present_forward from _call_day_of_week_present_forward_8

    $ renpy.pause (2.0, hard=True)

    show screen screen_home_post_pbedroom with dissolve
    $ yadj = ui.adjustment(range=9999999999)
    $ texts_kim_convo.append(1)
    $ phone_text_notif_kim = 1
    $ timer_count = 0
    play sound "sounds/se/se_notif_4.ogg"
    $ unclickable = False
    jump screen_home_post_pbedroom




    screen jobasement_alarmclock:

        if timer_count == 1:
            imagebutton:
                idle "jobasement_a4c"


        if timer_count == 1:
            timer 0.5 action SetVariable ("timer_count", 0) repeat True
        else:
            timer 0.5 action SetVariable ("timer_count", 1) repeat True
