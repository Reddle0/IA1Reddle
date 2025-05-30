init offset = 101

default persistent.see_incomplete_leftovers = False
default persistent.bonus_leftovers_enabled = False
default persistent.menu_zoom_enabled = False

init 200:
    screen choice_leftovers(items):
        style_prefix "choice"

        frame:
            background None
            yalign 0.55
            xalign 0.5
            side "c r":
                area 0, 0, 1280, 720
                viewport id "choice_screen":
                    mousewheel persistent.mouse_wheel_choice_scroll

        vbox:
            xfill True
            spacing 0

            for i in items:
                textbutton i.caption action i.action xalign 0.5 at anim_choice_button

        vbar value YScrollValue('choice_screen') unscrollable "hide" xsize 36

    transform anim_choice_button:
        on hover:
            xalign 0.5
            linear 0.25 zoom 1.25
        on idle:
            xalign 0.5
            linear 0.25 zoom 1.0

init 100 python:
    leftovers_old_nate_room_choices = nate_room_empty_choices

    def leftovers_nate_room_choices():
        choice_list = leftovers_old_nate_room_choices()

        choice_list.append( ("(LEFTOVERS) Mod Options", "leftovers_mod_options") )

        if persistent.bonus_leftovers_enabled:
        # add bonus scene list button to Nate's bedroom
            choice_list.append( ("(LEFTOVERS) Bonus Scenes", "leftovers_bonus_scene_list") )
        else:
            if ("(LEFTOVERS) Bonus Scenes", "leftovers_bonus_scene_list") in choice_list:
                choice_list.remove( ("(LEFTOVERS) Bonus Scenes", "leftovers_bonus_scene_list") )

    # Ensuring the (Back) is at the bottom
        if ("Back", "back") in choice_list:
            choice_list.remove( ("Back", "back") )

            choice_list.append( ("Back", "back") )

        return choice_list

    nate_room_empty_choices = leftovers_nate_room_choices

label leftovers_mod_options:
    menu:
        "Enable Incomplete Mod Content" if not persistent.see_incomplete_leftovers:
            $ persistent.see_incomplete_leftovers = True
            "Incomplete mod content enabled."
            "Purchase a swimsuit for Julia and select the new \"We should relax by the pool today!\" option."
            "Please note that this toggle is technically only meant for scenes with no CGs. For example, Julia's swimsuit sex scenes, including revisits."
            "This toggle has been made for that reason, but these affected scenes are otherwise ready to play."
            "Click on this option again to disable at any time."
            call nate_room_empty
            return
        "Disable Incomplete Mod Content" if persistent.see_incomplete_leftovers:
            $ persistent.see_incomplete_leftovers = False
            "Incomplete mod content disabled."
            call nate_room_empty
            return
        "Enable Bonus Scenes" if not persistent.bonus_leftovers_enabled:
            $ persistent.bonus_leftovers_enabled = True
            "Bonus mod scenes enabled."
            "These are small scenes I threw in for fun!"
            "They are self-contained, and do not have any impact on the rest of the game and/or mod."
            "This also contains scenes I wrote up for my scrapped project, Sam's Awakening."
            "I realized how absurdly ambitious I was with that mod, and ultimately I ended up having no idea what to actually do with the mod."
            "I was also a beginner at the time, and was overly eager to prove that this kind of mod was possible to do."
            "Regardless, I still wanted things I had done for Sam's Awakening to see the light of day in some form."
            "So, as a fun what-could-have-been, here you go!"
            "Click on this option again to disable at any time."
            call leftovers_bonus_scene_list
            return
        "Disable Bonus Mod Content" if persistent.bonus_leftovers_enabled:
            $ persistent.bonus_leftovers_enabled = False
            "Bonus mod content disabled."
            call nate_room_empty
            return
#        "Enable Bonus CGs" if not persistent.bonus_leftovers:
#            $ persistent.bonus_leftovers = True
#            "Bonus mod CGs enabled."
#            "These are CGs made by BarryVaughn that I still wanted to include in some capacity, even if I currently cannot find a fit for them."
#            "Credit goes to him for making these!"
#            "Click on this option again to disable at any time."
#            call nate_room_empty
#            return
#        "Disable Bonus CGs Content" if persistent.bonus_leftovers:
#            $ persistent.bonus_leftovers_enable = False
#            "Bonus mod CGs disabled."
#            call nate_room_empty
#            return
        "Back":
            call nate_room_empty
            return

    return
