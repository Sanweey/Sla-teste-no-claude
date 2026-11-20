


###--- Globe Main Menu

screen globe_main_menu:
    on "show" action Play('music', "sounds/me/m_game_1.ogg", if_changed=True)
    imagemap:
        ground "globe_cover"

    if unclickable == False:
        imagebutton:
            idle "globe_startgame_g"
            hover "globe_startgame_h"
            focus_mask True
            if unclickable == False:
                action Jump("boxing_sam_riley_prepare") activate_sound "sounds/se/se_click_1.ogg"

    if unclickable == False:
        imagebutton:
            idle "globe_tutorial_g"
            hover "globe_tutorial_h"
            focus_mask True
            if unclickable == False:
                action Call("boxing_sam_riley_tutorial") activate_sound "sounds/se/se_click_1.ogg"

    if meetkim_globe_done == 1:
        if unclickable == False:
            imagebutton:
                idle "globe_exit_g"
                hover "globe_exit_h"
                focus_mask True
                if unclickable == False:
                    if ptt_time == False:
                        action SetVariable ("pix_transition", 1), Jump("comp_post_desktop") activate_sound "sounds/se/se_click_1.ogg"
                    else:
                        action SetVariable ("pix_transition", 1), Jump("comp_ptt_desktop") activate_sound "sounds/se/se_click_1.ogg"

label boxing_sam_riley_mainmenu:
    if meetkim_globe_done == 1 and map_transition == 1:
        $ unclickable = True
        show screen globe_main_menu
        with pixellate
        hide screen comp_ptt_desktop
        hide screen comp_post_desktop
        hide screen comp_desktop
        $ map_transition = 0
        $ unclickable = False
        pause
        jump boxing_sam_riley_mainmenu
    elif meetkim_globe_done == 1:
        show screen globe_main_menu
        hide screen comp_ptt_desktop
        hide screen comp_post_desktop
        pause
        jump boxing_sam_riley_mainmenu
    else:
        show screen globe_main_menu
        hide screen comp_ptt_desktop
        hide screen comp_post_desktop
        pause
        jump boxing_sam_riley_mainmenu


###--- Tutorial Screen
screen globe_tutorial:
    imagemap:
        ground "globe_tutorial"




label boxing_sam_riley_tutorial:
    $ unclickable = True
    show screen globe_main_menu
    $ renpy.pause (0.0001)
    show screen globe_tutorial
    with dissolve
    $ renpy.pause()
    hide screen globe_tutorial
    with dissolve
    $ unclickable = False
    hide screen globe_main_menu
    jump boxing_sam_riley_mainmenu




