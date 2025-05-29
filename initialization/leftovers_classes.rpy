# 17/02/25 Fix for Sam's Twinstick Hat in the Bust Art Gallery

# new method for loading images from the mod folders
init 2 python:
    mod_image_folder_prefixes.append("mods/leftovers_mod/images")

## Sounds (Minigames) ##
init 99 python:
    def leftovers_sound_files(type):
        leftovers_files = []

        files = renpy.list_files()
        files = [string for string in files if "mods/leftovers_mod/audio/music/" or "mods/leftovers_mod/audio/sounds/" + type + "/" in string and ".ogg" in string]

        return files

# Resetting Appearances when backing out of the Gallery
init 2 python:
    def gallery_bust_art_back():
        clear_characters()
        reset_all_characters()
        renpy.call("gallery_bust_art")
        return

# ^^ This fixes issues in the line-up like Sam's Twinstick Hat text, Edna's hat "hitbox", and so on.
###

init 100 python:
    def kacey_base_image_filename(self):
        return "kaceybase " + str(self.pose) + "_" + self.outfit

    Gloryhole_Girl.base_image_filename = kacey_base_image_filename

    def kacey_face_image_filename(self):
        return "kaceyface " + self.face_pose(self.pose) + "_" + self.face

    Gloryhole_Girl.face_image_filename = kacey_face_image_filename

    def kacey_blush_image_filename(self):
        if self.blush == True:
            return "kaceyblush " + self.blush_pose(self.pose)
        else:
            return "invisible_char_part"

    Gloryhole_Girl.blush_image_filename = kacey_blush_image_filename

    def kacey_hovered_base_image_filename(self):
        return self.base_image_filename()

    Gloryhole_Girl.hovered_base_image_filename = kacey_hovered_base_image_filename

    def kacey_unhovered_base_image_filename(self):
        return self.base_image_filename()

    Gloryhole_Girl.unhovered_base_image_filename = kacey_unhovered_base_image_filename

    def kacey_hovered_face_image_filename(self):
        return self.face_image_filename()

    Gloryhole_Girl.hovered_face_image_filename = kacey_hovered_face_image_filename

    def kacey_unhovered_face_image_filename(self):
        return self.face_image_filename()

    Gloryhole_Girl.unhovered_face_image_filename = kacey_unhovered_face_image_filename

## Getting Kacey's Glasses to Render ##
    def kacey_gallery_glasses_list(self):
        return ["", "glasses"]

    Gloryhole_Girl.gallery_glasses_list = kacey_gallery_glasses_list

    def kacey_has_separate_glasses(self):
        return True

    Gloryhole_Girl.has_separate_glasses = kacey_has_separate_glasses

    def kacey_default_glasses(self):
        return "glasses"

    Gloryhole_Girl.default_glasses = kacey_default_glasses

    def kacey_glasses_image_filename(self):
        if not self.glasses:
            return "invisible_char_part"
        return "kaceyglasses " + self.glasses + " " + self.pose

    Gloryhole_Girl.glasses_image_filename = kacey_glasses_image_filename

## New Bust Art Icons ##
init 2 python:
    def icon_image(self, suffix = ""):
        string = "mods/leftovers_mod/images/interface/" + "Kacey" + "_Face_Icon" + suffix
        if "gloryhole_scene_stall" not in store.scenes_completed:
            string = string + "_Hidden"
        string = string + ".png"
        return string

    Gloryhole_Girl.icon_image = icon_image

    def icon_image(self, suffix = ""):
        string = "mods/leftovers_mod/images/interface/" + "Vicky" + "_Face_Icon" + suffix
        if "vicky_tease_scene" not in store.scenes_completed:
            string = string + "_Hidden"
        string = string + ".png"
        return string

    Vicky.icon_image = icon_image

