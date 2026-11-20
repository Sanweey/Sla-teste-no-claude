



screen musiccredit():

    tag menu

    use game_menu(_("Music Credit")):







    #- Koethe



        imagebutton:
            idle "ib_musiccredit_koethe_koethe_1_g"
            xpos 250 ypos -40
            focus_mask True



        if mc_koethe in (4, 1):
            imagebutton:
                xpos 250 ypos -40
                idle "ib_musiccredit_koethe_koethe_4_g"
                focus_mask True
                if mc_koethe == 1:
                    at ts_fadeout
                elif mc_koethe == 4:
                    at ts_fade

        if mc_koethe in (3, 4):
            imagebutton:
                xpos 250 ypos -40
                idle "ib_musiccredit_koethe_koethe_3_g"
                focus_mask True
                if mc_koethe == 4:
                    at ts_fadeout
                elif mc_koethe == 3:
                    at ts_fade


        if mc_koethe in (2, 3):
            imagebutton:
                xpos 250 ypos -40
                idle "ib_musiccredit_koethe_koethe_2_g"
                focus_mask True
                if mc_koethe == 3:
                    at ts_fadeout
                elif mc_koethe == 2:
                    at ts_fade




        #-Hover Image:
        imagebutton:
            xpos 250 ypos -40
            focus_mask True
            idle "ib_musiccredit_koethe_hovered_1"
            hover "ib_musiccredit_koethe_hovered_2"
            hovered ShowTransient("hover_koethe_songs_list_g") unhovered Hide("hover_koethe_songs_list_g")
            action NullAction()

        imagebutton:
            idle "ib_musiccredit_koethe_text"
            xpos 480 ypos -10






        if mc_koethe == 0:
            timer 5.0 action SetVariable ("mc_koethe", 2) repeat True
        elif mc_koethe == 1:
            timer 5.0 action SetVariable ("mc_koethe", 2) repeat True
        elif mc_koethe == 2:
            timer 5.0 action SetVariable ("mc_koethe", 3) repeat True
        elif mc_koethe == 3:
            timer 5.0 action SetVariable ("mc_koethe", 4) repeat True
        elif mc_koethe == 4:
            timer 5.0 action SetVariable ("mc_koethe", 1) repeat True

        #- Plugs

        imagebutton:
            xpos 658 ypos 76
            idle "ib_musiccredit_youtube_g"
            hover im.MatrixColor("musiccredit/ib_musiccredit_youtube_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://www.youtube.com/c/KoetheKoethe/videos")

        imagebutton:
            xpos 726 ypos 76
            idle "ib_voiceactors_twitter_g"
            hover im.MatrixColor("voiceactors/ib_voiceactors_twitter_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://twitter.com/koethekoethe")

        imagebutton:
            xpos 794 ypos 76
            idle "ib_musiccredit_spotify_g"
            hover im.MatrixColor("musiccredit/ib_musiccredit_spotify_g.png", im.matrix.brightness(0.15))
            focus_mask True
            action OpenURL("https://open.spotify.com/artist/2zLxo07EbSedKk5YsnyacC")






screen hover_koethe_songs_list_g:

    imagebutton:
        xpos 980 ypos 320
        idle "hover_koethe_songs_list_g"
        focus_mask True
