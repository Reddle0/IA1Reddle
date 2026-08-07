# Compatibility patch with Supersexual Awakening Remake (current build at time of updating: v0.05R)

###################################
# This patch includes:
# 1. A check to make sure that if the player has already completed the finale scene before this patch was added
# they will still get the toast and unlock Supersexual Awakening

# 2. A one-time toast that appears when the game detects that the player has completed the finale scene
# to let them know the mod story (Supersexual Awakening) is now unlocked
# 2a. Pop-up window with a message about the mod being unlocked and a button to dismiss it

# 3. A utility label that can be called to treat the start of Supersexual Awakening as a new day 
# (reinitializes variables, calls day_start etc.)

# 4. An override of SA's main menu to restore the base game buttons and add mod select

# 5. A complete re-do of SA's "skip to mod content" code to make it more compatible with other mods and less likely to cause issues down the line
# 5a. New screen for the skip confirmation, and a new label that applies the skip and then jumps to sa_start. No overriding of intro_0
# 5b. The original skip code is completely bypassed, and the old helper function it used is killed for the sake of the patch
# 5c. The skip confirmation screen also includes instructions for accessing the mod from an existing save, in case the player wants to do that instead of starting fresh with the skip
# 5d. Completely scrapped the "replayables" code that was in SA's original skip implementation, since it was very janky and caused a lot of issues. It shouldn't have even been looking for "replayablea" anyway. Non-stop issues getting it to work, so it got the axe
# 5e. Now looks for main story scenes and conversations and marks them as completed, which is enough to satisfy the base game's requirements for the finale. Uses actual base game variables, so no AI guesswork
# 5f. Also gives the player a small amount of money, maxes out their boldness, and maxes out all their relationships, to make sure they meet all the requirements for the finale scene and don't run into any issues trying to access SA content after the skip

###################################
# Thank you to DrX for this part! #
###################################
default persistent.finale_scene_done_for_mod_story_check = False

# one-time toast trigger
default mod_story_toast_pending = False
default mod_story_toast_shown = False

init 10 python:
    finale_tracker_old_label_callback = config.label_callback

    def finale_tracker_label_callback(label_name, jump_call_or_context):
        # also putting in day_advance_time just in case I guess
        if label_name in ["process_end_of_scene_before_advance_time", "day_advance_time"]:
            if "finale_scene" in store.scenes_completed:
                persistent.finale_scene_done_for_mod_story_check = True

        finale_tracker_old_label_callback(label_name, jump_call_or_context)
        return

    config.label_callback = finale_tracker_label_callback

    def final_tracker_after_load():
        if "finale_scene" in store.scenes_completed:
            if not persistent.finale_scene_done_for_mod_story_check:
                persistent.finale_scene_done_for_mod_story_check = True
                renpy.save_persistent()
            if not store.mod_story_toast_shown:
                store.mod_story_toast_pending = True
        return

    config.after_load_callbacks.append(final_tracker_after_load)

#######################
# supersexual utility #
#######################
init 205 python:
    import os
    if os.path.isdir(os.path.join(config.gamedir, "mods", "supersexual_awakening")):
        if (getattr(persistent, "finale_scene_done_for_mod_story_check", False)
            and not getattr(persistent, "supersexual_awakening_enabled", False)):
            persistent.supersexual_awakening_enabled = False
            renpy.save_persistent()

# Treats the Supersexual start as a new day
label supersexual_leftovers_new_day():
    call initialize_variables(force_reinitialization = True)

    call supersexual_leftovers_day

    return

label supersexual_leftovers_day:
    $ started_main_game = True
    call day_start

    return

####################
# supersexual menu #
####################
# Overrides SA's main menu:
# restores the base game buttons (original locations, buttons etc.)
# adds mod select

transform logo:
    xanchor 0.0
    xpos 0.01
    yanchor 1.0
    ypos 0.95

init 300:
    screen main_menu():
        tag menu

#        add "sa_slideshow"
        add "gui/main_menu.png"

        # add "mods/leftovers_mod/images/logo.png"
        # add "mods/supersexual_awakening/images/main_menu/logo.png" at logo_small # removed to restore the original IA logo

        text config.name style "default" size 120 xalign 0.5

        vbox:
            xalign 0.95
            yalign 0.4
            spacing 30

            use main_menu_button(text = "New Game", action = Start)

            if not wholesome_mode:
                use main_menu_button(text = "Load Game", action = ShowMenu("load") )

