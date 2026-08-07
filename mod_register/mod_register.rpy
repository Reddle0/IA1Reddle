# Mod Register #

# sets up the list of supported mods, stores their detect/enable vars, and keeps their help text together
# this is what the mod menu reads from when it builds the mod list on screen

# Default Leftovers Mod Registration #
init 2 python:
    import os

    # Format: #
    # if renpy.exists("mods/your_mod.rpy"):
    #     mod_registry.append(("Your Mod Name", "persistent_mod_name_detected", None))
    #
    # if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "your_mod")):
    #     mod_registry.append(("Your Mod Name", "persistent_mod_name_detected", None))

    # This mod is *not* toggleable, just detected
    mod_registry.append(("Leftovers Mod", "leftovers_mod_detected", None))

    # This mod is toggleable
    mod_registry.append(("Smol Tits Mod", "oimon_mod_detected", "oimon_mod_enabled"))

    # This mod is *not* toggleable, just detected
    mod_registry.append(("Anim Mod", "anim_mod_detected", None))

    # Other Mods #

    # This mod is *not* toggleable, just detected. ONLY do this for full mod folders.
    if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "pregnancy_epilogue_remake_mod")):
        mod_registry.append(("Pregnancy Epilogue Remake Mod", "pregnancy_epilogue_remake_mod_detected", None))

    # This mod is *not* toggleable, just detected. ONLY do this for full mod folders.
    if os.path.isdir(os.path.join(config.gamedir, "mods", "sam_side_story")):
        mod_registry.append(("Sam Side Story", "side_story_detected", None))

    if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "supersexual_awakening")):
        mod_registry.append(("Supersexual Awakening Remake", "supersexual_awakening_detected", None))

    # This mod is toggleable. ONLY do the first check for single .rpys.
    if renpy.exists("mods/skip_minigames.rpy") or os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "skip_minigames")):
        mod_registry.append(("Skip Minigames", "skip_minigames_enabled", None))

    # Add your mod below. Make sure it uses your actual variables! #
    # mod_registry.append(("Your Mod Name", "persistent_mod_name_detected", None))

    # Format: #
    # A is for single-file mods. B is for mod folders.

    # A. if renpy.exists("mods/your_mod.rpy):
    # B. if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "your_mod")):

init 3 python:
    import os

    # Format: #
    # mod_help_texts["My Mod"] = "My Mod makes Nate have infinite stamina."

    mod_help_texts["Leftovers Mod"] = "Mega-Mod that expands upon the base game. New scenes, bust-art, conversations, minigames, relationship levels, impregnation overhaul, and much more!"
    mod_help_texts["Smol Tits Mod"] = "Edits Sam and Julia's breast sizes to be more visually consistent across the game's scenes, when breasts are visible. Also gives Sam slightly more of a flatter chest."
    mod_help_texts["Anim Mod"] = "Majorly overhauls some existing scenes to have them become animated sequences. Affects Sam's vaginal scene and both revisits, as well as Julia's anal scene and both revisits."

    # Cru Remake Mod #
    if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "pregnancy_epilogue_remake_mod")):
        mod_help_texts["Pregnancy Epilogue Remake Mod"] = "This mod adds epilogue CG scenes for all characters, excluding Kira. Completely reworked and updated art, hand-drawn by Cru, plus improvements."

    if renpy.exists("mods/skip_minigames.rpy") or os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "skip_minigames")):
        if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "leftovers_mod")):
            mod_help_texts["Skip Minigames"] = "Lightweight mod that skips the minigames. Functionality has been disabled due to Leftovers Mod, which turns this mod into a purchasable item."
        else:
            mod_help_texts["Skip Minigames"] = "Lightweight mod that skips the minigames."

    if os.path.isdir(os.path.join(config.gamedir, "mods", "sam_side_story")):
        mod_help_texts["Sam Side Story"] = "A DLC-esque side story where you play as Sam, Nate's twin sister!"

    if os.path.isdir(os.path.join(renpy.config.gamedir, "mods", "supersexual_awakening")):
        mod_help_texts["Supersexual Awakening Remake"] = "A new remake of the old project of the same name, featuring a new story using the same characters you fell in love with, and new characters!"

    # Add your mod below. Make sure it uses your actual variables! #
    # mod_help_texts["My Mod"] = "My Mod makes Nate have infinite stamina so he can cum lots."