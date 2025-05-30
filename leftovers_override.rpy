# This file covers the following: #
# 1. Alters the existing splashscreen, and alerts the player if Leftovers is unable to be detected correctly
# 2. Serves as the built-in compatibility with Cru's Epilogue Remake Mod.
# 3. Has it's own unique splashscreen, that if combined with Cru's mod, will say that it has detected both
# 3. Updates the Preference Menu with Leftovers-Mod features, like Smol Tits and Enable Extra Music Tracks
# 4. New unique, conditional dialogue for Julia wearing her swimsuit during the pool party chat. Janet and Sam commenting on Julia's swimsuit to have it be present tense. She's embarrassed about wearing it in front of everybody.
# 4.1 Adds, and fixes dialogue/bust art checks for Sam and Simone's swimsuits during the same pool party chat.
# 4.2 If you haven't bought their swimsuits when you play this scene, this is now consistently shown instead of Simone having a swimsuit by default, for example, when she talks about Kacey and Vicky.

# 27/04/25 Added an addiitonal Ren'py.exists check that prevents a crash if you only have Leftovers installed

default persistent.version_1_1_changelog_read = False
default persistent.leftovers_mod_detected = True

init 101 python:
    def click_to_continue_animation(st, at):
        frame = int(st / .03)

        if frame >= 30:
            frame = 0

        return Image("ctc_" + str(frame) + ".png"), 0.03

init python:
    def mod_options():
        return []

init 1 python:
    config.label_overrides["splashscreen"] = "splashscreen_leftovers"

label splashscreen_leftovers:
    show bg black

#    if not renpy.exists('mods/leftovers_mod_v03/images/interface/Kacey_Face_Icon_Hidden.png'): #testing, intentionally incorrect filepath
    if not renpy.exists('mods/leftovers_mod/images/interface/Kacey_Face_Icon_Hidden.png'):
        "Incorrect file path detected! \nLeftovers Mod was not installed correctly. \nYour file path should be \"game/mods/leftovers_mod\"."
        "Now exiting game."
        $ renpy.quit()
        return

# Detects Cru's Remake Mod #
    if renpy.exists('mods/pregnancy_epilogue_remake_mod/scripts/pregnancy_epilogue_remake_menu.rpy'):
        $ store.pregnancy_epilogue_remake_mod_detected = True

    show bg warning

    if renpy.exists('mods/pregnancy_epilogue_remake_mod/scripts/pregnancy_epilogue_remake_menu.rpy'):
        if store.pregnancy_epilogue_remake_mod_detected:
            show screen splash_text_leftovers_cru
    else:
        show screen splash_text_leftovers

    with dissolve
    $ renpy.pause(2)
    show splash_ctc
    $ renpy.pause()

    hide screen splash_text_leftovers
    hide screen splash_text_leftovers_cru
    hide splash_ctc

    show bg black
    with Dissolve(0.75)

    if not persistent.version_1_1_changelog_read:
        show screen changelog
        pause
        $ persistent.version_1_1_changelog_read = True
        hide screen changelog

    return

init 2:
    screen splash_text_leftovers_cru:
        vbox:
            xalign 0.5
            yalign 0.5

            text "{b}Leftovers Mod + Cru's Remake Mod detected!{/b}" size 40 xalign 0.5
            text "See below:" size 32 xalign 0.5
            text "Both mods are now active!" size 24 xalign 0.5
            text "To see the content featured in the Pregnancy Epilogue Remake Mod, select \"View the Epilogue\" in Nate's bedroom, and play through it." size 24 xalign 0.5
            text "Report any issues to the IA Discord, and/or Reddle's IA1 Mods Empornium or the IA Modding Thread on AllTheFallen." size 24 xalign 0.5
            text "Thank you for playing these mods!" size 24 xalign 0.5

init 100:
    screen splash_text_leftovers:
        vbox:
            xalign 0.5
            yalign 0.5

            text "{b}Leftovers Mod now active!{/b}" size 69 xalign 0.5 #color "#FFFF00"
            text "See below:" size 32 xalign 0.5
            text "This mod is currently a work-in-progress!" size 24 xalign 0.5
            text "Please refer to the README!" size 24 xalign 0.5
            text "Be sure to make new saves just in case of potential issues!" size 24 xalign 0.5
            text "Report any bugs to the IA Discord, and/or Reddle's IA Mods Empornium, or the IA Modding Thread on AllTheFallen." size 24 xalign 0.5
            text "Thank you for playing this mod!" size 24 xalign 0.5

#            if not renpy.exists('mods/leftovers_mod_v03/images/interface/Kacey_Face_Icon_Hidden.png'):
#                text "Leftovers mod is not installed correctly." xalign 0.5 size 69 color "#ff0000"

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

                    vbox:
                        style_prefix "check"
                        label _("Mods")

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

                        vbox:

                            if config.has_music:
                                label _("Music Volume")

                                hbox:
                                    bar value Preference("music volume")

                            if config.has_sound:

                                label _("Sound Volume")

                                hbox:
                                    bar value Preference("sound volume")

                                    if config.sample_sound:
                                        textbutton _("Test") action Play("sound", config.sample_sound)


                            if config.has_voice:
                                label _("Voice Volume")

                                hbox:
                                    bar value Preference("voice volume")

                                    if config.sample_voice:
                                        textbutton _("Test") action Play("voice", config.sample_voice)

                            if config.has_music or config.has_sound or config.has_voice:
                                null height gui.pref_spacing

                                textbutton _("Reset Volume"):
                                    action Function(reset_volume)
                                    style "reset_volume_button"

                                textbutton _("Mute All"):
                                    action Preference("all mute", "toggle")
                                    style "mute_all_button"

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

# Julia wearing her new swimsuit during the pool party #
init 1000 python:
    config.label_overrides["day_dream"] = "day_dream_leftovers"

label day_dream_leftovers:
    python:
        choice_list = []

        dream_chars = npc_list()
        for dream_char in dream_chars:
            if dreams_enabled and len(dream_char.replayable_scenes) > 0:
                choice_list.append( ("Dream about " + dream_char.say_name, dream_char.variable_name) )

        if "finale_scene" in scenes_completed:
            choice_list.append( ("Dream about the pool party", "finale_scene_leftovers") )

        choice_list.append( ("Back", "back") )

        chosen_option = renpy.display_menu(choice_list)

    if chosen_option == "back":
        call day_manual_sleep
    elif chosen_option == "finale_scene_leftovers":
        python hide:
            if not persistent.disable_dream_music:
                music_name = "Dreamland.ogg" if random.randint(1, 2) == 1 else "Dreamland_02.ogg"
                music_name = "audio/music/" + music_name

                play_music(music_name, fadeout = 1.0)
            renpy.call(chosen_option + "_sex", dream = True)
    else:
        call character_dream_menu(eval(chosen_option))

    return