#            if store.finale_julia_sam:
                use main_menu_button(text="Mod Select", action = ShowMenu("mod_story_selection"))
        
            use main_menu_button(text = "Options", action = ShowMenu("preferences") )
            use main_menu_button(text = "FAQ", action = Jump("help") )
            use main_menu_button(text = "Quit", action = Quit(confirm = not main_menu))

        vbox:
            xanchor 0.0
            xpos 0.01
            yanchor 1.0
            ypos 0.95
            spacing 20
            use hover_text_button_2("images/interface/mastodon.png", Text("Baraag", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://baraag.net/@cyberhexxx"))
            use hover_text_button_2("images/interface/team cyber hexxx.png", Text("Blog", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://iathegame.blogspot.com/"))
            use hover_text_button_2("images/interface/discord.png", Text("Discord", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://discord.gg/qrEDPCa"))
            use hover_text_button_2("images/interface/subscribestar.png", Text("Support us!", size = 64, xalign = 0.5, yalign = 0.5), action = OpenURL("https://subscribestar.adult/cyberhexxx"))

        text "[config.version]":
            style "main_menu_version"
            size 36
            xanchor 1.0
            xpos 0.99
            yanchor 1.0
            ypos 0.97

# makes it so the SA toggle is in its own section instead of "Toggle Mods"

####################
# supersexual skip #
####################
# Patch overrides
init 999 python:
    import store

    # Force this patch to win over SA's skip code
    config.label_overrides["sa_intro_0"] = "patched_sa_intro_0"

    # Disable SA's skip helper functions
    # Anything related to "replayables" that SA tries to call/look for is scrapped for this patch
    # Obvious AI code that doesn't mesh well with the base game and other mods, and causes a lot of issues, so it's all gone
    def _pairs_for_replayables():
        return []

    # Minimal post-finale save equivalent
    def prepare_sa_skip_state():
        # The player only needs a small amount of money
        inventory.add_money(100)

        # Set boldness to the exact amount required for max level in the base game
        boldness_xp = stats.boldness_xp_required_for_level(stats.boldness_level_cap())
        stats.add_boldness_xp(boldness_xp, force_no_popup=True)

        # Set relationships to max
        for char in npc_list():
            relationship_cap = char.relationship_level_cap()

            if relationship_cap:
                char.points = char.xp_required_for_level(relationship_cap)
                char.relationship_level = relationship_cap

        # Progression flags that the base game uses
        store.had_julia_pre_arrival_scene = True
        store.had_julia_arrived_scene = True
        store.had_janet_intro_scene = True
        store.had_edna_pre_arrival_scene = True
        store.had_edna_intro_scene = True
        store.had_vicky_pre_intro_scene = True
        store.had_vicky_intro_scene = True

        # Set the minimum minigame states expected by the base game
        store.minigame_typing_times_succeeded = 3
        store.minigames_tried.add("minigame_table_tennis")

        # This doesn't need to be shown for the first time since it's post-finale
        store.dream_intro_shown = True

        # Mark base game scenes as complete
        for char in npc_list():
            store.scenes_completed.update(char.list_of_main_scenes())

        # Mark base game conversations as complete
        # Kacey and Vicky do not have conversations in the base game, so they are not included here

        # Kira
        store.k.conversations_completed.update({
            "kira_convo_1", "kira_convo_2", "kira_convo_3", "kira_convo_4",
            "kira_convo_5", "kira_convo_6", "kira_convo_7", "kira_convo_8",
            "kira_convo_9", "kira_convo_10", "kira_convo_11", "kira_convo_12",
            "kira_convo_13", "kira_convo_14", "kira_convo_15",
        })

        # Simone
        store.si.conversations_completed.update({
            "simone_convo_1", "simone_convo_2", "simone_convo_3", "simone_convo_4",
            "simone_convo_5", "simone_convo_6", "simone_convo_7", "simone_convo_8",
            "simone_convo_9", "simone_convo_11", "simone_convo_12",
            "simone_convo_13", "simone_convo_15",
        })

        # Sam
        store.sa.conversations_completed.update({
            "sam_convo_1", "sam_convo_2", "sam_convo_3", "sam_convo_4",
            "sam_convo_5", "sam_convo_6", "sam_convo_7", "sam_convo_8",
            "sam_convo_9", "sam_convo_10", "sam_convo_11", "sam_convo_12",
        })

        # Julia
        store.julia.conversations_completed.update({
            "julia_convo_1", "julia_convo_2", "julia_convo_3", "julia_convo_4",
        })

        # Janet
        store.janet.conversations_completed.update({
            "janet_convo_1", "janet_convo_2", "janet_convo_3", "janet_convo_4",
            "janet_convo_5", "janet_convo_6", "janet_convo_7",
        })

        # Edna
        store.edna.conversations_completed.update({
            "edna_convo_1", "edna_convo_2", "edna_convo_3",
            "edna_convo_4", "edna_convo_5", "edna_convo_6",
        })

        # after updating conversations, also update "recently completed"
        for char in npc_list():
            char.recently_completed_conversations = set()

# this adds supersexual into the extra story list when mod select rebuilds it
init 206 python:
    import os

    def refresh_supersexual_mod_story():
        if os.path.isdir(os.path.join(config.gamedir, "mods", "supersexual_awakening")):
            sa_locked = not (
                getattr(persistent, "finale_scene_done_for_mod_story_check", True)
                and getattr(persistent, "supersexual_awakening_enabled", True)
            )

            extra_mod_stories.append({
                "name": "Supersexual Awakening Remake",
                "image": "mods/leftovers_mod/images/supersexual_patch/supersexual_icon.png",
                "label": "patched_sa_intro_0",
                "locked": sa_locked,
                "status": "Locked" if sa_locked else "Unlocked",
                "show_unlock_toast": True,
                "toast_flag": "sa_toast_shown",
                "start_action": Show("sa_skip_modal"),
            })

    extra_mod_story_refreshers.append(refresh_supersexual_mod_story)

# Pop-up Window
screen sa_skip_modal():
    modal True
    zorder 200

    # dim background
    add Solid("#000") at Transform(alpha=0.55)

    # click outside to dismiss
    button:
        xfill True
        yfill True
        background None
        action Hide("sa_skip_modal")

    # centered panel
    fixed:
        xalign 0.5
        yalign 0.5
        xsize mod_story_box_w
        ysize mod_story_box_h
        at mod_story_panel_reveal

        # solid inner fill to avoid transparency
        add Solid("#111016") xpos 24 ypos 24 xsize (mod_story_box_w-48) ysize (mod_story_box_h-48) alpha 0.98

        # frame image on top
        add (
            Frame("images/interface/ShoppingMenuBox.png", mod_story_box_border, mod_story_box_border)
            if mod_story_box_border > 0
            else im.Scale("images/interface/ShoppingMenuBox.png", mod_story_box_w, mod_story_box_h)
        )

        # content of the pop-up
        frame:
            background None
            xfill True
            yfill True
            xpadding 48
            ypadding 36

            vbox:
                xalign 0.5
                #spacing 10

                text "Supersexual Awakening" size 56 xalign 0.5 color "#fff" outlines [(3, "#000c", 0, 0)]

                text "This option skips straight to the new mod content, after the finale." size 26 xalign 0.5 text_align 0.5 color "#fff"outlines [(2, "#000a", 0, 0)]
                text "To use an existing save, go to Nate's bedroom and choose:" size 26 xalign 0.5 text_align 0.5 color "#fff" outlines [(2, "#000a", 0, 0)]
                text "\"The summer ended! (Start Supersexual Awakening story)\"" size 26 xalign 0.5 text_align 0.5 color "#fff" outlines [(2, "#000a", 0, 0)]

                text "Skip to the new content now?" size 26 xalign 0.5 text_align 0.5 color "#fff"  outlines [(2, "#000a", 0, 0)]

                hbox:
                    xalign 0.5
                    spacing 60

                    textbutton "Yes":
                        text_size 34
                        action Start("patched_sa_intro_0")

                    textbutton "No":
                        text_size 34
                        action Hide("sa_skip_modal")

    use back_button(click_action = Hide("sa_skip_modal"), xalign = 0.98, yalign = 0.98)

# patched intro label
label patched_sa_intro_0:
    $ renpy.set_return_stack([])
    $ renpy.block_rollback()
    $ renpy.scene("screens")
    $ started_main_game = True

    call clear_and_reset_characters
    $ prepare_sa_skip_state()
    jump sa_start