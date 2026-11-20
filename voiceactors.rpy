



screen voiceactors():

    tag menu

    use game_menu(_("Voice Actors")):







    #- Little Clover - Penelope Rivera

        imagebutton:
            idle "voiceactor_littleclover"
            xpos 250 ypos 20

        imagebutton:
            idle "voiceactor_littleclover_text"
            xpos 220 ypos -40



        imagebutton:
            xpos 530 ypos 20
            idle "voiceactor_littleclover_penny_1"
            focus_mask True

        imagebutton:
            xpos 530 ypos 20
            idle "voiceactor_littleclover_penny_2"
            focus_mask True
            if va_penny == 2:
                at ts_fadeout
            elif va_penny == 1:
                at ts_fade

        imagebutton:
            idle "voiceactor_penny_text"
            xpos 485 ypos -20


        if va_penny == 1:
            timer 5.0 action SetVariable ("va_penny", 2) repeat True
        elif va_penny == 2:
            timer 5.0 action SetVariable ("va_penny", 1) repeat True

        #- Plugs

        imagebutton:
            xpos 467 ypos 55
            idle "ib_voiceactors_onlyfans_g"
            hover im.MatrixColor("voiceactors/ib_voiceactors_onlyfans_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://onlyfans.com/petit_trefle")

        imagebutton:
            xpos 467 ypos 125
            idle "ib_voiceactors_patreon_g"
            hover im.MatrixColor("voiceactors/ib_voiceactors_patreon_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://www.patreon.com/littleclovercosplay")

        imagebutton:
            xpos 467 ypos 195
            idle "ib_voiceactors_twitter_g"
            hover im.MatrixColor("voiceactors/ib_voiceactors_twitter_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://twitter.com/petit_trefle_xo")

        imagebutton:
            xpos 467 ypos 265
            idle "ib_voiceactors_discord_g"
            hover im.MatrixColor("voiceactors/ib_voiceactors_discord_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://discord.com/invite/littlecloverwhispers")
