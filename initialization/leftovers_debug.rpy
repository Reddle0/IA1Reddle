##########
# Debug #
##########

init 999 python:
    config.label_overrides["nate_room_debug"] = "nate_room_debug_leftovers"

label nate_room_debug_leftovers:
    menu:
        "Base Game":
            jump debug_page_base
        "Mod Page: Leftovers":
            jump debug_page_leftovers_menu
        "Mod Page: Sam Side Story":
            jump debug_page_sam
        "Mod Page: Supersexual":
            jump debug_page_supersexual
        "Mod Detection":
            jump debug_page_detection
        "Flowchart Test":
            show bg black
            call screen flowchart

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_base:
    menu:
        "(DEBUG) Add Boldness":
            jump debug_boldness_check
        "(DEBUG) Add max money":
            jump debug_max_money

        "Mark Finale Scene Done":
            "added"
            $ scenes_completed.add("finale_scene")

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_leftovers_menu:
    menu:
        "Utility":
            jump debug_page_leftovers_page_utility
        "Julia":
            jump debug_page_leftovers_page_julia

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_leftovers_page_utility:
    menu:
        "Check Impreg State":
            jump debug_impreg_2
        "Set Impreg State":
            jump debug_impreg
        "Remove Impreg State":
            jump debug_unpreg
        "Play Phone Test":
            jump phonestart
        "(BLEEP DEBUG) Play Bleep Parser scene":
            jump shit_test
        "Turn SFW mode on":
            jump debug_sfw_mode
        "Turn SFW mode off":
            jump debug_sfw_mode_off
        "Turn Debug off":
            jump debug_off

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_leftovers_page_julia:
    menu:
        "julia_scene_swimsuit_revisit":
            call julia_scene_swimsuit_revisit
        "julia_scene_swimsuit_revisit_first_time_normal":
            call julia_scene_swimsuit_revisit_first_time_normal
        "julia_scene_swimsuit_revisit_second_time_normal":
            call julia_scene_swimsuit_revisit_second_time_normal              
        "julia_scene_swimsuit_revisit_first_time_nude":
            call julia_scene_swimsuit_revisit_first_time_nude
        "julia_scene_swimsuit_revisit_second_time_nude":
            call julia_scene_swimsuit_revisit_second_time_nude
        "julia_scene_swimsuit_revisit_first_time_vaginal":
            call julia_scene_swimsuit_revisit_first_time_vaginal
        "julia_scene_swimsuit_revisit_second_time_vaginal":
            call julia_scene_swimsuit_revisit_second_time_vaginal

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_sam:
    menu:
        "Set Sam Side Story to True":
            jump sam_story_true
        "Set Sam Side Story to False":
            jump sam_story_false
        "Check if Sam Side Story is True":
            jump sam_story_check

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_supersexual:
    menu:
        "Set Sam Side Story to True":
            jump sam_story_true
        "Set Sam Side Story to False":
            jump sam_story_false

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_page_detection:
    menu:
        "Check if Skip Minigames is detected":
            jump skip_minigames_check
        "Check suspected undetected mods":
            jump debug_mod_check

        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

label debug_boldness_check:
    menu:
        "Set to 1":
            $ stats.boldness_level = 1
            $ stats.boldness_xp = 0
        "Add 2 points":
            call debug_boldness_2
        "Add 999 points":
            call debug_boldness_999
        "Back":
            jump nate_room_empty

    jump nate_room_empty
    return

    if started_main_game:
        $ advance_time_return_location.start()

    return

label debug_mod_check:
    python:
        import os

        mod_checks = {
            "Pregnancy Epilogue Remake Mod": "pregnancy_epilogue_remake_mod",
            "Sam Side Story": "sam_side_story",
            "Skip Minigames": "skip_minigames.rpy",
            "Supersexual Awakening": "supersexual_awakening",    
        }

        results = []

        for mod_name, value in mod_checks.items():
            if value.endswith(".rpy"):
                path = "mods/" + value
                found = renpy.exists(path)
                results.append("{} (file: {}) -> {}".format(mod_name, value, "FOUND" if found else "NOT FOUND"))
            else:
                folder_path = os.path.join(config.gamedir, "mods", value)
                found = os.path.isdir(folder_path)
                results.append("{} (folder: {}) -> {}".format(mod_name, value, "FOUND" if found else "NOT FOUND"))

    python:
        for r in results:
            renpy.say(None, r)

    jump nate_room_empty
    return