## Vicky ##
init 100 python:
    def has_location_navigation_icon(self):
        return True

    Vicky.has_location_navigation_icon = has_location_navigation_icon

    def use_character_select(self):
        return True

    Vicky.use_character_select = use_character_select

    def default_outfit(self):
        if store.finale_scene_completed_with_julia_sam:
            return "nude"

        if "finale_scene" in store.scenes_completed and self in store.vicky_apartment.character_list() and len(store.vicky_apartment.character_list()) == 1:
            return "nude"

        if "vicky_scene_vaginal" in store.scenes_completed and self in store.vicky_apartment.character_list() and len(store.vicky_apartment.character_list()) == 1:
            return "nude"

        if (not self.scene or self.play_scene_even_with_prompted_scene) and "vicky_titjob_scene" in store.scenes_completed and self in store.vicky_apartment.character_list() and len(store.vicky_apartment.character_list()) == 1:
            return "topless"

        if (not self.scene or self.play_scene_even_with_prompted_scene) and "vicky_tease_scene" in store.scenes_completed and self in store.vicky_apartment.character_list() and len(store.vicky_apartment.character_list()) == 1:
            return "underwear"

        return "clothes"

    Vicky.default_outfit = default_outfit

    def default_pose(self):
        return "handhip"

    Vicky.default_pose = default_pose

    def hovered_outfit(self):
        return self.default_outfit()

    Vicky.hovered_outfit = hovered_outfit

    def unhovered_outfit(self):
        return self.default_outfit()

    Vicky.unhovered_outfit = unhovered_outfit

    def hovered_pose(self):
        return "fisthip"

    Vicky.hovered_pose = hovered_pose

    def unhovered_pose(self):
        return "handhip"

    Vicky.unhovered_pose = unhovered_pose

    def face_pose(self, pose):
        if pose == "fisthip":
            return "fisthip"
        return pose

    Vicky.face_pose = face_pose

    def face_adjustment(self, face):
        if face == "aroused":
            return "flirty"
        return face

    Vicky.face_adjustment = face_adjustment

    leftover_mod_vicky_old_decide_default_location = Vicky.decide_default_location

    def decide_default_location(self):
        if "vicky_fondle_scene" in store.scenes_completed:
            self.place_and_set_scene(vicky_apartment)

        return

    Vicky.decide_default_location = decide_default_location

    def conversation_max(self):
        return 5

    Vicky.conversation_max = conversation_max

    def add_conversations_to_pool(self):
        self.test_and_add_conversation_to_pool(conversation_name = "vicky_convo_1")
        self.test_and_add_conversation_to_pool(conversation_name = "vicky_convo_2")
        self.test_and_add_conversation_to_pool(conversation_name = "vicky_convo_3")
        self.test_and_add_conversation_to_pool(conversation_name = "vicky_convo_4")
        self.test_and_add_conversation_to_pool(conversation_name = "vicky_convo_5")

        return

    Vicky.add_conversations_to_pool = add_conversations_to_pool

    def decide_priority_scene(self):

        return

    Vicky.decide_priority_scene = decide_priority_scene

    def xp_required_for_level(self, level):
        if not level or level == 1:
            return 0

        # julia underwear
        elif level == 2:
            return 3
        # julia topless
        elif level == 3:
            return 7
        # julia bottomless
        elif level == 4:
            return 11
        # julia nude
        elif level == 5:
            return 15
        elif level == 6:
            return 19
        elif level == 7:
            return 23
        elif level == 8:
            return 27
        elif level == 9:
            return 31
        elif level == 10:
            return 34

        return 999999999

    Vicky.xp_required_for_level = xp_required_for_level

    def relationship_level_cap(self):
        return 10

    Vicky.relationship_level_cap = relationship_level_cap

# Will be updated with the new character #
#    def available_minigames(self):
#        minigame_call_labels = []
#        minigame_call_labels.append("minigame_unknown")
#        minigame_call_labels.append("minigame_reading")

#        return minigame_call_labels

