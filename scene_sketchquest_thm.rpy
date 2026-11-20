



label scene_sketchquest_thm:


    $ unclickable = True
    stop music fadeout (2.0)

    show blackscreen
    hide screen screen_sketchbook_thm
    with dissolve

    $ unclickable = False

    image openingdream_a1 = Movie(channel="movies/scene_openingdream/openingdream_a1.webm", play="movies/scene_openingdream/openingdream_a1.webm")
    image openingdream_a2 = Movie(channel="movies/scene_openingdream/openingdream_a2.webm", play="movies/scene_openingdream/openingdream_a2.webm")
    image openingdream_a3 = Movie(channel="movies/scene_openingdream/openingdream_a3.webm", play="movies/scene_openingdream/openingdream_a3.webm")
    image sq_thm_a1a = Movie(channel="movies/sq_thm/sq_thm_a1a.webm", play="movies/sq_thm/sq_thm_a1a.webm")
    image sq_thm_a1b = Movie(channel="movies/sq_thm/sq_thm_a1b.webm", play="movies/sq_thm/sq_thm_a1b.webm")
    image sq_thm_a2a = Movie(channel="movies/sq_thm/sq_thm_a2a.webm", play="movies/sq_thm/sq_thm_a2a.webm")
    image sq_thm_a2b = Movie(channel="movies/sq_thm/sq_thm_a2b.webm", play="movies/sq_thm/sq_thm_a2b.webm")
    image sq_thm_a3 = Movie(channel="movies/sq_thm/sq_thm_a3.webm", play="movies/sq_thm/sq_thm_a3.webm")


    $ renpy.pause(3.0, hard=True)

    play music "sounds/me/m_tense_1.ogg"

    show openingdream_01
    hide blackscreen
    hide screen blackscreen
    with pixellate

    mc "Commander, do you read me?"
    mc "I've reached the inner sanctum of our enemy's lair."
    mc "The path so far has been clear, but I'll report back once I've found the vile beast!"

    show blackscreen with dissolve

    show openingdream_02 with dissolve
    hide openingdream_01
    hide blackscreen

    mc "(Where... are you?)"
    mc "(I've had just about enough of this little game of hide and seek.)"
    mc "(Ugh... more empty hallways? Maybe, this isn't the right place, after all.)"

    show openingdream_03
    hide openingdream_02

    mc "Commander, I believe I've reached the cave's apex."
    mc "Still no enemies to be found. Perhaps our intel was incorrect."
    mc "I'll proceed to exit shortly. Rendezvous at the drop point in a half..."

    stop music fadeout (2.0)
    play sound "sounds/se/se_alien_1.ogg"
    show openingdream_04 with Dissolve (2.0, hard=True)
    hide openingdream_03

    $ renpy.pause (1.0, hard=True)
    mc "(Wait... What was that?)"
    play music "sounds/me/m_fight_1.ogg"

    play sound "sounds/se/se_alien_2.ogg"
    show openingdream_05 with dissolve
    hide openingdream_04

    mc "Cancel that, Commander. There's been a change of plans!"
    mc "Looks like I've become an unwanted guest. It's time to crash this party!"
    mc "Come on you sons' of bitches... GIVE ME ALL YOU GOT!"

    show openingdream_06b with Dissolve (0.2)
    hide openingdream_05

    play sound "sounds/se/se_rifle_2.ogg"
    show openingdream_06a:
        xpos -100
    with Dissolve (0.3)

    show openingdream_06a:
        xpos -100
        linear 8.0 xpos 450

    $ renpy.pause(2.0, hard=True)


    show openingdream_07b with Dissolve (0.2)
    hide openingdream_06a
    hide openingdream_06b

    show openingdream_07a:
        xpos 100
    with Dissolve (0.3)

    play sound "sounds/se/se_knife_1.ogg"

    show openingdream_07a:
        xpos 100
        linear 8.0 xpos -450

    $ renpy.pause (2.0, hard=True)

    show openingdream_08b with Dissolve (0.2)
    hide openingdream_07a
    hide openingdream_07b

    show openingdream_08a:
        xpos 0
    with Dissolve (0.3)

    play sound "sounds/se/se_punch_1.ogg"

    show openingdream_08a:
        xpos 0
        linear 8.0 xpos 450

    $ renpy.pause(2.0, hard=True)

    show openingdream_09b
    hide openingdream_08a
    hide openingdream_08b

    show openingdream_09a:
        xpos 50
    with Dissolve (0.3)
    play sound "sounds/se/se_rifle_1.ogg"

    show openingdream_09a:
        xpos 50
        linear 8.0 xpos -450

    $ renpy.pause(2.0, hard=True)

    stop music fadeout (2.0)
    show blackscreen with dissolve
    hide openingdream_09a
    hide openingdream_09b

    pause(3.0)

    play music "sounds/me/m_tense_1.ogg"
    show screen openingdream_10a
    show openingdream_10b
    with dissolve
    hide blackscreen
    pause (0.5)

    mc "(Well, that was quite the battle...)"
    mc "(Can't let my guard down, though. These monstrosities pack quite the punch.)"

    play sound "sounds/se/se_fade_1.ogg"
    show openingdream_10c
    hide openingdream_10b
    with Dissolve (3.0)
    pause (1.0)

    mc "(And since they regenerate, we won't get anywhere by fighting her children.)"
    mc "(Each day our numbers dwindle, while theirs only grow...)"
    mc "(If we want to end this war, we have to terminate the source, the hive mother!)"

    show blackscreen
    hide screen openingdream_10a
    with dissolve
    hide openingdream_10b
    hide openingdream_10c

    pause (1.0)

    show openingdream_11 with dissolve
    hide blackscreen

    mc "(Now that I know I'm on the right track, I gotta keep going.)"
    mc "(But I don't have much time. They'll soon be back, and in greater numbers.)"

    scene openingdream_a1a

    mc "Yes, Commander. I'm still here. No, Sir. Only more of those wretched beasts..."
    mc "Afraid I can't do that, Sir. I'm not leaving this place until the job is done."
    mc "I'll massacre every last one of them if I have to. It's bound to draw her out!"

    stop music fadeout (4.0)
    show screen disable_player_action
    play sound "sounds/se/se_jump_1.ogg"
    show openingdream_a1anim
    $ renpy.pause(5.0, hard=True)

    play music "sounds/me/m_tense_2.ogg"

    hide screen disable_player_action
    thm "Then look no further, boy. Because here I am..."

    scene openingdream_13 with dissolve


    if renpy.exists("sounds/voice/scene_openingdream/mc/mc_openingdream_25.ogg") and voice_mc == 1:
        voice "sounds/voice/scene_openingdream/mc/mc_openingdream_25.ogg"
    mc "Speak of the devil! You're a hard one to find, but at last, we meet."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_02.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_02.mp3"
    thm "I'm not usually one to make appearances, but you've been quite the nuisance."

    if renpy.exists("sounds/voice/scene_openingdream/mc/mc_openingdream_26.ogg") and voice_mc == 1:
        voice "sounds/voice/scene_openingdream/mc/mc_openingdream_26.ogg"
    mc "Me? You're the one wreaking all the havoc. I'm just here to end it."

    show openingdream_a2a:
        xpos 952
    with dissolve

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_03.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_03.mp3"
    thm "Oh, but you have my intentions all wrong."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_04.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_04.mp3"
    thm "I'm merely purifying the earth of it's filth. Your deaths are just a byproduct of the process."

    show openingdream_a3a:
        xpos 0
    with dissolve

    if renpy.exists("sounds/voice/scene_openingdream/mc/mc_openingdream_27.ogg") and voice_mc == 1:
        voice "sounds/voice/scene_openingdream/mc/mc_openingdream_27.ogg"
    mc "I don't know what sort of sick, twisted planet you came from, but here on earth, nothing good has come from mass genocide."

    if renpy.exists("sounds/voice/scene_openingdream/mc/mc_openingdream_28.ogg") and voice_mc == 1:
        voice "sounds/voice/scene_openingdream/mc/mc_openingdream_28.ogg"
    mc "You're sorely mistaken if you think we'll just lay down without putting up one hell of a fight."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_05.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_05.mp3"
    thm "Foolish child..."

    show screen disable_player_action
    show openingdream_a2anim:
        xpos 952

    $ renpy.pause (1.25, hard=True)
    play sound "sounds/se/se_claw_1.ogg"
    $ renpy.pause (1.5, hard=True)

    hide screen disable_player_action
    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_06.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_06.mp3"
    thm "It doesn't matter how hard you push back. Your loss is inevitable!"

    if renpy.exists("sounds/voice/scene_openingdream/mc/mc_openingdream_29.ogg") and voice_mc == 1:
        voice "sounds/voice/scene_openingdream/mc/mc_openingdream_29.ogg"
    mc "We'll see about that, you vile beast!"

    show openingdream_16c with Dissolve (0.5)
    hide openingdream_15


    play sound "sounds/se/se_rifle_2.ogg"
    show openingdream_16b:
        xpos 200
        linear 12.0 xpos -180
    show openingdream_16a:
        xpos -100
        linear 12.0 xpos 180
    with Dissolve (1.0)

    $ renpy.pause(1.0, hard=True)


    show openingdream_06b with Dissolve (0.2)
    hide openingdream_16a
    hide openingdream_16b
    hide openingdream_16c

    play sound "sounds/se/se_dodge_1.ogg"
    show sq_thm_fight_01:
        xpos -100
    with Dissolve (0.3)

    show sq_thm_fight_01:
        xpos -100
        linear 8.0 xpos -450

    $ renpy.pause(2.0, hard=True)


    show openingdream_07b with Dissolve (0.2)
    hide sq_thm_fight_01
    hide openingdream_06b

    play sound "sounds/se/se_claw_1.ogg"
    show sq_thm_fight_02:
        xpos 100
    with Dissolve (0.3)

    show sq_thm_fight_02:
        xpos 100
        linear 8.0 xpos 450

    $ renpy.pause(2.0, hard=True)

    show openingdream_08b with Dissolve (0.2)
    hide sq_thm_fight_02
    hide openingdream_07b

    play sound "sounds/se/se_knife_1.ogg"
    show sq_thm_fight_03:
        xpos -100
    with Dissolve (0.3)

    show sq_thm_fight_03:
        xpos -100
        linear 8.0 xpos -450

    $ renpy.pause (2.0, hard=True)

    show openingdream_09b with Dissolve (0.2)
    hide sq_thm_fight_03
    hide openingdream_08b

    play sound "sounds/se/se_swoosh_1.ogg"

    show sq_thm_fight_04:
        xpos -600 ypos -380
        linear 4.0 xpos 600 rotate 20
    with Dissolve (0.3)

    $ renpy.pause (2.0, hard=True)

    show openingdream_06b with Dissolve (0.2)
    hide sq_thm_fight_04
    hide openingdream_09b

    play sound "sounds/se/se_footsteps_1.ogg"
    show sq_thm_fight_05
    with Dissolve (0.3)

    show sq_thm_fight_05:
        ypos 0
        linear 8.0 ypos 100

    $ renpy.pause (2.0, hard=True)

    show openingdream_07b with Dissolve (0.2)
    hide sq_thm_fight_05
    hide openingdream_06b

    play sound "sounds/se/se_swoosh_2.ogg"

    show sq_thm_fight_06:
        xpos -400
        ypos -500
        linear 8.0 xpos 450 rotate 30
    with Dissolve (0.3)

    stop music fadeout (3.0)
    $ renpy.pause (3.0, hard=True)

    show blackscreen with dissolve
    play sound "sounds/se/se_bodyfall_1.ogg"
    hide openingdream_07b
    hide sq_thm_fight_06

    $ renpy.pause (2.0, hard=True)

    play sound "sounds/se/se_equipgun_1.ogg"
    $ renpy.pause (1.0)
    play sound "sounds/se/se_nightvision_1.ogg"

    $ renpy.pause (1.0, hard=True)

    play music "sounds/me/m_tense_2.ogg"
    show sq_thm_01 with dissolve
    hide blackscreen

    mc "It's over, bitch! You've preyed upon the weak and helpless, but now you've finally met your match."
    mc "Make any sudden moves and I won't hesitate to put a bullet in your brain!"

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_11.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_11.mp3"
    thm "Urgh! Bested by a pathetic little human. How is this possible?!"

    mc "Clearly, you've underestimated my will to survive. You're mine now..."

    show sq_thm_02a with dissolve

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_12.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_12.mp3"
    thm "You're all the same! Blindly following orders... Depleting our resources for your people's own selfish gain."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_13.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_13.mp3"
    thm "Eradicating anything that stands in your way. We are merely doing what we must to exist."

    show sq_thm_02b with dissolve

    mc "Lies... you attacked us first. We are merely defending ourselves."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_14.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_14.mp3"
    thm "That is your twisted tale. The victor is the one that tells the story. Whether or not it is accurate."

    mc "You're still trying to manipulate and decieve up until the bitter end? I should kill you where you stand."

    show sq_thm_03 with hpunch
    hide sq_thm_01
    hide sq_thm_02a
    hide sq_thm_02b

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_15.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_15.mp3"
    thm "I'VE HAD ENOUGH OF THIS CAT AND MOUSE. THAT IS WHAT YOU'RE HERE FOR, ISN'T IT?"

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_16.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_16.mp3"
    thm "STOP TOYING WITH ME AND JUST DO IT, ALREADY!"

    stop music fadeout (3.0)
    $ renpy.pause (2.0, hard=True)

    mc "No..."

    $ renpy.pause (1.0, hard=True)

    play music "sounds/me/m_scene_18.ogg"
    show sq_thm_04 with fade
    hide sq_thm_03

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_17.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_17.mp3"
    thm "What... what are you doing?"

    mc "Making my own decisions for once. I've seen enough senseless killing."
    mc "I don't want the extinction of an entire species to be on my hands."

    show sq_thm_05
    hide sq_thm_04

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_18.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_18.mp3"
    thm "I don't understand. You had the opportunity to end this violence, and you choose not to. Why?"

    mc "Because you don't end violence... with violence. You've shown no mercy, but maybe you just don't understand it, because you've never known it."

    show sq_thm_06
    hide sq_thm_05

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_19.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_19.mp3"
    thm "I haven't seen such compassion. Maybe... I was wrong about your kind."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_20.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_20.mp3"
    thm "Perhaps you're right. Maybe, there is a future that doesn't end in bloodshed."

    mc "That is all I can ever hope for. We aren't just killing machines. Perhaps, this can be the start of a peaceful coexistence."

    show sq_thm_a3a with dissolve
    hide sq_thm_06

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_21.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_21.mp3"
    thm "I understand now..."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_22.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_22.mp3"
    thm "I always believed that the only way to win this war, was to wipe your kind from complete existence."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_23.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_23.mp3"
    thm "But I was wrong. There IS another way... after all."

    mc "Hmm... and what might that be?"

    stop music fadeout (3.0)
    show sq_thm_a3 with Dissolve (0.00001)

    $ renpy.pause (1.0, hard=True)
    play sound "sounds/se/se_jump_1.ogg"
    $ renpy.pause (1.05, hard=True)

    show sq_thm_a3b
    $ renpy.pause (0.2, hard=True)
    hide sq_thm_a3
    hide sq_thm_a3a

    play sound "sounds/se/se_fade_2.ogg"
    show sq_thm_a3c with Dissolve (1.0)

    $ renpy.pause (1.0, hard=True)

    play music "sounds/me/m_tense_2.ogg"

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_24.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_24.mp3"
    thm "Assimilation..."

    show sq_thm_07 with dissolve
    hide sq_thm_a3b
    hide sq_thm_a3c

    mc "Urgh! What... what are you doing?!"

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_25.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_25.mp3"
    thm "I've always dispised your kind. Believing you to only be spineless and weak. Completely inferior in every way. That is... until I met you."

    play sound "sounds/se/se_rip_1.ogg"
    show sq_thm_08
    hide sq_thm_07

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_26.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_26.mp3"
    thm "Maybe, the key to conquering is not by ridding the world of it's filth, but by adapting it. With others like you by my side... I can't lose."

    mc "None of that makes any sense! What the hell are you talking about?! What are you planning?!"

    play sound "sounds/se/se_bodyfall_1.ogg"
    show sq_thm_09 with hpunch
    hide sq_thm_08

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_27.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_27.mp3"
    thm "Doing what is needed to coexist. By passing along our unique bounties to one another."

    mc "What could I possibly have that you would want, or I, you?!"

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_28.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_28.mp3"
    thm "The gift of creation, of course. You will sow the seeds of life within me, and I in return, will bestow the gift of darkness upon you."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_29.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_29.mp3"
    thm "Both of which must be given... willingly."

    mc "Willingly?! In what form is this given voluntarily?! This is something I will not agree to!"

    show sq_thm_10a with dissolve

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_30.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_30.mp3"
    thm "Foolish boy... it is not the mind that must be willing, but the body, itself."

    show sq_thm_10b with dissolve

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_31.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_31.mp3"
    thm "From what I can see... yours is more than eager to partake in this ritual."

    play sound "sounds/se/se_fade_2.ogg"
    show sq_thm_10c with Dissolve (2.0)

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_32.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_32.mp3"
    thm "And that's all the permission I need. So let us begin..."

    show sq_thm_10d with dissolve

    mc "You won't get away with this! My death won't solve anything. It'll only motivate my kind to push further."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_33.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_33.mp3"
    thm "Oh, I never intend to kill you. Your body will still be in perfect health, but your mind... will belong to me."

    show sq_thm_11 with fade
    hide sq_thm_09
    hide sq_thm_10a
    hide sq_thm_10b
    hide sq_thm_10c
    hide sq_thm_10d

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_34.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_34.mp3"
    thm "I plan to have you as my prime consort. With such a strong-willed being as my mate, my future children will be more powerful than ever!"

    mc "I, I can not... I, I will not... let you use me to further your own cause."

    show sq_thm_a1a with dissolve
    hide sq_thm_11

    $ renpy.pause()

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_35.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_35.mp3"
    thm "Shh... resistance is futile. Relax and let the ritual commence without defiance."

    mc "Please... stop this..."

    show sq_thm_a1b with dissolve
    hide sq_thm_a1a

    $ renpy.pause()

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_36.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_36.mp3"
    thm "Why are you fighting this? In my experience with my past mates, your kind take great pleasure in procreation."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_37.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_37.mp3"
    thm "I'm sure this is quite enjoyable. Luckily for you, you'll be the first to not just be disposed of, afterward."

    show sq_thm_12a with fade
    hide sq_thm_a1b

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_38.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_38.mp3"
    thm "Mhmm... I feel it, can you? You're body is giving in. Lowering its defenses... slowly preparing itself for the exchange."

    show screen disable_player_action

    play sound "sounds/se/se_whoosh_1.ogg"
    show sq_thm_12b with Dissolve (2.0)

    $ renpy.pause (1.0, hard=True)

    hide screen disable_player_action
    mc "What are you doing? What... what is that I'm feeling?!"
    show screen disable_player_action

    play sound "sounds/se/se_whoosh_2.ogg"
    show sq_thm_12c with Dissolve (2.0)

    $ renpy.pause (1.0, hard=True)

    hide screen disable_player_action

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_39.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_39.mp3"
    thm "The darkness... It is spreading."

    show sq_thm_a2c with dissolve
    $ renpy.pause (1.0, hard=True)
    play sound "sounds/se/se_whoosh_2.ogg"
    show sq_thm_a2d with Dissolve (2.0)
    $ renpy.pause (1.0, hard=True)

    show sq_thm_a2a with dissolve
    hide sq_thm_12a
    hide sq_thm_12b
    hide sq_thm_12c
    hide sq_thm_a2c
    hide sq_thm_a2d

    $ renpy.pause()

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_40.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_40.mp3"
    thm "I feel your climax building as I speak. By the time it is complete, we will both be infected with each other's seed."

    mc "Yes... I... I can feel it coarsing through my veins."

    show sq_thm_a2b with dissolve
    hide sq_thm_a2a

    $ renpy.pause()

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_41.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_41.mp3"
    thm "The power is intoxicating, isn't it? Give in... give in to your desires and let them flow into me."

    mc "I can... I will... I must... pass my gift... into you."

    show sq_thm_13 with fade
    hide sq_thm_a2b

    mc "Uhhhh! I'm... I'm gonna cum."

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_42.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_42.mp3"
    thm "Yes! Do not fight it. Give in... Fill me with your seed..."

    show sq_thm_14a with dissolve
    hide sq_thm_13

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_43.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_43.mp3"
    thm "Let our union result in the fertilization of my womb..."

    $ renpy.pause (1.0, hard=True)

    show sq_thm_14b with Dissolve (2.0)

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_44.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_44.mp3"
    thm "So that I may breed the greatest force this world has ever seen."

    $ renpy.pause (1.0, hard=True)

    show sq_thm_15a with fade
    hide sq_thm_14a
    hide sq_thm_14b

    $ renpy.pause (0.5, hard=True)

    hide screen disable_player_action

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_45.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_45.mp3"
    thm "You've done well, young one. You are most deserving of the gift I am willing to bestow upon you."

    show screen disable_player_action

    play sound "sounds/se/se_whoosh_1.ogg"
    show sq_thm_15b with Dissolve (2.0)

    $ renpy.pause (3.0, hard=True)

    hide sq_thm_15b with Dissolve (2.0)

    $ renpy.pause (1.0, hard=True)

    play sound "sounds/se/se_whoosh_2.ogg"
    show sq_thm_15c with Dissolve (2.0)

    hide screen disable_player_action

    if renpy.exists("sounds/voice/scene_openingdream/penny/penny_openingdream_46.mp3") and voice_penny == 1:
        voice "sounds/voice/scene_openingdream/penny/penny_openingdream_46.mp3"
    thm "Once my sworn enemy, now my primary consort... Wake... and we will rise and conquer all."

    show screen disable_player_action

    $ renpy.pause (2.0, hard=True)

    show sq_thm_15_anim_01:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_02:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_03:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_04:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_05:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_06:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_07:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_08:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_09:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_10:
        xpos 735 ypos 232
    $ renpy.pause (0.05, hard=True)
    show sq_thm_15_anim_11:
        xpos 735 ypos 232
    $ renpy.pause (1.0, hard=True)
    play sound "sounds/se/se_whoosh_2.ogg"
    show sq_thm_15_anim_12:
        xpos 735 ypos 232
    with Dissolve (2.0)

    $ renpy.pause (0.5, hard=True)

    hide screen disable_player_action

    mc "Yes... my queen. I am here to serve..."

    stop music fadeout (2.0)

    show blackscreen with dissolve

    hide sq_thm_15a
    hide sq_thm_15b
    hide sq_thm_15c
    hide sq_thm_15_anim_01
    hide sq_thm_15_anim_02
    hide sq_thm_15_anim_03
    hide sq_thm_15_anim_04
    hide sq_thm_15_anim_05
    hide sq_thm_15_anim_06
    hide sq_thm_15_anim_07
    hide sq_thm_15_anim_08
    hide sq_thm_15_anim_09
    hide sq_thm_15_anim_10
    hide sq_thm_15_anim_11
    hide sq_thm_15_anim_12

    $ renpy.pause (2.0, hard=True)

    mc "(And that's why you never let your guard down.)"
    mc "(But like they say... 'Doesn't matter, had sex.' Heh...)"

    $ renpy.pause (1.0, hard=True)

    $ unclickable = True

    show screen screen_sketchbook_thm with pixellate
    hide blackscreen

    $ unclickable = False

    jump screen_sketchbook_thm