label debug_off:
    $ config.developer = False
    "Debug now disabled. Use ONLY for testing!"

    jump nate_room_empty
    return

label debug_sfw_mode:
    $ persistent.sfw_mode = True

    "SFW mode now on. Use ONLY for showcasing and/or testing!"

    jump nate_room_empty
    return

label debug_sfw_mode_off:
    $ persistent.sfw_mode = False

    "SFW mode now off."

    jump nate_room_empty
    return

###############################################
# Define a fading overlay
image fade_white_overlay = Solid("#FFFFFF")

# Anna Showcase Item #
image kira_test = "gui/window_icon.png"

screen item_showcase():
    modal True
    zorder 100

    add Solid("#00000080")

    frame:
        at fade_in_zoom
        background Frame("gui/textbox.png", 30, 30)
        padding (30, 30)
        xalign 0.5
        yalign 0.5

        add "kira_test" xalign 0.5 yalign 0.5

    # Click to dismiss
    textbutton "Close" action Hide("item_showcase") xalign 0.5 yalign 0.95

transform fade_in_zoom:
    alpha 0.0 zoom 0.8
    linear 0.3 alpha 1.0 zoom 1.0

# Label Test #
label text_test:
    $ replace_position = True

    call process_scene_beginning()

#    call bust_art_background("bg family_portrait")
    $ clear_characters()
#    $ process_character(julia, "outfit clothes position right")    

#    "{i}My cousin, [julia.say_name]!{/i}"

    #Comment: Texting SFX
    call play_new_chat

    # pause to have a slightly delayed recation
    pause 1

    call process_character(n, appearance = "outfit clothesjacket pose handpocket face curious blush false")
    n.c "...{p}..."

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(It's from [gloryhole_girl.say_name]!)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(What's it say...)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "..."

    call character_leave_dissolve(n)
    pause 0.5

    #Comment: Bring up phone interface. Must always use the variable, i.e. "n" for nate, "si" for simone
    call texting_preparation(gloryhole_girl)

    kacey_nvl "Hi [n.say_name]! Hope you're doing well!"
    $ phone_slide_up = False # requied or else it will slide up on every single message
    kacey_nvl "I've got my own apartment now!"
    kacey_nvl "{🤯}"
    kacey_nvl "Crazy, right?"
    kacey_nvl "I'd love for you to come see it!"
    kacey_nvl "It's a couple blocks away, but I've sent you directions on your phone to easily get here."
    kacey_nvl "When you're on the right block, it'll be the big white building right in front of you."
    kacey_nvl "You can't miss it!"
    kacey_nvl "I'll be waving at you from my apartment window. {👋}"
    kacey_nvl "Don't keep me waiting! {❤️}"

    call texting_hide_phone(hide_window = False, clear_nvl = False) # two arguments, clear_nvl is set to False to prevent message history being cleared
    # hide_window is set to False to help prevent a visual bug of the phone "ghosting" into view again if nvl isn't cleared
    window auto hide

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(She sounds really excited about this!)"

    call character_leave_dissolve(n)
    pause 0.5

    $ phone_slide_up = True
    nate_nvl "I'll be there in a few minutes [gloryhole_girl.say_name]!"
    $ phone_slide_up = False
    call texting_hide_phone(hide_window = True)
    window auto hide

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(There!)"

    call process_character(n, appearance = "outfit clothesjacket pose twohandfist face happy blush false")
    n.c "(Better head over as soon as I can!)"

    show screen item_showcase

    # Testing Long FTBs
    $ clear_characters()
    show fade_white_overlay at truecenter zorder 100:
        alpha 0.0
        linear 4.0 alpha 1.0  # 4-second smooth fade to white

    $ renpy.pause(7.0, hard=True) # hard pause

    scene black with fade

    call process_end_of_scene("text_test", char = gloryhole_girl, dream = dream)

    return