#    Vicky.available_minigames = available_minigames

    def boldness_level_required_for_scene(self, scene_name):
        if scene_name == "vicky_titjob_scene":
            return 7
        if scene_name == "vicky_scene_vaginal":
            return 8
        if scene_name == "vicky_scene_anal":
            return 8

            return 0

    Vicky.boldness_level_required_for_scene = boldness_level_required_for_scene

    def should_appear_in_gallery(self):
        return True

    Vicky.should_appear_in_gallery = should_appear_in_gallery

    def gallery_bust_art_default_pose(self):
        return "handhip"

    Vicky.gallery_bust_art_default_pose = gallery_bust_art_default_pose

    def gallery_bust_art_poses(self):
        return ["handhip", "fisthip", "handup"]

    Vicky.gallery_bust_art_poses = gallery_bust_art_poses

    def gallery_bust_art_faces(self):
        faces = IA_Actor.gallery_bust_art_faces(self)
        faces.extend(["surprised"])
        return faces

    Vicky.gallery_bust_art_faces = gallery_bust_art_faces

    def gallery_bust_art_outfits(self):
        outfits = ["clothesjacket", "clothes"]

        if "vicky_tease_scene" in store.scenes_completed:
            outfits.extend(["underwear"])

        if "vicky_titjob_scene" in store.scenes_completed:
            outfits.extend(["topless"])

        if "vicky_scene_blowjob" in store.scenes_completed:
            outfits.extend(["bottomless"])

        if "vicky_scene_vaginal" in store.scenes_completed:
            outfits.extend(["nude"])

        return outfits

    Vicky.gallery_bust_art_outfits = gallery_bust_art_outfits

    def gallery_bust_art_can_be_shown(self):
        return store.had_vicky_intro_scene

    Vicky.gallery_bust_art_can_be_shown = gallery_bust_art_can_be_shown

    def show_scene_completion_only_on_stats(self):
        return False

    Vicky.show_scene_completion_only_on_stats = show_scene_completion_only_on_stats