init 1000 python:
    config.label_overrides["finale_scene"] = "finale_scene_leftovers"
    config.label_overrides["finale_scene_sex"] = "finale_scene_sex_leftovers"

label finale_scene_leftovers(dream = False):
    call finale_scene_leftovers_sex(dream = dream)

    return

label finale_scene_leftovers_sex(dream = False):
    $ renpy.start_predict("edna_titfuck_nude_anim")

    call finale_scene_initialize

    if finale_julia_sam:
        $ finale_fucked_amount_goal = 8
    else:
        $ finale_fucked_amount_goal = 6

    call process_scene_beginning(bg = "bg kira_room_evening", char_tuple_array = [], dream = dream)

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Tonight's ideal for a jog!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(The temperatures are starting to get cooler)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(I should get [n.say_name] to join me)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(It'll give him a change of pace from the running track)"


    call process_new_location(bg = "bg nate_room_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Hey [n.say_name]!"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "{cps=40}You wanna go-{/cps}{w=0.75}{nw}"

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "(Where the hell is he?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(I know he's not fucking Mom, she's downstairs cleaning the kitchen)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(I didn't see him in [sa.say_name]'s room either)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(I'll try calling him)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(If he doesn't answer, then I'll just go by myself)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "..."


    "{i}Ring-Ring-Ring!{/i}"

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "..."


    "{i}Ring-Ring-Ring!{/i}"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(What the...)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(Seriously [n.say_name]?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(You left your phone in your room?)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "{i}Sigh.{/i}.."

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(My brother can be a flake sometimes...)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(One of these days his phone will get lost or stolen, it's inevitable)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(I bet he doesn't even have a password on his phone)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Yep, knew it!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(I can just open his phone with no effort!)"


    "{i}Ding!{/i}"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(And of course a text comes in)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(Whoever sent it will have to wait a while for a response from my brother)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "([gloryhole_girl.say_name]?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(I've never heard [n.say_name] mention a girl named [gloryhole_girl.say_name]...)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "\"I'll be at the park in a few minutes [n.say_name]!\""

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "\"Can't wait for us to have some more fun together! <3\""

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(Well I'll be...)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "([n.say_name]'s got himself a girlfriend!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Seems like she's fond of him too)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(Bro must want to keep this under the radar, meeting her in the park at night)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(I'm real curious to see what kind of girl [n.say_name] has hooked up with!)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(I know where I'm going for my jog!)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(If [n.say_name] happens to spot me, I'll just say it's pure coincidence that I'm jogging around the same park)"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "(Yeah, pure coincidence...)"

    call fade_to_black(1)

    call process_new_location("bg park_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(Alright, where is he, where is he...)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(A-ha!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(I see [n.say_name]!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(He's over near one of the bathrooms)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(I've got a bead on you now bro!)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(No girlfriend in sight...{w=1.0}yet)"

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(I bet they meet up near the bathroom, since it's an obvious landmark)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(Further investigation is required!)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "([n.say_name]'s going into the bathroom)"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "(While he's in there, I'll keep watch for his girl...)"

    call fade_to_black(1)

    call process_new_location("bg park_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(How long is [n.say_name] going to be in there for?)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(Is he crapping his brains out or something?)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(And I haven't seen anyone around here since he first went in)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "(No other text messages from [gloryhole_girl.say_name] either...)"

    call process_character(k, appearance = "outfit clothes pose handhip face concerned blush false")
    k.c "...{p}..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(Finally, he's emerged!)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armsup face curious blush false")
    k.c "(Why does [n.say_name] look sweaty?)"

    call process_character(k, appearance = "outfit clothes pose handhip face curious blush false")
    k.c "(Only time he sweats that much is when he's...)"

    call process_character(k, appearance = "outfit clothes pose handhip face shocked blush false")
    k.c "!"

    call process_character(k, appearance = "outfit clothes pose handhip face shocked blush false")
    k.c "(Whoa, whoa, what the fuck?!)"

    call process_character(k, appearance = "outfit clothes pose armcross face shocked blush false")
    k.c "(A girl just came out of the same bathroom as [n.say_name]!)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "(And she's talking to him too...)"

    call process_character(k, appearance = "outfit clothes pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face embarrassed blush false")
    k.c "(Could that be...{w=1.0}[gloryhole_girl.say_name]?)"

    call process_character(k, appearance = "outfit clothes pose handhip face embarrassed blush false")
    k.c "(She appears to be sweating as well)"

    call process_character(k, appearance = "outfit clothes pose handhip face shocked blush false")
    k.c "(Was bro doing what I think he was doing in there with her?)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "...{p}..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(They're hugging)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "([n.say_name]'s grabbing a good amount of her ass too...{w=0.5}nice one bro)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "(There's no doubt in my mind that's Kacey)"

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(Looks like they're parting ways)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(I need to take a quick look inside that bathroom)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(If any dirty deed was done in there, I'll know pretty quick...)"

    call fade_to_black(1)

    call process_new_location("bg public_bathroom_evening", dream = dream)

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "(There is a strong, familiar odor in here)"

    call process_character(k, appearance = "outfit clothes pose armcross face happy blush false")
    k.c "(And it's not the usual smell associated with a bathroom)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(But I need more evidence...)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "...{p}..."

    call static_still_ctc("bg gloryhole")

    k.c "(Well, can't get more obvious than this...)"
    k.c "(A gloryhole!)"
    k.c "(Wow, look at the floor just below it!)"
    k.c "(Those are fresh cum stains)"
    k.c "(Some jizz strands are still sliding down the stall door)"
    k.c "(That's all I need to see!)"
    k.c "([n.say_name]'s been banging this [gloryhole_girl.say_name] girl!)"
    k.c "(And from the looks of things, it's been way more than once!)"
    k.c "..."
    k.c "(How did these two manage to meet each other?)"
    k.c "(And why hasn't [n.say_name] invited her over to our place yet?)"
    k.c "(She seems like a girl I'd want to get to know!)"
    k.c "..."
    k.c "(Wait a second...{w=1.0}[n.say_name]'s phone...)"
    k.c "([gloryhole_girl.say_name] would assume it's [n.say_name] who's texting her from this number)"
    k.c "..."
    k.c "(I think I'll set up a meet and greet with this [gloryhole_girl.say_name])"
    k.c "(Then I can learn more about all the juicy, sticky details between her and [n.say_name], hehe...)"

    call fade_to_black(1)

    call process_new_location("bg kitchen_daytime", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face aroused blush false")
    n.c "{i}Yawn.{/i}.."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "Late night, eh?"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "Yeah."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "You won't be able to stay up as late with school starting soon."

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "Unless your plan is to take naps during class!"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face concerned blush false")
    n.c "Can't believe summer's almost over..."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "There's still some time left."

    call process_character(k, appearance = "outfit clothes pose armsup face neutral blush false")
    k.c "You just have to make the most out of it!"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face neutral blush false")
    n.c "Yeah, I should..."

    call process_character(k, appearance = "outfit clothes pose handhip face neutral blush false")
    k.c "Personally, I want to get a few more beach days in!"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "Me too!"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "Why don't we go there today?"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "I'm hankering for another volleyball match!"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "Can we ask Grandma if she'd like to join us?"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "Sure."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "I doubt she'd turn down a beach invite."

    call fade_to_black(1)

    call process_new_location("bg beach_daytime", dream = dream)

    $ replace_position = True
    $ k.position = "right"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I'm happy you two were able to get to the beach today!"

    call process_character(n, appearance = "pose handfist face happy blush false")
    n.c "Yeah, we are too!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Won't be long before we'll need jackets if we want to be out here."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Fall is fast approaching."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face concerned blush false")
    n.c "And so is school..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face curious blush false mouth red")
    edna.c "Is it really that close to school starting up for you again [n.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Feels like summer just started a few days ago!"


    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(k, appearance = "outfit bikini pose armcross face concerned blush false")
    k.c "Worst part is how long the wait is for the next summer to arrive."

    call process_character(k, appearance = "outfit bikini pose armcross face concerned blush false")
    k.c "Winter drags on for too long."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I know exactly how you feel [k.say_name]!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face embarrassed blush false mouth red")
    edna.c "My joints do not appreciate the cold weather!"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Well, before those cold fronts start rolling in, I'm gonna crush it at volleyball some more!"


    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "[n.say_name], you want to pair up so we can dominate?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "Hmm..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Can [n.say_name] join you a little later [k.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I want to talk with him about what's going to be happening at his new school, and what he'll be learning!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "That's fine Grandma."

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "While I wait, I'll help tilt a team that needs an extra player!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Go get em granddaughter!"

    call character_leave_dissolve(k)
    pause 0.5

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Once you're back in school, I won't get to see you as often."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "You'll be busy studying, taking tests..."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face concerned blush false")
    n.c "And writing papers..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "[k.say_name] will be occupied for a while."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face flirt blush false mouth red")
    edna.c "Did you want to head up to my condo?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face flirt blush false mouth red")
    edna.c "There are certain things we can do while we're up there..."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face neutral blush false")
    n.c "There sure is Grandma..."


    call fade_to_black(1)

    call process_new_location("bg beach_daytime", dream = dream)

    call process_character(k, appearance = "outfit bikini pose armcross face angry blush false")
    k.c "I don't think I've played with a shittier team before!"

    call process_character(k, appearance = "outfit bikini pose armcross face angry blush false")
    k.c "They could hardly hit the ball over the net!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "[n.say_name], you and I would wipe the floor against them!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Let's go back over there, and show them who are the masters of..."

    call process_character(k, appearance = "outfit bikini pose armsup face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Where'd [n.say_name] and Grandma go?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Their stuff is still here)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "(I bet they're making some sandwiches back at the condo)"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "(I need to grab some extra water bottles, so I'll head back up there real quick)"

    call fade_to_black(1)

    call process_new_location("bg edna_house_daytime", dream = dream)

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Damn, did I just miss them?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Nah, I couldn't have)"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "(I would have spotted them in the hallway or the lobby)"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "(There's no sandwiches or anything on the kitchen counter)"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "(What did they come back here for then?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "(Did [n.say_name] get stung by a jellyfish or something?)"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Oh, there they are!)"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(They're out on the balcony)"

    call process_character(k, appearance = "outfit bikini pose armsup face curious blush false")
    k.c "(Wait...{w=1.0}are they naked out there?)"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "{cps=40}(And why is Grandma kneeling down-){/cps}{w=0.75}{nw}"

    call process_character(k, appearance = "outfit bikini pose armcross face shocked blush false")
    k.c "!!"

    $ set_main_animation_speed(1.0)
    $ edna_titfuck_had_slow_speed_message = False
    $ edna_titfuck_had_normal_speed_message = False
    $ edna_titfuck_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image at main_animation_transform(IA_Animation_Edna_Titfuck_Nude_Info()) as main_animation
    with Dissolve(1.15)
    show bg white

    pause
    $ quick_menu = True
    $ no_bust_art = True

    k.c "(What the fucking shit?!)"
    k.c "(Am I suffering from heat stroke hallucinations?!)"
    k.c "..."
    k.c "(This...{w=1.0}this is real right now)"
    k.c "(Grandma and [n.say_name]...)"
    k.c "(Grandma...{w=1.0}and [n.say_name]!)"
    k.c "(Even for me, I can't wrap my head around this!)"
    k.c "..."
    k.c "(Although...{w=1.0}I recall Grandma acting a bit flirty towards [n.say_name] recently)"
    k.c "(But I thought she was just having fun!)"
    k.c "(I didn't think she wanted some real hardcore action with bro's dick!)"
    k.c "(I figured she was past that point at her age)"
    k.c "(I got that wrong!)"


    window hide
    call edna_titfuck_set_speed(edna_titfuck_fastest_speed_multiplier)
    pause
    window auto
    k.c "(Grandma is having a ball!)"
    k.c "(She's been smiling the whole time [n.say_name] has had his dick between her tits!)"
    k.c "(And [n.say_name] is showing no signs of hesitation!)"
    k.c "(Gone is the nervous and reluctant brother staring at my ass!)"
    k.c "(Now he's a verified mother, and grandmother fucker!)"
    n.c "Oh, oh yeah..."
    n.c "Here I come Grandma!"
    k.c "..."

    $ quick_menu = False
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    pause 0.5

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ quick_menu = False
    window hide
    show bg edna_nude_titfuck_cumshot_surprise
    with Dissolve(1.5)

    pause
    $ quick_menu = True
    n.c "Hnngaa!"
    k.c "(Damn, what a fat nut!)"

    call static_still_ctc("bg edna_nude_titfuck_aftercum_smile")
    k.c "([n.say_name] just blasted Grandma's tits with cum!)"
    k.c "(He spurted like a fountain!)"
    k.c "(And look at the wide grin on Grandma!)"
    k.c "(I don't think I've seen anybody show that much glee about a titty fuck...{w=0.5}other than me!)"
    edna.c "Feel better [n.say_name]?"
    edna.c "Now you'll be set for playing volleyball with your big sister!"
    n.c "Yeah, I will Grandma!"
    edna.c "Let's head back down to the beach."
    edna.c "[k.say_name] is probably wondering where we are right now."
    k.c "(Shit, I have to get out of here!)"
    k.c "(I'll just play it cool for the remainder of the day)"

    call fade_to_black(1)

    $ renpy.stop_predict("edna_titfuck_nude_anim")
    call process_new_location(bg = "bg edna_house_evening", dream = dream)

    $ k.position = "right"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "That was one of the longest times I've stayed at the beach in one day!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "But the temperature was too perfect to waste!"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "I think that was the best beach day yet Grandma!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I think it was too!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "It wasn't crowded, the waves were rolling in smooth..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face happy blush false mouth red")
    edna.c "And you and [k.say_name] went undefeated together in volleyball!"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Thanks to my trusty spike I like to call, deep impact!"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "I got sand all down my suit from playing."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "All those diving saves I made put plenty of the beach up my ass crack."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Use the shower to clean yourself up."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "After being on the beach for that long, you do start to get a bit grimy."


    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "You go in first bro."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "I'll chat with Grandma while I wait."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "That's nice of you [k.say_name]."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Don't hog all the hot water though!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "I won't."

    call character_leave_dissolve(n)
    pause 0.5

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "...{p}..."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I know you saw me on the balcony with [n.say_name], [k.say_name]."

    call process_character(k, appearance = "outfit bikini pose armcross face embarrassed blush false")
    k.c "!"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I caught your bright green bikini out of the corner of my eye."

    call process_character(k, appearance = "outfit bikini pose armcross face embarrassed blush false")
    k.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "You were going to ask me about it, I could tell."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "So I'm admitting to you now that yes, I do have sex with [n.say_name]."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "You're being surprisingly chill about telling me all of this Grandma."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Well, your reaction to it is rather subdued."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face curious blush false mouth red")
    edna.c "Isn't that unusual as well?"

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face curious blush false")
    k.c "What does my reaction have to do with this?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "You've also had sexual experiences with [n.say_name]."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "It started this summer."

    call process_character(k, appearance = "outfit bikini pose armsup face embarrassed blush false")
    k.c "Huh?!"

    call process_character(k, appearance = "outfit bikini pose armsup face embarrassed blush false")
    k.c "How do you..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "How do I know?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "[n.say_name] loves talking about you."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "He tells me you give great titfucks to him back at home."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face curious blush false mouth red")
    edna.c "And you both practice these...{w=0.5}kamasutra positions with each other?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face happy blush false mouth red")
    edna.c "They're out of my range of flexibility!"

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face curious blush false")
    k.c "So [n.say_name]'s just been blabbering all of this to you?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "Now don't get mad at [n.say_name], [k.say_name]."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "He only tells me these things because he knows I support it."

    call process_character(k, appearance = "outfit bikini pose armcross face embarrassed blush false")
    k.c "You support [n.say_name] and I fucking Grandma?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Of course I do!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I think it's great!"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "I...{w=1.0}didn't know you were so enthusiastic about it."


    if "family_foursome_scene" in scenes_completed or finale_julia_sam:
        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "[n.say_name] couldn't stop talking about the foursome he had with you, [sa.say_name], and [si.say_name] the other day!"

        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "I wish I could have been there to see it!"

    else:
        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "[n.say_name] couldn't stop talking about the threesome he had with you and [si.say_name] the other day!"

        call process_character(edna, appearance = "pose handclasp face happy blush false")
        edna.c "I wish I could have been there to see it!"


    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Are you like...{w=1.0}a nymphomaniac Grandma?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "Haha!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "At one point in time, that would have been a very accurate word to associate with me!"

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "So now you're just a nympho?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Very funny [k.say_name]!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Man, [n.say_name] has been getting around this summer!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "He's using that free time he has effectively!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "It's why I wanted to be with him today."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "School will be squeezing his schedule."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "He already occupies most of his time rotating among all of us!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "One day it may be me, next day it may be [si.say_name], then [janet.say_name], then..."

    call process_character(k, appearance = "outfit bikini pose armcross face shocked blush false")
    k.c "Wait, what?"

    call process_character(k, appearance = "outfit bikini pose armcross face shocked blush false")
    k.c "Aunt [janet.say_name]?!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face curious blush false mouth red")
    edna.c "You didn't know about [janet.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Yes, she's been active with [n.say_name] as well."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I've spotted them a couple times, fucking on the beach."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "It's very clever how they hide between the lounge chairs!"

    if finale_julia_sam:
        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "He's practically banging the entire family!"

        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "I don't know how [julia.say_name] hasn't found out about this yet."

        call process_character(edna, appearance = "pose handclasp face neutral blush false")
        edna.c "Mm...{w=1.0}well..."

        call process_character(k, appearance = "pose armcross face shocked blush false")
        k.c "..."

        call process_character(k, appearance = "pose armcross face shocked blush false")
        k.c "You've got to be shitting me."

        call process_character(edna, appearance = "pose handclasp face neutral blush false")
        edna.c "He's fucking [julia.say_name] too."

    else:
        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "..."

        call process_character(k, appearance = "pose armsup face embarrassed blush false")
        k.c "You've got to be shitting me."

    call process_character(k, appearance = "outfit bikini pose handhip face embarrassed blush false")
    k.c "How is that even possible for [n.say_name] to accomplish?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I don't know, but [n.say_name] makes it work."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I think it helps that everyone is in close proximity."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Did he also tell you about [gloryhole_girl.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face curious blush false mouth red")
    edna.c "[gloryhole_girl.say_name]?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "[gloryhole_girl.say_name]...{w=0.5}[gloryhole_girl.say_name]..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Yeah."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Bro's been having a big fling with her at the local park."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "I learned about his involvement with her purely by accident."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "I did not know about that."

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "So [n.say_name] has had sexual adventures outside the family as well."

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "[n.say_name] literally has a girl for every day of the week."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "A full itinerary!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "It's just constant sex for him."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Bro's not just a sex addict...{w=1.0}he's a sex maniac!"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "I don't know how much longer [n.say_name] will be able to keep this under wraps."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "My feeling is each girl will eventually learn everything we currently know."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "I think you're spot on Grandma."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Sooner or later, it will all come bursting out."

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Just like what [n.say_name] did earlier today, bursting on your tits!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Haha!"

    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false")
    n.c "Okay, I'm done in the shower."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "..."

    call process_character(n, appearance = "outfit underwear pose behindhead face neutral blush false")
    n.c "What were you two laughing about?"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face neutral blush false mouth red")
    edna.c "Oh, we were just laughing about..."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "How I bonked that one dude off the head with one of my spikes!"

    call process_character(edna, appearance = "outfit swimsuit pose fisthip face happy blush false mouth red")
    edna.c "Yes!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "Oh yeah!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "That was hilarious!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "He spun around after he got hit!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face neutral blush false mouth red")
    edna.c "..."


    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "My turn for the shower."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Grandma, we'll talk again later."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "There's a lot we need to catch up on..."

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    edna.c "I can't wait [k.say_name]!"

    call process_character(n, appearance = "outfit underwear pose handsdown face neutral blush false")
    n.c "..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Now, [n.say_name]..."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face neutral blush false mouth red")
    edna.c "Would you like to help me prepare a meal in the kitchen?"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "I've got a recipe for sweet and sour meatballs that I know you'll love!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "That sounds insanely good Grandma!"

    call process_character(n, appearance = "outfit underwear pose twohandfist face happy blush false")
    n.c "Yeah, I want to help make it!"

    call fade_to_black(1)

    call process_new_location(bg = "bg kira_room_daytime", dream = dream)

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(So this is how far you've come bro)"

    call process_character(k, appearance = "outfit clothes pose armcross face neutral blush false")
    k.c "(One day you're wedging your dick between my butt cheeks, eager to see what it feels like...)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(And the next, your dick is going into the pussy of every girl you meet!)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "(Quite a drastic leap)"

    call process_character(k, appearance = "outfit clothes pose armsup face happy blush false")
    k.c "..."

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(Imagine the number of fuck buddies he'll make at school!)"

    call process_character(k, appearance = "outfit clothes pose handhip face happy blush false")
    k.c "(It will be like a small army!)"


    "{i}Ding!{/i}"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "(Who'd I get a text from?)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "(The number isn't familiar)"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose handhip face curious blush false")
    k.c "([vicky.say_name]?)"

    call process_character(k, appearance = "pose handhip face curious blush false")
    k.c "(No idea who this is)"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "(Yikes, she sent me a wall of text!)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "(Let's see here...)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "\"Greetings [k.say_name] [last_name].\""

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "\"My name is [vicky.say_name], and I run an adult video production company, [vicky.say_name]'s Empornium\""

    call process_character(k, appearance = "pose armcross face happy blush false")
    k.c "(Empornium...{w=1.0}clever)"

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "(But why am I being contacted by someone like that?)"

    call process_character(k, appearance = "pose armcross face curious blush false")
    k.c "..."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "\"I was referred to you by your brother, [n.say_name] [last_name]\""

    call process_character(k, appearance = "pose handhip face shocked blush false")
    k.c "(What?)"

    call process_character(k, appearance = "pose handhip face shocked blush false")
    k.c "(An owner of a porn company knows [n.say_name]?)"

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "(And he referred me?)"

    call process_character(k, appearance = "pose armcross face embarrassed blush false")
    k.c "(This has to be a joke...)"

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "\"I would very much like to arrange a meeting with you\""

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "\"There is a great opportunity for you that we can discuss!\""

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "\"If you're interested, please respond to this text\""

    call process_character(k, appearance = "pose armcross face neutral blush false")
    k.c "\"I look forward to hearing from you\""

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "(Great opportunity?)"

    call process_character(k, appearance = "pose handhip face embarrassed blush false")
    k.c "(What crazy scheme did [n.say_name] get himself into?)"

    call process_character(k, appearance = "pose handhip face happy blush false")
    k.c "(Still...{w=1.0}my curiosity is through the roof right now!)"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "(I want to know if this chick is legit or not...)"

    call process_character(k, appearance = "pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "\"Hey Vicky\""

    call process_character(k, appearance = "pose armsup face neutral blush false")
    k.c "\"Where are you at, and what times are you available?\""

    call fade_to_black(1)

    show bg vicky_sit_smile
    with Dissolve(0.5)

    k.c "You're [vicky.say_name], I presume?"
    vicky.c "And you must be [k.say_name]!"
    vicky.c "I finally get to meet [n.say_name]'s big sister in the flesh!"
    k.c "Yeah so...{w=1.0}how did my little brother come to know you anyway?"
    k.c "I can't imagine he encountered a porn company owner by accident."

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    vicky.c "I previously worked as an affiliate for ReflexViz.HD."
    vicky.c "Are you familiar with the company?"
    k.c "That's the streaming thing online, right?"
    k.c "[n.say_name] and [sa.say_name] couldn't stop talking about it at the beginning of the summer."
    k.c "They were making a show or something called Twinsticks."
    vicky.c "That's right."
    vicky.c "I contacted [n.say_name] after he and his sister [sa.say_name] began building a sizable audience."
    vicky.c "Their channel had a lot of potential, and so I met with [n.say_name] to help maximize his growth."
    k.c "So [n.say_name] & [sa.say_name] must have been rocking it with their stream to be contacted by someone like you."


    show bg vicky_sit_smile
    with Dissolve(0.5)
    vicky.c "They're well on their way to becoming one of the top channels on the ReflexViz.HD platform!"
    k.c "So, where then does the whole porn thing come into play?"
    vicky.c "I found that [n.say_name] had a rather...{w=1.0}special talent when it came to adult content."
    vicky.c "Right from our first meeting, it was clear to me that [n.say_name] had all the makings of the next great porn star."
    k.c "Porn star?!"
    k.c "My little bro [n.say_name], a porn star?"
    k.c "Hahaha!"
    vicky.c "I can attest to [n.say_name]'s impressive capabilities."
    vicky.c "He never fails to deliver!"
    k.c "..."
    k.c "Are you trying to tell me that...{w=1.0}you and [n.say_name]..."
    vicky.c "This very office has been the sight of more than a few of our...{w=1.0}sessions."
    k.c "(I thought I smelled the faint scent of cum in here...)"
    vicky.c "Soon after, I established [vicky.say_name]'s Empornium, with [n.say_name] playing a pivotal role in production."
    k.c "A pivotal role, huh?"
    vicky.c "Have you seen our videos yet?"
    k.c "You and [n.say_name] made a video?!"
    vicky.c "Several at this point."
    vicky.c "It's content exclusive to the [vicky.say_name]'s Empornium website."

    show bg vicky_sit_turn
    with Dissolve(0.5)

    vicky.c "Here, let me pull up one of our recent ones for you."
    k.c "..."
    k.c "Holy shit, there's [n.say_name]!"
    k.c "And that's you!"
    vicky.c "Indeed it is."
    k.c "Nice camera work there."
    k.c "I see you let him go up your back passage, hehe."
    k.c "I approve."
    vicky.c "We try to do every possible scenario we can."
    k.c "([n.say_name]'s turned fucking into a profession!)"
    k.c "(He's literally making dough by having his dick do the work!)"


    show bg vicky_sit_smile
    with Dissolve(0.5)
    vicky.c "So, what do you think?"
    k.c "I think...{w=1.0}[n.say_name] is one lucky bastard."
    k.c "I wish I was doing the same thing."
    vicky.c "Then you'll want to hear my offer [k.say_name]."
    k.c "..."
    k.c "Go on."
    vicky.c "I'd like you to be the main adult actress that works with [n.say_name]."
    vicky.c "You could have your own dedicated series!"
    vicky.c "And, you'll get to keep seventy percent of the royalties from sales and subscriptions."
    k.c "Hmm!"
    k.c "I'm liking the sound of that!"
    k.c "If it becomes successful, I won't have to work at the fitness center anymore!"
    vicky.c "I'm certain it will be successful."
    vicky.c "The market is ripe for this sort of content right now."


    show bg vicky_sit_neutral
    with Dissolve(0.5)
    vicky.c "But you don't have to rush your decision."
    vicky.c "I want to make sure you feel certain about it."
    vicky.c "Before you leave today, I'll give you some documents and outlines as to what would be expected of you."
    vicky.c "Read it over carefully, and let me know what you think."

    show bg vicky_sit_smile
    with Dissolve(0.5)

    vicky.c "I'm open to revisions and negotiations, so all of what you read is subject to change."
    k.c "I don't think it will take me that long to make a decision!"
    vicky.c "That's great to hear you have enthusiasm for the offer!"
    vicky.c "I'm glad you were able to stop by and talk to me today!"
    k.c "Hey, thank you for dropping this once in a lifetime opportunity in my lap!"
    vicky.c "No need to thank me."
    vicky.c "It was your brother [n.say_name] that informed me about you, after all."
    vicky.c "He's the one you should be thanking."
    k.c "Oh trust me, I will..."
    vicky.c "You have my contact information and business card, so give me a buzz whenever you'd like to talk."
    k.c "Sounds good [vicky.say_name]!"

    call fade_to_black(1)

    call process_new_location(bg = "bg backyard_daytime", dream = dream)

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Imagine...{w=0.5}me being a porn star with [n.say_name])"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "(My favorite pastime of fucking can now be a career!)"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "(I'll have to come up with a good porn star name)"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "(I wonder if [n.say_name] has one yet...)"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "(Bro is the only person I've known where thinking with his dick turned out to be a good thing!)"

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "(Now he has a whole line-up of girls willing to go down on him)"

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Imagine if every girl [n.say_name] had been with gathered together in one spot?)"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(It would be chaos...{w=1.0}for [n.say_name]!)"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "(Talk about too much of a good thing!)"

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "(Would his cock and balls even survive such an ordeal?)"

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Hmm..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Hehe..."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "(Given the way this summer has been for [n.say_name], it would only be fitting if it went out with a huge bang)"

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "(A gangbang that is...)"

    call fade_to_black(1)

    "{i}Several days later...{/i}"

    call process_new_location(bg = "bg nate_room_daytime", dream = dream)

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "(Not much longer until school starts...)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Wish I could time travel and go through the summer again)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face concerned blush false")
    n.c "{i}Sigh.{/i}.."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "(Well, like [k.say_name] said, I need to make the most of my remaining summer vacation)"

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "Hm?"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(I hear a lot of talking outside at the pool)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "(Did Mom invite company over?)"

    call process_character(n, appearance = "outfit clothesjacket pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face neutral blush false")
    n.c "(It is pretty warm out today)"

    call process_character(n, appearance = "outfit clothesjacket pose handfist face neutral blush false")
    n.c "(I think a swim in the pool is in order!)"

    call character_leave_dissolve(n)

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "(I'm ready for a cannonball!)"

    call fade_to_black(1)

    call process_new_location(bg = "bg backyard_daytime", dream = dream)

    call process_character(n, appearance = "outfit swimsuit pose handsdown face neutral blush false")
    n.c "..."

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose armunder face happy blush false")
        si.c "There he is!"
    else:
        call process_character(si, appearance = "outfit clothes pose armunder face happy blush false")
        si.c "There he is!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Bout time bro!"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Everyone's been waiting for you."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "What do you mean everyone?"

    if finale_julia_sam and "sam_scene_swimsuit" in store.scenes_completed:
        call process_character(sa, appearance = "outfit swimsuit pose leaning face neutral blush false")
        sa.c "Just look at who's here [n.say_name]!"
    else:
        call process_character(sa, appearance = "outfit clothes pose leaning face neutral blush false")
        sa.c "Just look at who's here [n.say_name]!"

    call process_character(janet, appearance = "outfit swimsuit pose handhips face neutral blush false")
    janet.c "I love this pool [n.say_name]!"

    call process_character(janet, appearance = "outfit swimsuit pose handhips face neutral blush false")
    janet.c "It's perfect for hosting a party like this!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
    n.c "Aunt [janet.say_name]!"

    if finale_julia_sam and "julia_scene_swimsuit" in store.scenes_completed:
        call process_character(julia, appearance = "outfit swimsuit pose armcross face concerned blush false")
        julia.c "..."

        call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
        n.c "Hey [julia.say_name]!"

        call process_character(n, appearance = "outfit swimsuit pose handfist face happy blush false")
        n.c "Oh, you're wearing the swimsuit I got you!"

        call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
        julia.c "..."

        call process_character(julia, appearance = "outfit swimsuit pose handup face neutral blush false")
        julia.c "Yeah..."

        call process_character(janet, appearance = "outfit swimsuit pose handface face happy blush false")
        janet.c "Ah, ha!"

        call process_character(janet, appearance = "outfit swimsuit pose handface face happy blush false")
        janet.c "So it was you who got her that, [n.say_name]!"

        call process_character(janet, appearance = "outfit swimsuit pose handchest face neutral blush false")
        janet.c "This is the first time in a long time that I've seen her wear a swimsuit."

        call process_character(janet, appearance = "outfit swimsuit pose handchest face happy blush false")
        janet.c "I guess I have you to thank for that!"

        call process_character(julia, appearance = "outfit swimsuit pose handup face concerned blush false")
        julia.c "..."

        call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
        n.c "Um, is everything okay, [julia.say_name]?"

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handface face neutral blush false")
            sa.c "She's fine!"
        else:
            call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
            sa.c "She's fine!"

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face neutral blush false")
            sa.c "She's just a little embarrassed about wearing her swimsuit in front of everybody, I think."
        else:
            call process_character(sa, appearance = "outfit clothes pose handsbehind face neutral blush false")
            sa.c "She's just a little embarrassed about wearing her swimsuit in front of everybody, I think."

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face neutral blush false")
            sa.c "But I'm helping her ease into it!"

            call process_character(julia, appearance = "outfit swimsuit pose armcross face embarrassed blush false")
            julia.c "Yes, she's very... {w=0.5}persistent about it."

            call process_character(sa, appearance = "outfit swimsuit pose leaning face neutral blush false")
            sa.c "I gave her some inspiring words of encouragement earlier too."

            call process_character(sa, appearance = "outfit swimsuit pose leaning face happy blush false")
            sa.c "Everybody gets to wear a swimsuit today!"

        else:
            call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
            sa.c "Oh man, I wish I had a swimsuit too!"

            call process_character(sa, appearance = "outfit clothes pose handface face neutral blush false")
            sa.c "Maybe I could get one just like yours, [julia.say_name]!"

            call process_character(sa, appearance = "outfit clothes pose leaning face happy blush false")
            sa.c "Then we could have matching swimsuits!"

        call process_character(janet, appearance = "outfit swimsuit pose handchest face neutral blush false")
        janet.c "I know you're no fan of swimming, [julia.say_name], but it suits you very well!"

#        call process_character(n, appearance = "outfit swimsuit pose handfist face neutral blush false")
#        n.c "Yeah!"

        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face happy blush false")
            sa.c "Mhm!"

            call process_character(sa, appearance = "outfit swimsuit pose handsbehind face happy blush false")
            sa.c "You look really cute in that swimsuit!"
        else:
            call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false")
            sa.c "Mhm!"

            call process_character(sa, appearance = "outfit clothes pose handsbehind face happy blush false")
            sa.c "You look really cute in that swimsuit!"

        call process_character(julia, appearance = "outfit swimsuit pose armcross face embarrassed blush true")
        julia.c "(Cute?)"

        call process_character(julia, appearance = "outfit swimsuit pose armcross face embarrassed blush true")
        julia.c "T-thanks..."

    elif finale_julia_sam and "julia_scene_swimsuit" not in store.scenes_completed:
        call process_character(julia, appearance = "outfit clothes pose armcross face neutral blush false")
        julia.c "I don't have a suit to put on for swimming, not that I would anyway."

        call process_character(julia, appearance = "outfit clothes pose armcross face happy blush false")
        julia.c "But, I like dipping my feet into the hot tub."

        call process_character(n, appearance = "pose handfist face neutral blush false")
        n.c "Hey [julia.say_name]!"

        call process_character(julia, appearance = "outfit clothes pose handup face happy blush false")
        julia.c "Hey."

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Help yourself to the snacks [n.say_name]!"

    call process_character(edna, appearance = "outfit swimsuit pose handclasp face happy blush false mouth red")
    edna.c "Try out the chips and dip!"

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face happy blush false")
    n.c "You're here too Grandma?!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsup face neutral blush false")
        si.c "This was all [k.say_name]'s planning!"
    else:
        call process_character(si, appearance = "outfit clothes pose handsup face neutral blush false")
        si.c "This was all [k.say_name]'s planning!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsup face happy blush false")
        si.c "She said we should have an end of summer get together, and I very much agreed with the idea!"
    else:
        call process_character(si, appearance = "outfit clothes pose handsup face happy blush false")
        si.c "She said we should have an end of summer get together, and I very much agreed with the idea!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "It wasn't easy working around the schedules."

    call process_character(k, appearance = "outfit bikini pose handhip face happy blush false")
    k.c "But I wasn't going to give up!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
    n.c "I'm glad you didn't [k.say_name]!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face happy blush false")
    n.c "This is so cool having everybody here!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Well, it's not quite everyone yet."

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "There's still two more guests yet to arrive."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "Really?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face neutral blush false")
    n.c "More?"

    call process_character(k, appearance = "outfit bikini pose armsup face neutral blush false")
    k.c "Yes..."

    call process_character(k, appearance = "outfit bikini pose armsup face happy blush false")
    k.c "Your park friend [gloryhole_girl.say_name], and business partner [vicky.say_name]."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face embarrassed blush false")
    n.c "[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name] and [vicky.say_name] are coming?!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsfront face neutral blush false")
        si.c "You should have told us about them earlier sweetie!"
    else:
        call process_character(si, appearance = "outfit clothes pose handsfront face neutral blush false")
        si.c "You should have told us about them earlier sweetie!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose handsfront face neutral blush false")
        si.c "They both sound like lovely girls, based on what [k.say_name] told me."
    else:
        call process_character(si, appearance = "outfit clothes pose handsfront face neutral blush false")
        si.c "They both sound like lovely girls, based on what [k.say_name] told me."

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose armunder face happy blush false")
        si.c "I would have invited them over for supper!"
    else:
        call process_character(si, appearance = "outfit clothes pose armunder face happy blush false")
        si.c "I would have invited them over for supper!"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "H-How did you learn about..."

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Attention everyone!"

    call process_character(k, appearance = "outfit bikini pose handhip face neutral blush false")
    k.c "Attention!"

    call process_character(n, appearance = "outfit swimsuit pose handsdown face concerned blush false")
    n.c "..."

    call process_character(k, appearance = "outfit bikini pose armcross face neutral blush false")
    k.c "Now that [n.say_name] is finally here...{w=1.0}it's about time we revealed to him what this party is really about."

    call process_character(k, appearance = "outfit bikini pose armcross face happy blush false")
    k.c "Each of you should know exactly what I mean, based on what was discussed previously."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "What was discussed?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face curious blush false")
    n.c "I don't think you talked to me about it..."

    call character_leave_dissolve(k)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
    pause 0.5

    call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
    k.c "..."

    call process_character(n, appearance = "outfit swimsuit pose twohandfist face embarrassed blush false")
    n.c "!!"

    if "simone_scene_swimsuit" in store.scenes_completed:
        call process_character(si, appearance = "outfit swimsuit pose armunder face flirt blush false")
    else:
        call process_character(si, appearance = "outfit clothes pose armunder face flirt blush false")

    pause 0.5
    call character_leave_dissolve(si)
    pause 0.5
    call process_character(si, appearance = "outfit nude pose armunder face flirt blush false")
    pause 0.5

    call process_character(si, appearance = "outfit nude pose armunder face flirt blush false")
    si.c "..."

    call process_character(n, appearance = "outfit swimsuit pose handsdown face embarrassed blush true")
    n.c "(H-Huh?!)"

    if finale_julia_sam:
        if "sam_scene_swimsuit" in store.scenes_completed:
            call process_character(sa, appearance = "outfit swimsuit pose handface face happy blush false")
        else:
            call process_character(sa, appearance = "outfit clothes pose handface face happy blush false")
        pause 0.5
        call character_leave_dissolve(sa)
        pause 0.5
        call process_character(sa, appearance = "outfit nude pose handface face happy blush false")
        pause 0.5

        call process_character(sa, appearance = "outfit nude pose handface face happy blush false")
        sa.c "Aw yeah, it begins!"

        if "julia_scene_swimsuit" in store.scenes_completed:
            call process_character(julia, appearance = "outfit swimsuit pose handup face aroused blush false")
        else:
            call process_character(julia, appearance = "outfit clothes pose handup face aroused blush false")
        pause 0.5
        call character_leave_dissolve(julia)
        pause 0.5
        call process_character(julia, appearance = "outfit nude pose handup face aroused blush false")
        pause 0.5
        call process_character(julia, appearance = "outfit nude pose handup face aroused blush false")
        julia.c "..."

    call process_character(janet, appearance = "outfit swimsuit pose handface face neutral blush false")
    pause 0.5
    call character_leave_dissolve(janet)
    pause 0.5
    call process_character(janet, appearance = "outfit nude pose handface face neutral blush false")
    pause 0.5

    call process_character(janet, appearance = "outfit nude pose handface face neutral blush false")
    janet.c "Your face is bright red [n.say_name]!"

    call process_character(janet, appearance = "outfit nude pose handface face happy blush false")
    janet.c "Are there too many cute girls around you?"

    call process_character(edna, appearance = "outfit swimsuit pose handhip face happy blush false mouth red")
    pause 0.5
    call character_leave_dissolve(edna)
    pause 0.5
    call process_character(edna, appearance = "outfit nude pose handhip face happy blush false mouth red")
    pause 0.5

    call process_character(edna, appearance = "outfit nude pose handhip face happy blush false mouth red")
    edna.c "There's a lot to look at, isn't there [n.say_name]?"

    call process_character(n, appearance = "outfit swimsuit pose behindhead face embarrassed blush true")
    n.c "(T-They're all naked...)"

    call process_character(n, appearance = "outfit swimsuit_hard pose behindhead face aroused blush true")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit_hard pose twohandfist face aroused blush true")
    n.c "(My whole family is naked in front of me!)"

    call process_character(k, appearance = "outfit nude pose handhip face flirt blush false")
    k.c "Are you connecting the dots in your head yet bro?"

    call process_character(k, appearance = "outfit nude pose handhip face flirt blush false")
    k.c "Your other head has figured it out already!"

    call process_character(n, appearance = "outfit swimsuit_hard pose handsdown face aroused blush true")
    n.c "..."

    call process_character(n, appearance = "outfit swimsuit_hard pose handsdown face aroused blush true")
    n.c "(What's going to happen with everyone here?)"

    call process_character(k, appearance = "outfit nude pose armsup face happy blush false")
    k.c "Quit ogling the tits and ass [n.say_name], and get that suit off!"

    call process_character(n, appearance = "outfit nudehard pose twohandfist face aroused blush true", show_bust = False)
    $ refresh_character(n, force_transition = Dissolve(1.0))
    call process_character(n, appearance = "outfit nudehard pose twohandfist face aroused blush true")
    n.c "Ah!"

    call process_character(k, appearance = "pose armcross face flirt blush false")
    k.c "Alright, who wants first dibs?"

    if finale_julia_sam:
        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "Me, me, me!"

        call process_character(sa, appearance = "pose leaning face neutral blush false")
        sa.c "I want first dibs!"

    call process_character(edna, appearance = "pose handclasp face happy blush false")
    edna.c "Is seniority factored in to who goes first?"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "What about if you're head of the household?"

    call process_character(si, appearance = "pose handsup face happy blush false")
    si.c "Haha!"

    call process_character(janet, appearance = "pose handface face happy blush false")
    janet.c "Shall we draw straws?"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "W-Wait!"

    call process_character(n, appearance = "pose behindhead face embarrassed blush true")
    n.c "Do I get a say in this?"

    call process_character(k, appearance = "pose handhip face happy blush false")
    k.c "You want to choose yourself bro?"

    call process_character(k, appearance = "pose handhip face flirt blush false")
    k.c "I should have known, since you like to do that."

    call process_character(n, appearance = "pose behindhead face curious blush true")

    call process_character(edna, appearance = "pose handhip face neutral blush false")
    edna.c "That's fine with me."

    call process_character(edna, appearance = "pose handhip face happy blush false")
    edna.c "As long as I get my time in with my grandson!"

    if finale_julia_sam:
        call process_character(sa, appearance = "pose handsbehind face neutral blush false")
        sa.c "Same!"

    call process_character(janet, appearance = "pose handchest face neutral blush false")
    janet.c "Whatever's easiest!"

    if finale_julia_sam:
        call process_character(julia, appearance = "pose handface face neutral blush false")
        julia.c "I don't care, either way."

    call process_character(si, appearance = "pose armunder face flirt blush false")
    si.c "Seems like there's a general agreement that you'll make the choice sweetie!"

    call process_character(k, appearance = "pose armsup face flirt blush false")
    k.c "Okay bro, you got a lot of options."

    call process_character(k, appearance = "pose armsup face flirt blush false")
    k.c "Hope you can pace yourself!"

    call process_character(n, appearance = "pose handsdown face curious blush true")
    n.c "..."

    call finale_scene_choices_impreg_override(dream = dream)

    return
