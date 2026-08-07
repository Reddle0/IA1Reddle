# Story Save Variables #
default had_anna_intro_scene = True
default had_anna_confession = False
default had_met_anna_grandma = False
default had_anna_mom_scene = False

# Anna Save Variable #
init 2:
    default anna = Anna()

init 2 python:
# Anna's Class #
    class Anna(IA_Actor):
        def __init__(self, internal_name = "anna", variable_name = "anna"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return

        def hide_notifications(self):
            return persistent.hide_anna_notification

        #################################
        #           defaults            #
        #################################
        def default_color(self):
            return "#89CFF0"

        def default_say_name(self):
            return "Anna"

        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"

            return "clothes"

        # Edit this accordingly when you have the anna images done
        def default_pose(self):
            return "handclasp"

        def decide_default_location(self):
            self.place_and_set_scene(kitchen)
            return

            if not store.had_anna_intro_scene:
                return

            self.place_and_set_scene(kitchen)

            return

        #################################
        #   character select screen     #
        #################################
        # Edit this accordingly when you have the anna images done
        def hovered_pose(self):
            return "armunder"

        # Edit this accordingly when you have the anna images done
        def unhovered_pose(self):
            return "handclasp"

        # Once you get the anna images done, you can remove this method
        def hovered_base_image_filename(self):
            return "anna" + "base " + self.hovered_pose() + "_" + self.hovered_outfit()

        # Once you get the anna images done, you can remove this method
        def unhovered_base_image_filename(self):
            return "anna" + "base " + self.unhovered_pose() + "_" + self.unhovered_outfit()

        # Once you get the anna images done, you can remove this method
        def hovered_face_image_filename(self):
            return "anna" + "face " + self.face_pose(self.hovered_pose()) + "_" + self.hovered_face()

        # Once you get the anna images done, you can remove this method
        def unhovered_face_image_filename(self):
            return "anna" + "face " + self.face_pose(self.unhovered_pose()) + "_" + self.unhovered_face()

        # Edit this accordingly when you have the anna images done
        def character_select_button_crop_left(self):
            return 160

        # Edit this accordingly when you have the anna images done
        def character_select_button_crop_top(self):
            return 465

        # Edit this accordingly when you have the anna images done
        def character_select_button_crop_right(self):
            return 215

        # this is if you get an error for missing images when you used 'bikini' instead of 'swimsuit'
        def fix_appearance(self):
            if self.outfit == "swimsuit":
                self.outfit = "bikini"

            return

        # if your charcter has different faces depending on the pose (i.e. sam's leaning pose), this NEEDS to be adjusted
        def face_pose(self, pose):
            if pose == "handsfront":
                return "handsfront"
            return pose

        #################################
        #        mod rendering          # 
        #################################
        # this is what gets the modded character to actually show up

        # Once you get the anna images done, you can remove this method
        def base_image_filename(self):
            return "anna" + "base " + str(self.pose) + "_" + self.outfit

        # Once you get the anna images done, you can remove this method
        def face_image_filename(self):
            return "anna" + "face " + self.face_pose(self.pose) + "_" + self.face

        # Edit this accordingly when you have the anna images done
        def icon_image(self, suffix = ""):
            string = "mods/leftovers_mod/images/interface/" + "Anna" + "_Face_Icon" + suffix
            if self.is_hidden_on_stat_screen():
                string = string + "_Hidden"
            string = string + ".png"
            return string

        ################################
        #           stats              # 
        ################################
        def is_hidden_on_stat_screen(self):
            if not store.had_anna_intro_scene:
                return True

            return False

        def show_on_stat_screen(self):
            return True

        def display_scene_stats(self):
            return store.had_anna_intro_scene

        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0

            elif level == 2:
                return 2

            elif level == 3:
                return 4

            elif level == 4:
                return 8

            return 999999999

        def relationship_level_cap(self):
            return 28

        ################################
        #       convos/scenes          #
        ################################
        def add_conversations_to_pool(self):
            #self.test_and_add_conversation_to_pool(conversation_name = "anna_convo_default")
            self.test_and_add_conversation_to_pool(conversation_name = "anna_test")

            return

        def conversation_max(self):
            return 1

        def list_of_main_scenes(self):
            scenes = []
            return scenes

        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "anna_scene_bath":
                return 5
            return 0

        def prompt_label(self, scene_name):
            if scene_name == "anna_scene_bath":
                return "I'd like to bath together again, [anna.say_name]..."
            return ""

        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "edna_scene_intro_2":
                return True
            if scene_name == "edna_scene_nate_underwear":
                return True
            return False

        def decide_normal_scene(self):
            if not store.had_anna_intro_scene:
                return

#        def revisitable_scene_choice_label(self, scene_name):
#            if scene_name == "anna_scene_bath":
#                if "edna_scene_handjob_revisit" not in store.scenes_completed:
#                    return "Let's bath together again, [anna.say_name]!"
#                else:
#                    return "Can we bath together again, [anna.say_name]?"

#            return ""

#        def replayable_scene_choice_label(self, scene_name):
#            if scene_name == "anna_scene_bath":
#                return "When I had a bath with [anna.say_name]..."

#            return ""

        ################################
        #          minigames           #
        ################################
#        def available_minigames(self):
#            minigame_call_labels = []
#            if "edna_scene_minigame_intro" in scenes_completed:
#                minigame_call_labels.extend(["minigame_table_tennis"])

#            return minigame_call_labels

#        def racing_icon_losing(self):
#            return self.icon_image("")

#        def racing_icon_losing_bad(self):
#            return self.icon_image("_Surprised")

#        def racing_icon_winning(self):
#            return self.icon_image("_Happy")

        #################################
        #           gallery             # 
        #################################
        def gallery_unlock_name_requirement(self):
            return store.had_anna_intro_scene

        def gallery_unlock_scene_thumbnail_requirement(self):
            return "edna_scene_handjob"

        def should_appear_in_gallery(self):
            return True

        def gallery_images(self):
            images = []
            if "edna_scene_handjob" in scenes_completed:
                images.append("images/bg/edna/Edna Handjob/bg edna_hottub.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_NoSimone.png")

            if "edna_scene_titfuck" in scenes_completed:
                images.append("images/bg/edna/edna titfuck/bg edna_titrub.png")
                images.append("images/bg/edna/edna titfuck/bg edna_titsuck.png")
                images.append("images/animations/edna titfuck bikini/edna_titfuck_anim_0.png")

                if "edna_scene_titfuck_revisit" in scenes_completed:
                    images.append("images/bg/edna/edna titfuck/bg edna_nude_titfuck_nocum_smile.png")
                    images.append("images/animations/edna titfuck nude/edna_titfuck_nude_anim_0.png")

            images.extend(self.finale_images())
            return images

        def gallery_thumbnail(self):
            return "images/bg/edna/Edna Handjob/bg edna_hottub.png"

        def gallery_bust_art_default_pose(self):
            return "handclasp"

        def gallery_bust_art_poses(self):
            return ["handclasp", "armunder", "handsfront"]
            # "twohandfist"]

        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            faces.extend(["surprised"]) # if your character is smol, you can omit this
            return faces

        def gallery_bust_art_outfits(self):
            outfits = ["clothes"]

            if "sam_scene_swimsuit" in scenes_completed:
                outfits.extend(["bikini"])

            if "sam_scene_3" in scenes_completed:
                outfits.extend(["hoodie"])

            if "sam_scene_1_seq_1" in scenes_completed:
                outfits.extend(["underwear"])

            if "sam_scene_2_seq_2" in scenes_completed:
                outfits.extend(["nude"])

            if "sam_scene_3" in scenes_completed:
                outfits.extend(["topless", "bra_bottomless"])

            return outfits

        def gallery_bust_art_can_be_shown(self):
            return store.had_anna_intro_scene

        def gallery_bust_art_enabled(self):
            return True

label anna_test:
    call process_character(anna, appearance = "pose handclasp face neutral")
    anna.c "Yo what up man"
    anna.c "I can count to 3, look"
    anna.c "1"
    anna.c "2"
    call process_character(anna, appearance = "pose armunder face angry")
    anna.c "3"

    call process_end_of_conversation("anna_test", anna, priority = False, default = False)
    return

################################
#       method overrides       #
################################
init 100 python:
    # record the old version of the function so we can use it later
    leftovers_old_npc_list = npc_list

    # make a new function that uses the old function and then adds a new character to the array
    def leftovers_npc_list():
        character_list = leftovers_old_npc_list()

        if store.anna not in character_list:
            character_list.append( store.anna )

        return character_list

    # replace old npc list function with the new one
    npc_list = leftovers_npc_list

################################
#        Anna's family         #
################################

# Establishing a New Family #
init 1:
    default anna_mom = Anna_Mom()
    default anna_grandma = Anna_Grandma()
    default anna_family_last_name = "Roberts" 

init 100 python:
    def anna_family_list():
        character_list = []

        if hasattr(store, "anna_mom") and store.anna_mom is not None:
            character_list.append(store.anna_mom)

        if hasattr(store, "anna") and store.anna is not None:
            character_list.append(store.anna)

        if hasattr(store, "anna_grandma") and store.anna_grandma is not None:
            character_list.append(store.anna_grandma)

        return character_list

# Anna's Mom #
# 1. Has bust art #
# 2. Is interactible #
init 1 python:
    class Anna_Mom(IA_Actor):
        def __init__(self, internal_name = "anna_mom", variable_name = "anna_mom"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return

        def default_color(self):
            return "#AA89F0"

        def character_select_button_crop_left(self):
            return 56

        def character_select_button_crop_top(self):
            return 254

        def character_select_button_crop_right(self):
            return 43

        def default_say_name(self):
            return "Evelyn"

        def default_outfit(self):
            return "clothes"

        def default_pose(self):
            return "handhip"

        def hovered_outfit(self):
            return self.default_outfit()

        def unhovered_outfit(self):
            return self.default_outfit()

        def hovered_pose(self):
            return "armunder"

        def unhovered_pose(self):
            return "handclasp"

        def face_pose(self, pose):
            if pose == "handclasp":
                return "handclasp"
            return pose

        def is_hidden_on_stat_screen(self):
            if not store.had_anna_mom_reveal:
                return True

            return False

        def show_on_stat_screen(self):
            return True

        def display_scene_stats(self):
            return store.had_anna_mom_reveal

        def decide_default_location(self):
            if not store.had_anna_mom_reveal:
                return

            self.place_and_set_scene(fortune_teller)

            return

# Anna's Grandma #
# 1. Has bust art #
# 2. Is *not* interactible, so her class is more limited #
    class Anna_Grandma(IA_Actor):
        def __init__(self, internal_name = "anna_grandma", variable_name = "anna_grandma"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return

        def default_color(self):
            return "#F0AA89"

        def default_say_name(self):
            return "Mrs. [anna_family_last_name]"

        def default_outfit(self):
            return "clothes"

        def default_pose(self):
            return "handhip"