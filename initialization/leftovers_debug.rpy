# DEBUG #
init 300 python:
    config.label_overrides["nate_room_debug"] = "nate_room_debug_leftovers"

label nate_room_debug_leftovers:
    menu:
        "(DEBUG) Add Boldness":
            jump debug_boldness_check
        "(DEBUG) Add max money":
            jump debug_max_money
        "(LEFTOVERS DEBUG) Check Impreg State":
            jump debug_impreg_2
        "(LEFTOVERS DEBUG) Set Impreg State":
            jump debug_impreg
        "(LEFTOVERS DEBUG) Remove Impreg State":
            jump debug_unpreg
        "(BLEEP DEBUG) Play Bleep Parser scene":
            jump shit_test
        "(SAM DEBUG) Set Sam Side Story to True":
            jump sam_story_check
        "(LEFTOVERS DEBUG) Play Texting Test":
            jump text_test

        "Mark Finale Scene Done":
            "added"
            $ scenes_completed.add("finale_scene")
        
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