## Kacey ##
init 100 python:
    def has_location_navigation_icon(self):
        return True

    Gloryhole_Girl.has_location_navigation_icon = has_location_navigation_icon

    def use_character_select(self):
        return True

    Gloryhole_Girl.use_character_select = use_character_select

    def default_outfit(self):
        if store.finale_scene_completed_with_julia_sam:
            return "nude"

        if "finale_scene" in store.scenes_completed and self in store.kacey_apartment.character_list() and len(store.kacey_apartment.character_list()) == 1:
            return "nude"

        if "gloryhole_scene_stall" in store.scenes_completed and self in store.park.character_list() and len(store.park.character_list()) == 1:
            return "nude"

        if (not self.scene or self.play_scene_even_with_prompted_scene) and "gloryhole_scene_vaginal" in store.scenes_completed and self in store.kacey_apartment.character_list() and len(store.kacey_apartment.character_list()) == 1:
            return "topless"

        if (not self.scene or self.play_scene_even_with_prompted_scene) and "gloryhole_scene_blowjob" in store.scenes_completed and self in store.kacey_apartment.character_list() and len(store.kacey_apartment.character_list()) == 1:
            return "underwear"

        return "clothes"

    Gloryhole_Girl.default_outfit = default_outfit

    def default_pose(self):
        return "handsfront"

    Gloryhole_Girl.default_pose = default_pose

    def hovered_outfit(self):
        return self.default_outfit()

    Gloryhole_Girl.hovered_outfit = hovered_outfit

    def unhovered_outfit(self):
        return self.default_outfit()

    Gloryhole_Girl.unhovered_outfit = unhovered_outfit

    def hovered_pose(self):
        return "handface"

    Gloryhole_Girl.hovered_pose = hovered_pose

    def unhovered_pose(self):
        return "handsfront"

    Gloryhole_Girl.unhovered_pose = unhovered_pose

    def face_pose(self, pose):
        if pose == "handface":
            return "handface"
        return pose

    Gloryhole_Girl.face_pose = face_pose

    def face_adjustment(self, face):
        if face == "aroused":
            return "flirty"
        return face

    Gloryhole_Girl.face_adjustment = face_adjustment

    def decide_default_location(self):
        if store.week.time == "night":
            self.place_and_set_scene(location = park)
        else:
            if store.week.time == "day" and store.had_kacey_apartment_intro:
                self.place_and_set_scene(location = kacey_apartment)
        return

    Gloryhole_Girl.decide_default_location = decide_default_location

    def decide_normal_scene(self):
        self.place_and_set_scene(park, scene_name = "gloryhole_handjob_scene")

        if store.week.time == "night" and "gloryhole_handjob_scene" in store.scenes_completed and store.stats.boldness_level >= 5:
            self.place_and_set_scene(park, scene_name = "gloryhole_scene_blowjob")

        if store.week.time == "night" and "gloryhole_scene_blowjob" in store.scenes_completed and store.stats.boldness_level >= 6:
            self.place_and_set_scene(park, scene_name = "gloryhole_scene_vaginal")

        if store.week.time == "night" and "gloryhole_scene_vaginal" in store.scenes_completed and store.stats.boldness_level >= 7:
            self.place_and_set_scene(park, scene_name = "gloryhole_scene_anal")

        if store.week.time == "night" and "gloryhole_scene_anal" in store.scenes_completed and store.stats.boldness_level >= 8:
            self.place_and_set_scene(park, scene_name = "gloryhole_scene_stall")

        if week.time == "day" and store.had_kacey_apartment_intro and not "kacey_scene_minigame_intro" in store.scenes_completed:
            self.place_and_set_scene(kacey_apartment, scene_name = "kacey_scene_minigame_intro", override_scene_limit = True, is_conversation = True)

        return

    Gloryhole_Girl.decide_normal_scene = decide_normal_scene

    def conversation_max(self):
        return 4

    Gloryhole_Girl.conversation_max = conversation_max

    def kacey_add_conversations_to_pool(self):
        # no conversations if the apartment intro hasn't been done or she's not at her apartment.

        if not store.stats.current_location:
            return
        if not store.had_kacey_apartment_intro or store.gloryhole_girl not in store.kacey_apartment.characters:
            return

        self.test_and_add_conversation_to_pool(conversation_name = "gloryhole_girl_convo_1")
        self.test_and_add_conversation_to_pool(conversation_name = "gloryhole_girl_convo_2")
        self.test_and_add_conversation_to_pool(conversation_name = "gloryhole_girl_convo_3")
        self.test_and_add_conversation_to_pool(conversation_name = "gloryhole_girl_convo_4")

        return

    Gloryhole_Girl.add_conversations_to_pool = kacey_add_conversations_to_pool

    old_kacey_revisitable_scene_choice_label = Gloryhole_Girl.revisitable_scene_choice_label

    def kacey_revisitable_scene_choice_label(self, scene_name):
        # if kacey is at apartment, can't revisit
        if store.gloryhole_girl in store.kacey_apartment.characters:
            return ""

        return old_kacey_revisitable_scene_choice_label(self, scene_name)

    Gloryhole_Girl.revisitable_scene_choice_label = kacey_revisitable_scene_choice_label

    def kacey_decide_priority_scene(self):

        return

    Gloryhole_Girl.decide_priority_scene = kacey_decide_priority_scene

    def xp_required_for_level(self, level):
        if not level or level == 1:
            return 0

        # julia underwear
        elif level == 2:
            return 3
        # julia topless
        elif level == 3:
            return 7
        # julia bottomless
        elif level == 4:
            return 11
        # julia nude
        elif level == 5:
            return 15
        elif level == 6:
            return 19
        elif level == 7:
            return 23
        elif level == 8:
            return 27
        elif level == 9:
            return 31
        elif level == 10:
            return 34

        return 999999999

    Gloryhole_Girl.xp_required_for_level = xp_required_for_level

    def relationship_level_cap(self):
        return 10

    Gloryhole_Girl.relationship_level_cap = relationship_level_cap

    def available_minigames(self):
        minigame_call_labels = []

        if store.gloryhole_girl not in store.kacey_apartment.characters:
            return []

        if "kacey_scene_minigame_intro" in store.scenes_completed:
            minigame_call_labels.append("minigame_table_tennis")

        return minigame_call_labels

    Gloryhole_Girl.available_minigames = available_minigames

#    def decide_low_priority_scene(self):
#        if store.had_kacey_apartment_intro and store.week.time == "day" and store.stats.current_location == store.kacey_apartment:
#            self.place_and_set_scene(scene_name = "kacey_scene_minigame_intro", override_scene_limit = True, is_conversation = True, is_low_priority = True)
#        return