label boxing_sam_riley_prepare:

    image boxing_sari_special_1 = Movie(channel="movies/boxing/boxing_sari_special_1.webm", play="movies/boxing/boxing_sari_special_1.webm", size=(1920,1080))
    image boxing_sari_special_2 = Movie(channel="movies/boxing/boxing_sari_special_2.webm", play="movies/boxing/boxing_sari_special_2.webm", size=(1920,1080))
    image boxing_sari_windup = Movie(channel="movies/boxing/boxing_sari_windup.webm", play="movies/boxing/boxing_sari_windup.webm", size=(1920,1080))
    image boxing_a1 = Movie(channel="movies/boxing/boxing_a1.webm", play="movies/boxing/boxing_a1.webm", size=(1920,1080))
    image boxing_sari_idle = Movie(channel="movies/boxing/boxing_sari_idle.webm", play="movies/boxing/boxing_sari_idle.webm", size=(1920,1080))
    image boxing_sari_dr = Movie(channel="movies/boxing/boxing_sari_dr.webm", play="movies/boxing/boxing_sari_dr.webm", size=(1920,1080))
    image boxing_sari_dl = Movie(channel="movies/boxing/boxing_sari_dl.webm", play="movies/boxing/boxing_sari_dl.webm", size=(1920,1080))
    image boxing_sari_hr = Movie(channel="movies/boxing/boxing_sari_hr.webm", play="movies/boxing/boxing_sari_hr.webm", size=(1920,1080))
    image boxing_sari_hl = Movie(channel="movies/boxing/boxing_sari_hl.webm", play="movies/boxing/boxing_sari_hl.webm", size=(1920,1080))
    image boxing_sari_pl = Movie(channel="movies/boxing/boxing_sari_pl.webm", play="movies/boxing/boxing_sari_pl.webm", size=(1920,1080))
    image boxing_sari_pr = Movie(channel="movies/boxing/boxing_sari_pr.webm", play="movies/boxing/boxing_sari_pr.webm", size=(1920,1080))
    image boxing_sari_rcheer_1 = Movie(channel="movies/boxing/boxing_sari_rcheer_1.webm", play="movies/boxing/boxing_sari_rcheer_1.webm", size=(1920,1080))
    image boxing_sari_rcheer_2 = Movie(channel="movies/boxing/boxing_sari_rcheer_2.webm", play="movies/boxing/boxing_sari_rcheer_2.webm", size=(1920,1080))
    image boxing_sari_scheer_1 = Movie(channel="movies/boxing/boxing_sari_scheer_1.webm", play="movies/boxing/boxing_sari_scheer_1.webm", size=(1920,1080))
    image boxing_sari_scheer_2 = Movie(channel="movies/boxing/boxing_sari_scheer_2.webm", play="movies/boxing/boxing_sari_scheer_2.webm", size=(1920,1080))
    image boxing_sari_rwin = Movie(channel="movies/boxing/boxing_sari_rwin.webm", play="movies/boxing/boxing_sari_rwin.webm", size=(1920,1080))
    image boxing_sari_swin = Movie(channel="movies/boxing/boxing_sari_swin.webm", play="movies/boxing/boxing_sari_swin.webm", size=(1920,1080))
    $ boxing_riley_special_counter = 0

    hide screen globe_main_menu
    show blackscreen
    $ renpy.pause (0.1)
    show boxing_a1
    with dissolve
    hide blackscreen

    $ renpy.pause (0.5, hard=True)

    show char_samvicious:
        xpos -800
        linear 0.5 xpos 0

    $ renpy.pause (1.0, hard=True)

    show samvicious with dissolve

    $ renpy.pause (1.0, hard=True)

    show vs with dissolve

    $ renpy.pause (1.0, hard=True)

    show char_rileypiper:
        xpos 800
        linear 0.5 xpos 0

    $ renpy.pause (1.0, hard=True)

    show rileypiper with dissolve

    $ renpy.pause (1.5, hard=True)

    #- Disable Rollback
    $ config.rollback_enabled = False
    #- Disable Menu
    $ _game_menu_screen = None

    $ renpy.pause (1.5, hard=True)

    show blackscreen
    hide boxing_a1
    hide char_samvicious
    hide samvicious
    hide vs
    hide char_rileypiper
    hide rileypiper
    with pixellate

    $ renpy.pause (1.0, hard=True)

    stop music fadeout (2.0)

    $ boxing_health_player = 8
    $ boxing_health_enemy = 8
    $ rng_boxing = 1
    $ rng_boxing_punched = 1

    $ renpy.pause (1.0, hard=True)
    play music "sounds/me/m_game_2.ogg"
    show boxing_kr_idle
    show boxing_sari_idle
    with pixellate
    $ renpy.pause (1.0, hard=True)
    show screen sari_boxing_health
    with dissolve
    hide boxing_background
    $ renpy.pause (1.0, hard=True)
    if minigame_mode == 2:
        jump sam_riley_win

label boxing_sam_riley_repeat:
    $ qte_boxing_sari_special_timer = 0
    $ boxing_dodged_special_1 = 0
    $ boxing_dodged_special_2 = 0
    $ boxing_dodged_special_3 = 0
    $ boxing_dodged_special_4 = 0
    $ boxing_dodged = 0
    $ boxing_punched = 0
    $ renpy.pause (2.0, hard=True)
    if boxing_health_player <= 0:
        jump sam_riley_win
    elif boxing_health_enemy <= 0:
        jump sam_riley_lose
    elif boxing_riley_special_counter >= 5:
        jump sam_riley_special
    else:
        $ boxing_riley_special_counter += 1

