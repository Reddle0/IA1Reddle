# DO NOT REMOVE FROM THE LEFTOVERS FOLDER! #
# THIS IS REQUIRED FOR LEFTOVERS ! #

# Mod Detection #
# checks which supported mods are present and updates the detected flags
# also checks for skip_minigames.rpy so the mod menu can show it properly

# Detects if certain mods are present
init -99 python:
    detected_mods = []

    # Leftovers Mod
    if os.path.isdir(os.path.join(config.gamedir, "mods", "leftovers_mod")):
        detected_mods.append("leftovers_mod")

    # Supersexual Awakening Remake
    if os.path.isdir(os.path.join(config.gamedir, "mods", "supersexual_awakening")):
        detected_mods.append("supersexual_awakening")

    # Pregnancy Epilogue Remake
    if os.path.isdir(os.path.join(config.gamedir, "mods", "pregnancy_epilogue_remake_mod")):
        detected_mods.append("pregnancy_epilogue_remake_mod")

# Skip Minigames
init -99 python:
    skip_minigames_enabled = False

    # if the single .rpy exists, enable Skip Minigames
    if renpy.exists("mods/skip_minigames.rpy"):
        skip_minigames_enabled = True

# Persistent Variables / Misc Detection
init -99 python:
    if persistent.leftovers_mod_detected:
        # Smol Tits Mod
        if not hasattr(persistent, "oimon_mod_detected"):
            persistent.oimon_mod_detected = True
        if not hasattr(persistent, "oimon_mod_enabled"):
            persistent.oimon_mod_enabled = True

        # Anim Mod
        if not hasattr(persistent, "anim_mod_detected"):
            persistent.anim_mod_detected = True

init 2 python:
    if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "pregnancy_epilogue_remake_mod")):
        persistent.pregnancy_epilogue_remake_mod_detected = True

init 2 python:
    if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "supersexual_awakening")):
        persistent.supersexual_awakening_detected = True

# Splash for Skip Minigames
label splashscreen_skip_minigames:
    if skip_minigames_enabled:
        show bg warning
        show screen splash_text_skip_minigames

        with dissolve
        $ renpy.pause(2)
        show splash_ctc
        $ renpy.pause()

        hide screen splash_text_skip_minigames
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
    screen splash_text_skip_minigames:
        vbox:
            xalign 0.5
            yalign 0.5

            text "{b}Skip Minigames detected!{/b}" size 40 xalign 0.5
            text "Now loading..." size 24 xalign 0.5

label skip_minigames_check:
    if skip_minigames_enabled:
        "Skip Minigames is detected."
    else:
        "Skip Minigames is not detected."

    jump nate_room_empty
    return