#    Gloryhole_Girl.decide_low_priority_scene = decide_low_priority_scene

    def boldness_level_required_for_scene(self, scene_name):
        if scene_name == "gloryhole_scene_vaginal":
            return 7
        if scene_name == "gloryhole_scene_stall":
            return 8

            return 0

    Gloryhole_Girl.boldness_level_required_for_scene = boldness_level_required_for_scene

    def should_appear_in_gallery(self):
        return True

    Gloryhole_Girl.should_appear_in_gallery = should_appear_in_gallery

    def gallery_bust_art_default_pose(self):
        return "handsfront"

    Gloryhole_Girl.gallery_bust_art_default_pose = gallery_bust_art_default_pose

    def gallery_bust_art_poses(self):
#       return ["handhip", "handturn", "handface"]
        return ["handsfront", "handface", "leaning"]

    Gloryhole_Girl.gallery_bust_art_poses = gallery_bust_art_poses

    def gallery_bust_art_faces(self):
        faces = IA_Actor.gallery_bust_art_faces(self)
        faces.extend(["surprised"])
        return faces

    Gloryhole_Girl.gallery_bust_art_faces = gallery_bust_art_faces

    def gallery_bust_art_outfits(self):
        outfits = ["clothes"]

        if "gloryhole_scene_blowjob" in store.scenes_completed:
            outfits.extend(["underwear"])

        if "gloryhole_scene_vaginal" in store.scenes_completed:
            outfits.extend(["topless"])

        if "gloryhole_scene_anal" in store.scenes_completed:
            outfits.extend(["bottomless"])

        if "gloryhole_scene_stall" in store.scenes_completed:
            outfits.extend(["nude"])

        return outfits

    Gloryhole_Girl.gallery_bust_art_outfits = gallery_bust_art_outfits

    def gallery_bust_art_can_be_shown(self):
        return "gloryhole_scene_stall" in store.scenes_completed

    Gloryhole_Girl.gallery_bust_art_can_be_shown = gallery_bust_art_can_be_shown

    def show_scene_completion_only_on_stats(self):
        return False

    Gloryhole_Girl.show_scene_completion_only_on_stats = show_scene_completion_only_on_stats

    def has_separate_glasses(self):
        return True

    def display_bust_art_in_character_menu(self):
        return True

    Gloryhole_Girl.display_bust_art_in_character_menu = display_bust_art_in_character_menu