label boxing_sam_riley_idle:

    if rng_boxing == 1:
        $ rng_boxing = 2
        show screen qte_boxing_sari_1
        with Dissolve (0.7)
        call screen boxing_sr_right
    elif rng_boxing == 2:
        $ rng_boxing = 3
        show screen qte_boxing_sari_1
        with Dissolve (0.7)
        call screen boxing_sr_left
    elif rng_boxing == 3:
        $ rng_boxing = 4
        show screen qte_boxing_sari_1
        with Dissolve (0.7)
        call screen boxing_sr_right
    elif rng_boxing == 4:
        $ rng_boxing = 1
        show screen qte_boxing_sari_1
        with Dissolve (0.7)
        call screen boxing_sr_left

label boxing_sam_riley_right_outcome:

    if boxing_dodged == 0:
        show boxing_sari_hr with Dissolve (0.0001)
        hide boxing_sari_idle
        $ renpy.pause (0.3, hard=True)
        play sound "sounds/se/se_punch_1.ogg"
        $ boxing_health_player -= 1
        show transparent with hpunch
        $ renpy.pause (0.80, hard=True)
        show boxing_sari_idle with Dissolve (0.0001)
        hide boxing_sari_hr
        hide transparent
        $ boxing_dodged = 0
        jump boxing_sam_riley_repeat
    else:
        show boxing_sari_dr with Dissolve (0.0001)
        hide boxing_sari_idle
        show screen boxing_sr_sampunch_left
        show screen qte_boxing_sari_punch_1
        with Dissolve (0.5, hard=True)
        play sound "sounds/se/se_dodge_1.ogg"
        $ renpy.pause (0.55, hard=True)
        show boxing_sari_idle with Dissolve (0.000001)
        hide boxing_sari_dr
        hide transparent
        $ boxing_dodged = 0
        if minigame_mode == 1:
            $ renpy.pause (2000, hard=True)
        else:
            $ renpy.pause (3.0, hard=True)
        jump boxing_sam_riley_repeat


label boxing_sam_riley_left_outcome:

    if boxing_dodged == 0:
        show boxing_sari_hl with Dissolve (0.0001)
        hide boxing_sari_idle
        $ renpy.pause (0.3, hard=True)
        play sound "sounds/se/se_punch_2.ogg"
        $ boxing_health_player -= 1
        show transparent with hpunch
        $ renpy.pause (0.80, hard=True)
        show boxing_sari_idle with Dissolve (0.0001)
        hide boxing_sari_hl
        hide transparent
        $ boxing_dodged = 0
        jump boxing_sam_riley_repeat
    else:
        show boxing_sari_dl with Dissolve (0.0001)
        hide boxing_sari_idle
        show screen boxing_sr_sampunch_right
        show screen qte_boxing_sari_punch_1
        with Dissolve (0.5, hard=True)
        play sound "sounds/se/se_dodge_2.ogg"
        $ renpy.pause (0.55, hard=True)
        show boxing_sari_idle with Dissolve (0.000001)
        hide boxing_sari_dl
        hide transparent
        $ boxing_dodged = 0
        if minigame_mode == 1:
            $ renpy.pause (2000, hard=True)
        else:
            $ renpy.pause (3.0, hard=True)
        jump boxing_sam_riley_repeat

####################################

###--- Transforms

###--- Riley's Punches
###--- Top Left
transform boxing_dodge_riley_tl:
    linear 0.5 xpos -100 ypos -300

###--- Bottom Right
transform boxing_dodge_riley_tr:
    linear 0.5 xpos 300 ypos 400

###--- Bottom Left
transform boxing_dodge_riley_bl:
    linear 0.5 xpos -150 ypos 400

###--- Top Right
transform boxing_dodge_riley_br:
    linear 0.5 xpos 240 ypos -210


###--- Sam's Punches
###--- Right
transform boxing_dodge_sam_r:
    linear 0.5 xpos 300

###--- Left
transform boxing_dodge_sam_l:
    linear 0.5 xpos -300

###--- Down
transform boxing_dodge_sam_d:
    linear 0.5 ypos 300

###--- Up
transform boxing_dodge_sam_u:
    linear 0.5 ypos -300

####################################

###--- Screens

