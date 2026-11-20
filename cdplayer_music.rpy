



label cdplayer_pbedroom:

    $ unclickable = True
    show blackscreen
    hide screen screen_home_post_pbedroom
    with dissolve
    $ unclickable = False

    image audio_wave = Movie(channel="movies/misc/audio_wave.webm", play="movies/misc/audio_wave.webm", size=(1580,130))
    image cdplayer_mc_ltm_day = Movie(channel="movies/misc/cdplayer_mc_ltm_day.webm", play="movies/misc/cdplayer_mc_ltm_day.webm")
    image cdplayer_mc_ltm2_day = Movie(channel="movies/misc/cdplayer_mc_ltm2_day.webm", play="movies/misc/cdplayer_mc_ltm2_day.webm")
    image cdplayer_mc_ltm3_day = Movie(channel="movies/misc/cdplayer_mc_ltm3_day.webm", play="movies/misc/cdplayer_mc_ltm3_day.webm")
    image cdplayer_mc_ltm_night = Movie(channel="movies/misc/cdplayer_mc_ltm_night.webm", play="movies/misc/cdplayer_mc_ltm_night.webm")
    image cdplayer_mc_ltm2_night = Movie(channel="movies/misc/cdplayer_mc_ltm2_night.webm", play="movies/misc/cdplayer_mc_ltm2_night.webm")
    image cdplayer_mc_ltm3_night = Movie(channel="movies/misc/cdplayer_mc_ltm3_night.webm", play="movies/misc/cdplayer_mc_ltm3_night.webm")

    hide cdplayer_pbedroom_day_1_g
    hide cdplayer_pbedroom_day_2_g

    if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
        show cdplayer_pbedroom_day_1_g
        show cdplayer_pbedroom_speakers_01_day
        with dissolve
        hide blackscreen
    else:
        show cdplayer_pbedroom_night_1_g
        show cdplayer_pbedroom_speakers_01_night
        with dissolve
        hide blackscreen

    if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
        show cdplayer_pbedroom_speakers_01_day
        hide cdplayer_pbedroom_speakers_02_day
    else:
        show cdplayer_pbedroom_speakers_01_night
        hide cdplayer_pbedroom_speakers_02_night

label cdplayer_pbedroom_options:

    menu:

        "'Storm' - Koethe" if cdplayer_pbedroom_koethe_price == 0:
            $ renpy.pause (0.5, hard=True)
            call cdplayer_song_stop from _call_cdplayer_song_stop
            $ cdplayer_pbedroom_koethe_storm = 1
            stop music fadeout (1.0)
            play sound "sounds/se/se_click_2.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_day_2_g
                show cdplayer_pbedroom_music_on_day
                hide cdplayer_pbedroom_day_1_g
            else:
                show cdplayer_pbedroom_night_2_g
                show cdplayer_pbedroom_music_on_night
                hide cdplayer_pbedroom_night_1_g


            show audio_wave:
                xpos 173 ypos 620

            $ cdplayer_pbedroom_on = 1

            play music "sounds/me/m_koethe_storm.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_music_on_day
                hide cdplayer_pbedroom_speakers_01_day
            else:
                show cdplayer_pbedroom_music_on_night
                hide cdplayer_pbedroom_speakers_01_night

            $ renpy.pause (0.5, hard=True)


            jump cdplayer_musicplaying





        "'Price' - Koethe" if cdplayer_pbedroom_koethe_price == 0:
            $ renpy.pause (0.5, hard=True)
            call cdplayer_song_stop from _call_cdplayer_song_stop_1
            $ cdplayer_pbedroom_koethe_price = 1
            stop music fadeout (1.0)
            play sound "sounds/se/se_click_2.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_day_2_g
                show cdplayer_pbedroom_music_on_day
                hide cdplayer_pbedroom_day_1_g
            else:
                show cdplayer_pbedroom_night_2_g
                show cdplayer_pbedroom_music_on_night
                hide cdplayer_pbedroom_night_1_g

            show audio_wave:
                xpos 173 ypos 620

            $ cdplayer_pbedroom_on = 1

            play music "sounds/me/m_koethe_price.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_music_on_day
                hide cdplayer_pbedroom_speakers_01_day
            else:
                show cdplayer_pbedroom_music_on_night
                hide cdplayer_pbedroom_speakers_01_night


            $ renpy.pause (0.5, hard=True)

        "'Only One' - Koethe" if cdplayer_pbedroom_koethe_onlyone == 0:
            $ renpy.pause (0.5, hard=True)
            call cdplayer_song_stop from _call_cdplayer_song_stop_2
            $ cdplayer_pbedroom_koethe_onlyone = 1
            stop music fadeout (1.0)
            play sound "sounds/se/se_click_2.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_day_2_g
                show cdplayer_pbedroom_music_on_day
                hide cdplayer_pbedroom_day_1_g
            else:
                show cdplayer_pbedroom_night_2_g
                show cdplayer_pbedroom_music_on_night
                hide cdplayer_pbedroom_night_1_g

            show audio_wave:
                xpos 173 ypos 620

            $ cdplayer_pbedroom_on = 1

            play music "sounds/me/m_koethe_onlyone.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_music_on_day
                hide cdplayer_pbedroom_speakers_01_day
            else:
                show cdplayer_pbedroom_music_on_night
                hide cdplayer_pbedroom_speakers_01_night


            $ renpy.pause (0.5, hard=True)


        "Back":
            $ unclickable = True
            if cdplayer_pbedroom_on == 1:
                $ renpy.pause (0.5, hard=True)
                stop music fadeout (1.0)
                play sound "sounds/se/se_click_2.ogg"
                if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                    show cdplayer_pbedroom_day_1_g
                    hide cdplayer_pbedroom_day_2_g
                else:
                    show cdplayer_pbedroom_night_1_g
                    hide cdplayer_pbedroom_night_2_g
                $ cdplayer_pbedroom_on = 0
                if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                    show cdplayer_pbedroom_speakers_01_day
                    hide cdplayer_pbedroom_music_on_day
                else:
                    show cdplayer_pbedroom_speakers_01_night
                    hide cdplayer_pbedroom_music_on_night

            show blackscreen with dissolve
            hide cdplayer_pbedroom_speakers_01_day
            hide cdplayer_pbedroom_speakers_02_day
            hide cdplayer_pbedroom_speakers_01_night
            hide cdplayer_pbedroom_speakers_02_night
            hide cdplayer_pbedroom_day_1_g
            hide cdplayer_pbedroom_day_2_g
            hide cdplayer_pbedroom_night_1_g
            hide cdplayer_pbedroom_night_2_g
            hide audio_wave
            $ cdplayer_pbedroom_on = 0
            call cdplayer_song_stop from _call_cdplayer_song_stop_3
            show screen screen_home_post_pbedroom with dissolve
            hide blackscreen
            $ unclickable = False
            jump screen_home_post_pbedroom