## Julia ##
init 100 python:
    # record the old version of the function so we can use it later
    leftovers_mod_julia_old_outfits = Julia.gallery_bust_art_outfits

    # make a new function that uses the old function and then adds an outfit to the array
    def leftovers_mod_julia_new_outfits(self):
        outfits = leftovers_mod_julia_old_outfits(self)
        if "julia_scene_swimsuit" in scenes_completed:
            outfits.append("swimsuit")

        return outfits

    # replace Julia's gallery outfit function with the new one
    Julia.gallery_bust_art_outfits = leftovers_mod_julia_new_outfits

    def fix_appearance(self):
        if self.outfit == "bikini":
            self.outfit = "swimsuit"

        return

    Julia.fix_appearance = fix_appearance

    def default_outfit(self):
        if store.finale_scene_completed_with_julia_sam:
            return "nude"

        if store.stats.current_zone == store.home and store.has_fucked_everyone_in_home:
            return "nude"

        if (not self.scene or self.play_scene_even_with_prompted_scene) and "julia_scene_anal" in store.scenes_completed and self in store.bathroom.character_list() and len(store.bathroom.character_list()) == 1:
            return "nude"

        if store.week.time == "day" and "julia_scene_swimsuit" in store.scenes_completed and (not self.scene or self.play_scene_even_with_prompted_scene) and self in store.backyard.character_list() and len(store.backyard.character_list()) == 1:
            return "swimsuit"

        return "clothes"

    Julia.default_outfit = default_outfit

    def decide_default_location(self):
        if not store.had_julia_arrived_scene:
            return

        if "julia_scene_anal" in store.scenes_completed and daily_random_event_coin_toss("julia_bathroom"):
            self.place_and_set_scene(bathroom)
        elif store.week.time == "day" and "julia_scene_swimsuit" in store.scenes_completed and daily_random_event_coin_toss("julia_swimsuit"):
            self.place_and_set_scene(backyard)

        self.place_and_set_scene(living_room)

        if store.week.time == "day" and "julia_scene_swimsuit" in store.scenes_completed and daily_random_event_coin_toss("julia_swimsuit"):
            self.place_and_set_scene(backyard)
        else:
            self.place_and_set_scene(living_room)

        return

    Julia.decide_default_location = decide_default_location

    # record the old version of the function so we can use it later
    leftovers_mod_julia_old_list_of_main_scenes = Julia.list_of_main_scenes

    # make a new function that uses the old function and then adds an outfit to the array
    def leftovers_mod_julia_new_list_of_main_scenes(self):
        scenes = leftovers_mod_julia_old_list_of_main_scenes(self)
        scenes.append("julia_scene_swimsuit")
        return scenes

    # replace Julia's gallery outfit function with the new one
    Julia.list_of_main_scenes = leftovers_mod_julia_new_list_of_main_scenes

    def replayable_scene_choice_label(self, scene_name):
        if scene_name == "julia_scene_underwear":
            return "When [julia.say_name] came into my room asking for a pillow..."
        if scene_name == "julia_scene_topless":
            return "When I saw [julia.say_name] without her top in [sa.say_name]'s room..."
        if scene_name == "julia_scene_bottomless":
            return "When I saw [julia.say_name] in the hallway without her pants on..."
        if scene_name == "julia_scene_swimsuit":
            return "When I bought a swimsuit for " + julia.say_name + "..."
        if scene_name == "julia_scene_nude":
            return "When [julia.say_name] came out of the shower..."
        if scene_name == "julia_scene_footjob":
            return "When [julia.say_name] rubbed my penis with her feet..."
        if scene_name == "julia_scene_blowjob":
            return "When [julia.say_name] sucked on my penis..."
        if scene_name == "julia_scene_vaginal":
            return "That time [julia.say_name] wanted me to fuck her..."
        if scene_name == "julia_scene_anal":
            return "That time I fucked [julia.say_name] in the ass..."
        if scene_name == "sam_julia_threesome_scene":
            return "When [julia.say_name] and [sa.say_name] fucked me at the same time..."

        return ""

    Julia.replayable_scene_choice_label = replayable_scene_choice_label

    def revisitable_scene_choice_label(self, scene_name):
        if scene_name == "julia_scene_footjob_revisit":
            if "julia_scene_footjob_revisit" not in scenes_completed:
                return "Can you rub my penis with your feet again?"
            else:
                return "Would you like to give me a footjob again?"

        if scene_name == "julia_scene_blowjob_revisit":
            if "julia_scene_blowjob_revisit" not in scenes_completed:
                return "Could you suck my dick [julia.say_name]?"
            else:
                return "Would you like to give me another blowjob?"

        if scene_name == "julia_scene_vaginal_revisit":
            if "julia_scene_vaginal_revisit" not in scenes_completed:
                return "Want me to fuck you again [julia.say_name]?"
            else:
                return "I'm ready to fuck again!"

        if scene_name == "julia_scene_anal_revisit":
            if "julia_scene_anal_revisit" not in scenes_completed:
                return "You up for some anal again [julia.say_name]?"
            else:
                return "I'm ready for another anal fuck with you [julia.say_name]!"

        if persistent.see_incomplete_leftovers:
            if scene_name == "julia_scene_swimsuit_revisit":
                if "julia_scene_swimsuit_revisit" in scenes_completed:
                    if "julia_scene_swimsuit_revisit_first_time_has_done_vaginal" in scenes_completed:
                        return "I'm ready to fuck besides the pool again!"
                    elif "julia_scene_swimsuit_revisit_first_time_has_done_grinding" in scenes_completed:
                        return "Wanna relax by the pool again?"
                    else:
                        return "You up for relaxing by the pool today?"

                return "We should relax by the pool today!"

        if scene_name == "sam_julia_threesome_scene_revisit_julia":
            return "Want to join [sa.say_name] and I for some sex [julia.say_name]?"

        return ""

    Julia.revisitable_scene_choice_label = revisitable_scene_choice_label