###--- Riley Punches
screen boxing_sr_left:

    if minigame_mode == 0:
        timer 3.0 action Hide('boxing_sr_left'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump("boxing_sam_riley_left_outcome")

screen boxing_sr_right:

    if minigame_mode == 0:
        timer 3.0 action Hide('boxing_sr_right'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump("boxing_sam_riley_right_outcome")

###--- Sam Punches
screen boxing_sr_sampunch_left:

    if minigame_mode == 0:
        timer 3.0 action Hide('boxing_sr_sampunch_left'), Hide ('qte_boxing_sari_punch_1'), Hide ('qte_boxing_sari_punch_2', transition=dissolve), Jump("boxing_sam_riley_punch_outcome")

screen boxing_sr_sampunch_right:

    if minigame_mode == 0:
        timer 3.0 action Hide('boxing_sr_sampunch_right'), Hide ('qte_boxing_sari_punch_1'), Hide ('qte_boxing_sari_punch_2', transition=dissolve), Jump("boxing_sam_riley_punch_outcome")



###--- Riley Punches
screen qte_boxing_sari_1:

    if boxing_dodged == 0:
        imagebutton:
            if rng_boxing == 1:
                idle "boxing_riley_dodge_right_g"
                at boxing_dodge_riley_tl
            elif rng_boxing == 2:
                idle "boxing_riley_dodge_left_g"
                at boxing_dodge_riley_tr
            elif rng_boxing == 3:
                idle "boxing_riley_dodge_right_g"
                at boxing_dodge_riley_bl
            elif rng_boxing == 4:
                idle "boxing_riley_dodge_left_g"
                at boxing_dodge_riley_br
            focus_mask True

    timer 0.5 action Hide('qte_boxing_sari_1'), Show ('qte_boxing_sari_2')


screen qte_boxing_sari_2:

    if boxing_dodged == 0:
        imagebutton:
            if rng_boxing == 1:
                idle "boxing_riley_dodge_right_g"
                hover "boxing_riley_dodge_right_h"
                xpos -100 ypos -300
                action SetVariable ("boxing_dodged", 1), Hide('boxing_sr_sampunch_right'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump ("boxing_sam_riley_right_outcome") activate_sound "sounds/se/se_ding_1.ogg"
            elif rng_boxing == 2:
                idle "boxing_riley_dodge_left_g"
                hover "boxing_riley_dodge_left_h"
                xpos 300 ypos 400
                action SetVariable ("boxing_dodged", 1), Hide('boxing_sr_sampunch_right'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump ("boxing_sam_riley_left_outcome") activate_sound "sounds/se/se_ding_1.ogg"
            elif rng_boxing == 3:
                idle "boxing_riley_dodge_right_g"
                hover "boxing_riley_dodge_right_h"
                xpos -150 ypos 400
                action SetVariable ("boxing_dodged", 1), Hide('boxing_sr_sampunch_right'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump ("boxing_sam_riley_right_outcome") activate_sound "sounds/se/se_ding_1.ogg"
            elif rng_boxing == 4:
                idle "boxing_riley_dodge_left_g"
                hover "boxing_riley_dodge_left_h"
                xpos 240 ypos -210
                action SetVariable ("boxing_dodged", 1), Hide('boxing_sr_sampunch_right'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump ("boxing_sam_riley_left_outcome") activate_sound "sounds/se/se_ding_1.ogg"
            focus_mask True


###--- Sam Punches

screen qte_boxing_sari_punch_1:

    if boxing_punched == 0:
        imagebutton:
            if rng_boxing == 1:
                idle "boxing_sam_punch_right_g"
                at boxing_dodge_sam_r
            elif rng_boxing == 2:
                idle "boxing_sam_punch_left_g"
                at boxing_dodge_sam_l
            elif rng_boxing == 3:
                idle "boxing_sam_punch_right_g"
                at boxing_dodge_sam_u
            elif rng_boxing == 4:
                idle "boxing_sam_punch_left_g"
                at boxing_dodge_sam_d
            focus_mask True

    timer 0.5 action Hide('qte_boxing_sari_punch_1'), Show ('qte_boxing_sari_punch_2')


screen qte_boxing_sari_punch_2:

    if boxing_punched == 0:
        imagebutton:
            if rng_boxing == 1:
                idle "boxing_sam_punch_right_g"
                hover "boxing_sam_punch_right_h"
                xpos 300
            elif rng_boxing == 2:
                idle "boxing_sam_punch_left_g"
                hover "boxing_sam_punch_left_h"
                xpos -300
            elif rng_boxing == 3:
                idle "boxing_sam_punch_right_g"
                hover "boxing_sam_punch_right_h"
                ypos -300
            elif rng_boxing == 4:
                idle "boxing_sam_punch_left_g"
                hover "boxing_sam_punch_left_h"
                ypos 300
            focus_mask True
            action SetVariable ("boxing_punched", 1), Hide('boxing_sr_sampunch_right'), Hide ('qte_boxing_sari_1'), Hide ('qte_boxing_sari_2', transition=dissolve), Jump ("boxing_sam_riley_punch_outcome") activate_sound "sounds/se/se_ding_1.ogg"


###--- Boxing Health Bars
screen sari_boxing_health:

    if minigame_mode == 1:
        imagebutton:
            xpos 875 ypos 5
            focus_mask True
            if ptt_time == True:
                idle "ezmode_blink_ptt"
            else:
                idle "ezmode_blink_post"

    ###--- Player Health

    imagebutton:
        xpos 720
        if boxing_health_player > 7:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 620
        if boxing_health_player > 6:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 520
        if boxing_health_player > 5:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 420
        if boxing_health_player > 4:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 320
        if boxing_health_player > 3:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 220
        if boxing_health_player > 2:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 120
        if boxing_health_player > 1:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 20
        if boxing_health_player > 0:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"


    ###--- Enemy Health

    imagebutton:
        xpos 1100
        if boxing_health_enemy > 7:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1200
        if boxing_health_enemy > 6:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1300
        if boxing_health_enemy > 5:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1400
        if boxing_health_enemy > 4:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1500
        if boxing_health_enemy > 3:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1600
        if boxing_health_enemy > 2:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1700
        if boxing_health_enemy > 1:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"

    imagebutton:
        xpos 1800
        if boxing_health_enemy > 0:
            idle "pixelheart_full_g"
        else:
            idle "pixelheart_empty_g"



label boxing_sam_riley_punch_outcome:

    if minigame_mode == 2:
        jump sam_riley_win

    if boxing_punched == 1:
        if rng_boxing_punched < 4:
            $ rng_boxing_punched += 1
        else:
            $ rng_boxing_punched = 1
        hide screen boxing_sr_sampunch_left
        hide screen boxing_sr_sampunch_right
        hide screen qte_boxing_sari_punch_1
        hide screen qte_boxing_sari_punch_2
        if rng_boxing_punched == 1 or rng_boxing_punched == 3:
            show boxing_sari_pr with Dissolve (0.00000001)
            $ renpy.pause (0.3, hard=True)
            play sound "sounds/se/se_punch_2.ogg"
        else:
            show boxing_sari_pl with Dissolve (0.00000001)
            $ renpy.pause (0.3, hard=True)
            play sound "sounds/se/se_punch_1.ogg"
        hide boxing_sari_idle
        hide boxing_sari_dl
        hide boxing_sari_dr
        $ boxing_health_enemy -= 1
        show transparent with hpunch
        $ renpy.pause (0.85, hard=True)
        show boxing_sari_idle with Dissolve (0.0000000001)
        hide boxing_sari_pl
        hide boxing_sari_pr
        hide transparent
        $ boxing_dodged = 0
        $ boxing_punched = 0
        jump boxing_sam_riley_repeat
    else:
        if rng_boxing_punched < 4:
            $ rng_boxing_punched += 1
        else:
            $ rng_boxing_punched = 1
        show boxing_sari_idle with Dissolve (0.000001)
        hide screen boxing_sr_sampunch_left
        hide screen boxing_sr_sampunch_right
        hide screen qte_boxing_sari_punch_1
        hide screen qte_boxing_sari_punch_2
        $ boxing_dodged = 0
        $ boxing_punched = 0
        jump boxing_sam_riley_repeat


#########################

label sam_riley_win:
$ boxing_kimbeatsmc = 1
show boxing_sari_rwin with Dissolve (0.000001, hard=True)
hide boxing_sari_idle
$ renpy.pause (1.0, hard=True)
play sound "sounds/se/se_bodyfall_1.ogg"
show boxing_sari_rcheer_1 with Dissolve (0.000001, hard=True)
hide boxing_sari_rwin
$ renpy.pause (0.4, hard=True)
show boxing_sari_rcheer_2 with Dissolve (0.000001, hard=True)
hide boxing_sari_rcheer_1
if minigame_mode == 2:
    show screen minigame_skip_image with dissolve
    $ renpy.pause (1.0, hard=True)
    hide screen minigame_skip_image
    hide screen poolparty_chickenfight_ui_3_dissolve
    with dissolve
$ renpy.pause (1.0, hard=True)
show boxing_rileywins with dissolve
$ renpy.pause ()
show blackscreen
hide boxing_sari_rcheer_2
hide screen sari_boxing_health
hide boxing_rileywins
hide boxing_kr_idle
with pixellate
$ renpy.pause (2.0)
if meetkim_globe_done == 1:
    $ renpy.block_rollback()
    $ unclickable = True
    stop music fadeout (1.0)
    if ptt_time == False:
        show screen comp_post_desktop with pixellate
    else:
        show screen comp_ptt_desktop with pixellate
    hide screen blackscreen
    hide blackscreen
    $ config.rollback_enabled = True
    $ _game_menu_screen = 'save'
    $ unclickable = False
    if ptt_time == False:
        jump comp_post_desktop
    else:
        jump comp_ptt_desktop
else:
    jump scene_globe_with_kim_outcome



label sam_riley_lose:
show boxing_sari_swin with Dissolve (0.000001, hard=True)
hide boxing_sari_idle
$ renpy.pause (1.0, hard=True)
play sound "sounds/se/se_bodyfall_1.ogg"
show boxing_sari_scheer_1 with Dissolve (0.000001, hard=True)
hide boxing_sari_swin
$ renpy.pause (0.5, hard=True)
show boxing_sari_scheer_2 with Dissolve (0.000001, hard=True)
hide boxing_sari_scheer_1
$ renpy.pause (1.0, hard=True)
show boxing_samwins with dissolve
$ renpy.pause ()
show blackscreen
hide boxing_sari_scheer_2
hide screen sari_boxing_health
hide boxing_samwins
hide boxing_kr_idle
with pixellate
$ renpy.pause (2.0)
if meetkim_globe_done == 1:
    $ renpy.block_rollback()
    $ unclickable = True
    stop music fadeout (1.0)
    if ptt_time == False:
        show screen comp_post_desktop with pixellate
    else:
        show screen comp_ptt_desktop with pixellate
    hide blackscreen
    $ config.rollback_enabled = True
    $ _game_menu_screen = 'save'
    $ unclickable = False
    if ptt_time == False:
        jump comp_post_desktop
    else:
            jump comp_ptt_desktop
else:
    jump scene_globe_with_kim_outcome






#- Riley Special -#

###--- Riley's Punches
###--- Top Left
transform boxing_dodge_riley_special_tl:
    linear 0.5 xpos -380 ypos -350

###--- Bottom Right
transform boxing_dodge_riley_special_tr:
    linear 0.5 xpos 400 ypos 300

###--- Bottom Left
transform boxing_dodge_riley_special_bl:
    linear 0.5 xpos -390 ypos 310

###--- Top Right
transform boxing_dodge_riley_special_br:
    linear 0.5 xpos 320 ypos -310

label sam_riley_special:

    if meetkim_globe_done == 0:
        k "Get your cameras ready. Watch this..."

    show boxing_sari_special_1 with Dissolve (0.00000001, hard=True)
    $ renpy.pause (1.0, hard=True)
    show boxing_sari_windup with Dissolve (0.00000001, hard=True)
    hide boxing_sari_idle
    hide boxing_sari_special_1
    $ renpy.pause (0.9, hard=True)
    if meetkim_globe_done == 0:
        k "Watch this... She's goin' down. Here it comes!"
    show screen qte_boxing_sari_special_1
    call screen qte_boxing_sari_special_timer


screen qte_boxing_sari_special_1:

    if qte_boxing_sari_special_timer >= 1 and boxing_dodged_special_1 == 0:
        imagebutton:
            idle "boxing_riley_dodge_right_special_g"
            at boxing_dodge_riley_special_tl
            focus_mask True
    if qte_boxing_sari_special_timer >= 2 and boxing_dodged_special_3 == 0:
        imagebutton:
            idle "boxing_riley_dodge_left_special_g"
            at boxing_dodge_riley_special_bl
            focus_mask True
    if qte_boxing_sari_special_timer >= 3 and boxing_dodged_special_2 == 0:
        imagebutton:
            idle "boxing_riley_dodge_right_special_g"
            at boxing_dodge_riley_special_tr
            focus_mask True
    if qte_boxing_sari_special_timer >= 4 and boxing_dodged_special_4 == 0:
        imagebutton:
            idle "boxing_riley_dodge_left_special_g"
            at boxing_dodge_riley_special_br
            focus_mask True

    timer 0.5 action SetVariable('qte_boxing_sari_special_timer', 1), Show ('qte_boxing_sari_4')
    timer 1.0 action SetVariable('qte_boxing_sari_special_timer', 2)
    timer 1.5 action SetVariable('qte_boxing_sari_special_timer', 3)
    timer 2.0 action SetVariable('qte_boxing_sari_special_timer', 4)
    timer 2.5 action SetVariable('qte_boxing_sari_special_timer', 5), Hide ('qte_boxing_sari_special_1')

screen qte_boxing_sari_4:

    if boxing_dodged_special_1 == 0 and qte_boxing_sari_special_timer >= 2:
        imagebutton:
            idle "boxing_riley_dodge_right_special_g"
            hover "boxing_riley_dodge_right_special_h"
            xpos -380 ypos -350
            focus_mask True
            action SetVariable ("boxing_dodged_special_1", 1) activate_sound "sounds/se/se_ding_1.ogg"
    if boxing_dodged_special_3 == 0 and qte_boxing_sari_special_timer >= 3:
        imagebutton:
            idle "boxing_riley_dodge_left_special_g"
            hover "boxing_riley_dodge_left_special_h"
            xpos -390 ypos 310
            focus_mask True
            action SetVariable ("boxing_dodged_special_3", 1) activate_sound "sounds/se/se_ding_1.ogg"
    if boxing_dodged_special_2 == 0 and qte_boxing_sari_special_timer >= 4:
        imagebutton:
            idle "boxing_riley_dodge_right_special_g"
            hover "boxing_riley_dodge_right_special_h"
            xpos 400 ypos 300
            focus_mask True
            action SetVariable ("boxing_dodged_special_2", 1) activate_sound "sounds/se/se_ding_1.ogg"
    if boxing_dodged_special_4 == 0 and qte_boxing_sari_special_timer >= 5:
        imagebutton:
            idle "boxing_riley_dodge_left_special_g"
            hover "boxing_riley_dodge_left_special_h"
            xpos 320 ypos -310
            focus_mask True
            action SetVariable ("boxing_dodged_special_4", 1) activate_sound "sounds/se/se_ding_1.ogg"


screen qte_boxing_sari_special_timer:

    if minigame_mode == 1:
        if boxing_dodged_special_1 == 1 and boxing_dodged_special_2 == 1 and boxing_dodged_special_3 == 1 and boxing_dodged_special_4 == 1:
            timer 0.5 action Hide('qte_boxing_sari_special_1'), Hide('qte_boxing_sari_4'), Jump('qte_boxing_sari_special_outcome') repeat True
    else:
        timer 5.0 action Hide('qte_boxing_sari_special_1'), Hide('qte_boxing_sari_4'), Jump('qte_boxing_sari_special_outcome')

label qte_sari_special_ezmode_check:
    if boxing_dodged_special_1 == 1 and boxing_dodged_special_2 == 1 and boxing_dodged_special_3 == 1 and boxing_dodged_special_4 == 1:
        hide screen qte_boxing_special_1
        hide screen qte_boxing_sari_4
        jump qte_boxing_sari_special_outcome
    return


label qte_boxing_sari_special_outcome:

    show screen disable_player_action
    show boxing_sari_special_2 with Dissolve (0.000001, hard=True)
    $ renpy.pause (0.3, hard=True)
    show boxing_sari_idle with Dissolve (0.0000001, hard=True)
    hide boxing_sari_special_2
    $ renpy.pause (0.00001, hard=True)

    if boxing_dodged_special_1 == 0:
        show boxing_sari_hr with Dissolve (0.000001, hard=True)
        hide boxing_sari_windup
        hide boxing_sari_idle
        $ renpy.pause (0.3, hard=True)
        play sound "sounds/se/se_punch_1.ogg"
        $ boxing_health_player -= 1
        show transparent with hpunch
        $ renpy.pause (0.55, hard=True)
        hide transparent
    else:
        show boxing_sari_dr with Dissolve (0.000001, hard=True)
        $ renpy.pause (0.3, hard=True)
        $ renpy.pause (0.000001, hard=True)
        $ boxing_punch_special_1 = 1
        hide boxing_sari_windup
        hide boxing_sari_idle
        play sound "sounds/se/se_dodge_1.ogg"
        $ renpy.pause (0.55, hard=True)
        hide transparent


    if boxing_dodged_special_2 == 0:
        show boxing_sari_hl with Dissolve (0.000001, hard=True)
        hide boxing_sari_windup
        hide boxing_sari_hr
        hide boxing_sari_dr
        hide boxing_sari_idle
        $ renpy.pause (0.3, hard=True)
        play sound "sounds/se/se_punch_2.ogg"
        $ boxing_health_player -= 1
        show transparent with hpunch
        $ renpy.pause (0.60, hard=True)
        hide transparent
    else:
        show boxing_sari_dl with Dissolve (0.000001, hard=True)
        $ renpy.pause (0.3, hard=True)
        $ renpy.pause (0.5, hard=True)
        $ boxing_punch_special_2 = 1
        hide boxing_sari_windup
        hide boxing_sari_hr
        hide boxing_sari_dr
        hide boxing_sari_idle
        play sound "sounds/se/se_dodge_2.ogg"
        $ renpy.pause (0.25, hard=True)
        hide transparent


    if boxing_dodged_special_3 == 0:
        show boxing_sari_hr with Dissolve (0.000001, hard=True)
        hide boxing_sari_windup
        hide boxing_sari_hl
        hide boxing_sari_dl
        hide boxing_sari_idle
        $ renpy.pause (0.3, hard=True)
        play sound "sounds/se/se_punch_1.ogg"
        $ boxing_health_player -= 1
        show transparent with hpunch
        $ renpy.pause (0.55, hard=True)
        hide transparent
    else:
        show boxing_sari_dr with Dissolve (0.000001, hard=True)
        $ renpy.pause (0.3, hard=True)
        $ boxing_punch_special_3 = 1
        hide boxing_sari_windup
        hide boxing_sari_hl
        hide boxing_sari_dl
        hide boxing_sari_idle
        play sound "sounds/se/se_dodge_1.ogg"
        $ renpy.pause (0.55, hard=True)
        hide transparent


    if boxing_dodged_special_4 == 0:
        show boxing_sari_hl with Dissolve (0.000001, hard=True)
        $ renpy.pause (0.3, hard=True)
        hide boxing_sari_windup
        hide boxing_sari_hr
        hide boxing_sari_dr
        hide boxing_sari_idle
        play sound "sounds/se/se_punch_2.ogg"
        $ boxing_health_player -= 1
        show transparent with hpunch
        $ renpy.pause (0.60, hard=True)
        hide transparent
    else:
        show boxing_sari_dl with Dissolve (0.000001, hard=True)
        $ renpy.pause (0.3, hard=True)
        $ renpy.pause (0.5, hard=True)
        $ boxing_punch_special_4 = 1
        hide boxing_sari_windup
        hide boxing_sari_hr
        hide boxing_sari_dr
        hide boxing_sari_idle
        play sound "sounds/se/se_dodge_2.ogg"
        $ renpy.pause (0.25, hard=True)
        hide transparent

    show boxing_sari_idle with Dissolve (0.0000001, hard=True)
    hide boxing_sari_windup
    hide boxing_sari_hr
    hide boxing_sari_dr
    hide boxing_sari_hl
    hide boxing_sari_dl
    $ boxing_riley_special_counter = 0
    $ renpy.pause (0.5, hard=True)
    hide screen disable_player_action



    jump boxing_sam_riley_repeat


##########