label cdplayer_musicplaying:

    $ renpy.pause (0.5, hard=True)

    menu:

        "{color=#73C74C}'Storm' - Koethe (disabled)" if cdplayer_pbedroom_koethe_storm == 1:
            jump cdplayer_pbedroom_options

        "{color=#73C74C}'Price' - 'Koethe' (disabled)" if cdplayer_pbedroom_koethe_price == 1:
            jump cdplayer_pbedroom_options
        "{color=#73C74C}'Only One' - 'Koethe' (disabled)" if cdplayer_pbedroom_koethe_onlyone == 1:
            jump cdplayer_pbedroom_options





        "Change Song":
            if cdplayer_pbedroom_on == 2:
                hide blackscreen
                hide screen ltm_relax_animations
                hide cdplayer_mc_ltm_day
                hide cdplayer_relax_speaker_day
                hide cdplayer_mc_ltm_night
                hide cdplayer_relax_speaker_night
                with dissolve
            $ renpy.pause (0.5, hard=True)
            stop music fadeout (1.0)
            play sound "sounds/se/se_click_2.ogg"
            call cdplayer_song_stop from _call_cdplayer_song_stop_4

            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_day_1_g
                hide cdplayer_pbedroom_day_2_g
            else:
                show cdplayer_pbedroom_night_1_g
                hide cdplayer_pbedroom_night_2_g
            $ cdplayer_pbedroom_on = 0
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_speakers_01_day
                hide cdplayer_pbedroom_music_on_day
            else:
                show cdplayer_pbedroom_speakers_01_night
                hide cdplayer_pbedroom_music_on_night

            $ cdplayer_pbedroom_on = 0
            $ renpy.pause (0.5, hard=True)

            hide audio_wave
            jump cdplayer_pbedroom_options

        "Relax and Listen" if not cdplayer_pbedroom_on == 2:

            $ ts_images = 0
            $ renpy.pause (0.5, hard=True)
            $ cdplayer_pbedroom_on = 2
            if time_of_day_present == 'NIGHT':
                show blackscreen
                show screen ltm_relax_animations

                with Dissolve (2.0)
            else:
                show blackscreen
                show screen ltm_relax_animations
                with Dissolve (2.0)

            jump cdplayer_musicplaying

        "Back":


            if cdplayer_pbedroom_on == 2:
                hide screen ltm_relax_animations
                hide cdplayer_mc_ltm_day
                hide cdplayer_relax_speaker_day
                hide cdplayer_mc_ltm_night
                hide cdplayer_relax_speaker_night
                hide blackscreen
                with dissolve
            $ renpy.pause (0.5, hard=True)
            $ unclickable = True
            hide cdplayer_mc_ltm with dissolve
            $ renpy.pause (1.0, hard=True)
            stop music fadeout (1.0)
            play sound "sounds/se/se_click_2.ogg"
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_day_1_g
                hide cdplayer_pbedroom_day_2_g
            else:
                show cdplayer_pbedroom_night_1_g
                hide cdplayer_pbedroom_night_2_g
            $ cdplayer_pbedroom_on = 0
            if time_of_day_present in ("MORNING", "AFTERNOON", "EVENING"):
                show cdplayer_pbedroom_speakers_01_day
                hide cdplayer_pbedroom_music_on_day
            else:
                show cdplayer_pbedroom_speakers_01_night
                hide cdplayer_pbedroom_music_on_night

            $ renpy.pause (0.5, hard=True)

            show blackscreen with dissolve
            hide cdplayer_pbedroom_speakers_01_day
            hide cdplayer_pbedroom_speakers_02_day
            hide cdplayer_pbedroom_speakers_01_night
            hide cdplayer_pbedroom_speakers_02_night
            hide cdplayer_pbedroom_day_1_g
            hide cdplayer_pbedroom_day_2_g
            hide cdplayer_pbedroom_night_1_g
            hide cdplayer_pbedroom_night_2_g
            hide audio_wave
            $ cdplayer_pbedroom_on = 0
            call cdplayer_song_stop from _call_cdplayer_song_stop_5
            show screen screen_home_post_pbedroom with dissolve
            hide blackscreen
            $ unclickable = False
            jump screen_home_post_pbedroom