label shit_test:
    call process_character(julia, appearance = "outfit clothes face neutral pose handface")
    julia.c "I am speaking with a neutral face and the \"handface\" pose."
    
    #Comment: This is a comment.
    
    #Comment: The above line will cause the parser to put in a comment in the code that says \"#This is a comemnt.\"
    
    call process_character(julia, appearance = "face neutral")
    julia.c "I am speaking with a neutral face again, but using an abbreviation in the document."
    
    call process_character(julia, appearance = "face flirty blush true pose handup")
    julia.c "Now I'm blushing with the flirty face and the handup pose."
    
    menu:
        "This is the first choice.":
            call process_character(n, appearance = "face happy pose handfist")
            n.c "I chose the first choice!"
            
            call process_character(julia, appearance = "face neutral pose handface")
            julia.c "Wow, you did, didn't you."

        "I like to read books!":
            call process_character(n, appearance = "face happy pose handfist")
            n.c "I read a million books yesterday!"
            call add_points(julia, 1, tag = "replace_me")            
            call process_character(julia, appearance = "face neutral pose handface")
            julia.c "Surprising."
            
            call process_character(julia, appearance = "face neutral")
            julia.c "When you add a relationship point, make sure to change the tag to a unique one in the code."

    call process_character(julia, appearance = "face neutral")
    julia.c "Looks like the dialog options ended."
    
    # Conditional: If Nate has had anal sex    
    if persistent.leftovers_mod_detected:
        call process_character(n, appearance = "face happy pose twohandfist")
        n.c "I've had anal sex before!"
        
        call process_character(julia, appearance = "face neutral")
        julia.c "Yeah, I know, I was there."

    elif persistent.leftovers_mod_detected:
        # Conditional: If Nate has not had anal sex.
        
        call process_character(n, appearance = "face curious pose behindhead blush true")
        n.c "What's anal sex?"
        
        call process_character(julia, appearance = "face neutral pose handup")
        julia.c "Ask your mom."

    call process_character(julia, appearance = "face neutral")
    julia.c "When you put in conditionals, they don't automatically create the proper code expression to evaluate in the if else."
    
    call process_character(julia, appearance = "face neutral")
    julia.c "The parser will create code that that is \"if False\" or \"elif False\"."
    
    call process_character(julia, appearance = "face neutral")
    julia.c "You still need to write the proper conditional code yourself."
    
    call process_character(n, appearance = "face curious")
    n.c "I heard that conditionals can also be nested."
    
    # Conditional: If Nate has a lot of money.    
    if persistent.leftovers_mod_detected:
        n.c "I have a lot of money!"
        
        # Conditional: If Nate doesn't have a lot of boldness.        
        if persistent.leftovers_mod_detected:
            call process_character(n, appearance = "face sad")
            n.c "I have a lot of money, but not a whole lot of boldness."

        call process_character(julia, appearance = "face neutral")
        julia.c "..."

    elif persistent.leftovers_mod_detected:
        # Conditional: If Nate doesn't have a lot of money.
        
        call process_character(n, appearance = "face neutral")
        n.c "I don't have a lot of money..."
        
        # Conditional: If Nate has a lot of boldness.        
        if persistent.leftovers_mod_detected:
            call process_character(n, appearance = "face happy")
            n.c "But I am pretty bold!"

        elif persistent.leftovers_mod_detected:
            # Conditional: If Nate doesn't have a lot of boldness.
            
            call process_character(n, appearance = "face sad")
            n.c "And I'm not very bold."

        call process_character(julia, appearance = "face neutral")
        julia.c "..."

    call process_character(n, appearance = "face happy outfit nudehard")
    n.c "I'm naked now!"
    
    call process_character(julia, appearance = "face happy outfit nude")
    julia.c "Fine, I'll get naked too."
    
    call process_character(n, appearance = "face happy")
    n.c "Let's fuck!"
    
    call fade_to_black
    
    call static_still_ctc("bg julia_anal_fuck")
    julia.c "T-This is the end of the parser document writing example."
    julia.c "You still need to understand how to write renpy and IA1 code... the parser just makes certain things faster."
    n.c "H-Hope you learned something!"
    n.c "Nngh!"

    return