# leftover code for overriding methods
#    # record the old version of the function so we can use it later
#    leftovers_mod_julia_old_gallery_images = Julia.gallery_images

    # make a new function that uses the old function and then adds an outfit to the array
#    def leftovers_mod_julia_swimsuit_gallery_images(self):
#        images = leftovers_mod_julia_old_gallery_images(self)
#        if "julia_scene_swimsuit" in scenes_completed:
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_read.png")

#        if "julia_scene_swimsuit" in scenes_completed and "julia_scene_footjob" in scenes_completed:
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_vaginal_reveal.png")

#        if "julia_scene_swimsuit_revisit_first_time_vaginal" in scenes_completed and "julia_scene_vaginal" in scenes_completed:
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_vaginal_reveal_nude.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_fuck.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_fuck_nude.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_fuck_blur.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_fuck_blur_nude.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_cum_blur.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_cum_blur_nude.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_aftercum.png")
#            images.append("mods/leftovers_mod/images/bg/julia/julia_swimsuit/bg julia_swimsuit_aftercum_nude.png")

#        return images

    # replace Julia's gallery outfit function with the new one
#    Julia.gallery_images = leftovers_mod_julia_swimsuit_gallery_images

## Kacey and Vicky Renaming ##
init 500 python:
    config.label_overrides["nate_room_rename_characters"] = "nate_room_rename_characters_kacey_vicky"

label nate_room_rename_characters_kacey_vicky:
    $ renpy.scene('screens')

    $ process_character(si, "position right")
    call change_character_name(si, _("My Mom"))

    $ clear_characters()
    $ process_character(k, "position right")
    call change_character_name(k, _("My big sis"))

    $ clear_characters()
    $ process_character(sa, "position right")
    call change_character_name(sa, _("My twin sister"))

    if had_julia_arrived_scene:
        $ clear_characters()
        $ process_character(julia, "position right")
        call change_character_name(julia, _("My cousin"))

    if had_janet_intro_scene:
        $ clear_characters()
        $ process_character(janet, "position right")
        call change_character_name(janet, _("My Aunt"))

    if had_edna_intro_scene:
        $ clear_characters()
        $ process_character(edna, "position right")
        call change_character_name(edna, _("My Grandma"))

    if had_vicky_intro_scene:
        $ clear_characters()
        $ process_character(vicky, "position right")
        call change_character_name(vicky, _("My Business Partner"))

    if "gloryhole_scene_stall" in store.scenes_completed:
        $ clear_characters()
        $ process_character(gloryhole_girl, "position right")
        call change_character_name(gloryhole_girl, _("My Park Friend"))

    $ clear_characters()
    $ process_character(n, "position right")
    call change_character_name(n, _("My name"))

    python:
        last_name = renpy.input(_("My last name"), default = last_name, length = 14)

    call update_last_names
    $ clear_characters()

    call nate_room_empty

    return

## Vicky/Kacey Talk ##
default vicky_disable_talk_intro = False
default kacey_disable_talk_intro = False

init 100 python:
    def vicky_menu_character_select_renpy_label(self):
        return "vicky_character_menu_leftovers"

    def vicky_display_menu(self):
        renpy.call("vicky_character_menu_leftovers")
        return

    Vicky.display_menu = vicky_display_menu

    def kacey_menu_character_select_renpy_label(self):
        return "kacey_character_menu_leftovers"

    def kacey_display_menu(self):
        renpy.call("kacey_character_menu_leftovers")
        return

    Gloryhole_Girl.display_menu = kacey_display_menu

# there's no need to have the character parameter in the ().
# we already know it's vicky
label vicky_character_menu_leftovers:
    call process_scene_beginning(bg = "bg vicky_sit_smile")

    if not vicky_disable_talk_intro:
        vicky.c "Hello [n.say_name]!"
        vicky.c "Have a seat, make yourself comfortable!"
        vicky.c "So, what's on your mind?"

    $ vicky_disable_talk_intro = False
    $ no_bust_art = True

    call character_menu(vicky, draw_characters = False)

    return