label cdplayer_song_stop:
    $ cdplayer_pbedroom_koethe_storm = 0
    $ cdplayer_pbedroom_koethe_price = 0
    $ cdplayer_pbedroom_koethe_onlyone = 0
    return


image cdplayer_pbedroom_music_on_day:
    "locations/home_post/pbedroom/cdplayer_pbedroom_speakers_01_day.png"
    pause 0.2
    "locations/home_post/pbedroom/cdplayer_pbedroom_speakers_02_day.png"
    pause 0.2
    repeat

image cdplayer_pbedroom_music_on_night:
    "locations/home_post/pbedroom/cdplayer_pbedroom_speakers_01_night.png"
    pause 0.2
    "locations/home_post/pbedroom/cdplayer_pbedroom_speakers_02_night.png"
    pause 0.2
    repeat

image cdplayer_relax_speaker_day:
    "locations/home_post/pbedroom/cdplayer_relax_speaker_1_day.png"
    pause 0.2
    "locations/home_post/pbedroom/cdplayer_relax_speaker_2_day.png"
    pause 0.2
    repeat

image cdplayer_relax_speaker2_day:
    "locations/home_post/pbedroom/cdplayer_relax_speaker2_1_day.png"
    pause 0.2
    "locations/home_post/pbedroom/cdplayer_relax_speaker2_2_day.png"
    pause 0.2
    repeat

image cdplayer_relax_speaker_night:
    "locations/home_post/pbedroom/cdplayer_relax_speaker_1_night.png"
    pause 0.2
    "locations/home_post/pbedroom/cdplayer_relax_speaker_2_night.png"
    pause 0.2
    repeat

image cdplayer_relax_speaker2_night:
    "locations/home_post/pbedroom/cdplayer_relax_speaker2_1_night.png"
    pause 0.2
    "locations/home_post/pbedroom/cdplayer_relax_speaker2_2_night.png"
    pause 0.2
    repeat


screen ltm_relax_animations:


    if ts_images in (0, 1, 2):
        imagebutton:
            if time_of_day_present == 'NIGHT':
                idle "cdplayer_mc_ltm_night"
            else:
                idle "cdplayer_mc_ltm_day"
            if ts_images == 2:
                at ts_fadeout
            else:
                at ts_fade

        imagebutton:
            if time_of_day_present == 'NIGHT':
                idle "cdplayer_relax_speaker_night"
            else:
                idle "cdplayer_relax_speaker_day"
            xpos 695 ypos 517
            if ts_images == 2:
                at ts_fadeout
            else:
                at ts_fade


    if ts_images in (2, 3):
        imagebutton:
            if time_of_day_present == 'NIGHT':
                idle "cdplayer_mc_ltm2_night"
            else:
                idle "cdplayer_mc_ltm2_day"
            if ts_images == 3:
                at ts_fadeout
            else:
                at ts_fade

        imagebutton:
            if time_of_day_present == 'NIGHT':
                idle "cdplayer_relax_speaker2_night"
            else:
                idle "cdplayer_relax_speaker2_day"
            xpos 140 ypos 125
            if ts_images == 3:
                at ts_fadeout
            else:
                at ts_fade

    if ts_images in (3, 1):
        imagebutton:
            if time_of_day_present == 'NIGHT':
                idle "cdplayer_mc_ltm3_night"
            else:
                idle "cdplayer_mc_ltm3_day"
            if ts_images == 1:
                at ts_fadeout
            else:
                at ts_fade


    if ts_images == 0:
        timer 10.0 action SetVariable ("ts_images", 2) repeat True
    elif ts_images == 1:
        timer 10.0 action SetVariable ("ts_images", 2) repeat True
    elif ts_images == 2:
        timer 10.0 action SetVariable ("ts_images", 3) repeat True
    elif ts_images == 3:
        timer 10.0 action SetVariable ("ts_images", 1) repeat True
