# Overrides other preference screens #
init 101 python:
    def click_to_continue_animation(st, at):
        frame = int(st / .03)

        if frame >= 30:
            frame = 0

        return Image("ctc_" + str(frame) + ".png"), 0.03

style reset_volume_button is check_button
style reset_volume_text is check_button_text

init 100:
    screen preferences():

        tag menu

        if renpy.mobile:
            $ cols = 2
        else:
            $ cols = 4

        if not wholesome_mode:
            use game_menu(_("Preferences"), scroll="viewport"):

                vbox:

                    hbox:
                        spacing 50
                        box_wrap True

                        if renpy.variant("pc"):

                            vbox:
                                style_prefix "radio"
                                label _("Display")
                                textbutton _("Window") action Preference("display", "window")
                                textbutton _("Fullscreen") action Preference("display", "fullscreen")

                        vbox:
                            style_prefix "radio"
                            label _("Rollback Side")
                            textbutton _("Disable") action Preference("rollback side", "disable")
                            textbutton _("Left") action Preference("rollback side", "left")
                            textbutton _("Right") action Preference("rollback side", "right")

                        vbox:
                            style_prefix "check"
                            label _("Skip")
                            textbutton _("Unseen Text") action Preference("skip", "toggle")
                            textbutton _("After Choices") action Preference("after choices", "toggle")
                            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                        vbox:
                            style_prefix "check"
                            label _("Extra")

                            if not wholesome_mode:
                                textbutton _("Disable Splash") action ToggleField(persistent, 'disable_splash_movie', True, False)
                                textbutton _("Disable Warning") action ToggleField(persistent, 'disable_warning', True, False)
                                textbutton _("Disable Dream Music") action ToggleField(persistent, 'disable_dream_music', True, False)
                                textbutton _("Disable Dream Blur") action ToggleField(persistent, 'disable_dream_blur', True, False)
                                textbutton _("Enable Sex Sounds") action ToggleField(persistent, 'enable_sex_sounds', True, False)
                                textbutton _("Mousewheel Choice Scroll") action ToggleField(persistent, 'mouse_wheel_choice_scroll', True, False)
                                textbutton _("Use \"Incestral Awakening\" As Name") action ToggleField(persistent, 'use_incestral_awakening_name', True, False)

                                if not main_menu:
                                    textbutton _("Hide [sa.say_name] ! Notification") action ToggleField(persistent, 'hide_sam_notification', True, False)
                                    textbutton _("Hide [si.say_name] ! Notification") action ToggleField(persistent, 'hide_simone_notification', True, False)
                                    textbutton _("Hide [k.say_name] ! Notification") action ToggleField(persistent, 'hide_kira_notification', True, False)

                                    if store.had_julia_arrived_scene:
                                        textbutton _("Hide [julia.say_name] ! Notification") action ToggleField(persistent, 'hide_julia_notification', True, False)

                                    if store.had_janet_intro_scene:
                                        textbutton _("Hide [janet.say_name] ! Notification") action ToggleField(persistent, 'hide_janet_notification', True, False)

                                    if store.had_edna_intro_scene:
                                        textbutton _("Hide [edna.say_name] ! Notification") action ToggleField(persistent, 'hide_edna_notification', True, False)

                                    if store.had_vicky_intro_scene:
                                        textbutton _("Hide Vicky ! Notification") action ToggleField(persistent, 'hide_vicky_notification', True, False)

                                    if "gloryhole_handjob_scene" in store.scenes_completed:
                                        textbutton _("Hide Kacey ! Notification") action ToggleField(persistent, 'hide_kacey_notification', True, False)
                                    else:
                                        textbutton _("Hide Park ! Notification") action ToggleField(persistent, 'hide_kacey_notification', True, False)

#                                    if had_beach_intro:
#                                       textbutton _("Hide Beach ! Notification") action ToggleField(persistent, 'hide_beach_notification', True, False)

                use mods_preferences       
                style_prefix "check"
            
                for mod_option in mod_options():
                    textbutton _(mod_option[0]) action ToggleField(persistent, mod_option[1], True, False)

                if persistent.leftovers_mod_detected:
                    vbox:
                        style_prefix "check"
                        label _("Leftovers-Mod")

                        for mod_leftovers_option in mod_leftovers_options():
                            textbutton _(mod_leftovers_option[0]) action ToggleField(persistent, mod_leftovers_option[1], True, False)

                    hbox:
                        style_prefix "slider"
                        box_wrap True

                        vbox:

                            label _("Text Speed")

                            bar value Preference("text speed")

                            label _("Auto-Forward Time")

                            bar value Preference("auto-forward time")

                        use audio_preferences

                    if main_menu:
                        vbox:
                            label _("Daytime (Home) Music")
                            style_prefix "check"
                            use music_disable_vbox( disable_audio_filenames( home_daytime_music_list() ) )

                        vbox:
                            label _("Evening (Home) Music")
                            style_prefix "check"
                            use music_disable_vbox( disable_audio_filenames( home_evening_music_list() ) )

                        vbox:
                            label _("Daytime (Outside) Music")
                            style_prefix "check"
                            use music_disable_vbox( disable_audio_filenames( outside_daytime_music_list() ) )
                        vbox:
                            label _("Evening (Outside) Music")
                            style_prefix "check"
                            use music_disable_vbox( disable_audio_filenames( outside_evening_music_list() ) )