label kacey_character_menu_leftovers:
    if store.week.time == "day" and store.had_kacey_apartment_intro and store.stats.current_location and store.stats.current_location == store.kacey_apartment:
        call process_scene_beginning(bg = "bg kacey_apartment_daytime")
    else:
        call process_scene_beginning(bg = "bg gloryhole")
        $ kacey_disable_talk_intro = False

    if not kacey_disable_talk_intro:
        if store.week.time == "day" and store.had_kacey_apartment_intro and store.stats.current_location and store.stats.current_location == store.kacey_apartment:
            call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
            gloryhole_girl.c "[n.say_name]!"

            call process_character(gloryhole_girl, appearance = "pose handface face happy blush false")
            gloryhole_girl.c "I'm so glad you could make it!"

            call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
            gloryhole_girl.c "Go on, make yourself comfortable!"

            call process_character(gloryhole_girl, appearance = "pose handsfront face neutral blush false")
            gloryhole_girl.c "So, what's up?"

            $ kacey_disable_talk_intro = False

            call character_menu(gloryhole_girl, draw_characters = True)
        else:
            if not kacey_disable_talk_intro:
                n.c "You there [gloryhole_girl.say_name]?"
                gloryhole_girl.c "[n.say_name]!"
                gloryhole_girl.c "Back again!"
                gloryhole_girl.c "So, you want another round of fun?"

            $ kacey_disable_talk_intro = False

            if "gloryhole_scene_stall" in store.scenes_completed:
                $ no_bust_art = False

                call character_menu(gloryhole_girl, draw_characters = True)
            else:
                $ no_bust_art = True

                call character_menu(gloryhole_girl, draw_characters = False)
    else:
        call character_menu(gloryhole_girl, draw_characters = False)

    return

## Sam Twinsticks Hat + Edna Hat ##
init 100 python:
    def has_separate_hat(self):
        return True

    Sam.has_separate_hat = has_separate_hat

    leftovers_mod_sam_default_hat_old = Sam.default_hat

    def leftovers_mod_sam_default_hat_new(self):
        if getattr(store, 'sam_impreg', False) and store.week.time == "night" and store.stats.current_location and store.stats.current_location == store.sam_room:
            if daily_random_event_coin_toss("sam hat"):
                return "TwinSticks"

        return leftovers_mod_sam_default_hat_old(self)

    Sam.default_hat = leftovers_mod_sam_default_hat_new

    def gallery_hat_list(self):
        return ["", "TwinSticks"]

    Sam.gallery_hat_list = gallery_hat_list

    def has_separate_hat(self):
        return True

# 17/02/25 Fix for Sam's Twinstick Hat in the Bust Art Gallery
init 100 python:
    leftovers_mod_sam_hat_image_filename_old = Sam.hat_image_filename

    def leftovers_mod_sam_hat_image_filename_new(self):
        filename = leftovers_mod_sam_hat_image_filename_old(self)

        if self.position in ["left"] and self.hat == "TwinSticks":
            filename = filename.replace("TwinSticks", "TwinSticks_Mirror")
        elif self.position in ["right"] and self.hat == "TwinSticks":
            filename = filename.replace("TwinSticks_Mirror", "TwinSticks")

        return filename

    Sam.hat_image_filename = leftovers_mod_sam_hat_image_filename_new

    Edna.has_separate_hat = has_separate_hat

    leftovers_mod_edna_default_hat_old = Edna.default_hat

    def leftovers_mod_edna_default_hat_new(self):
        if "edna_scene_topless" in store.scenes_completed and store.week.time == "day" and self in store.edna_house.character_list() and len(store.edna_house.character_list()) == 1 and store.stats.current_location and store.stats.current_location == store.edna_house:
            if daily_random_event_coin_toss("edna hat"):
                return "sunhat"

        return leftovers_mod_edna_default_hat_old(self)

    Edna.default_hat = leftovers_mod_edna_default_hat_new

    def gallery_hat_list(self):
        return ["", "sunhat"]

    Edna.gallery_hat_list = gallery_hat_list
##########################################
