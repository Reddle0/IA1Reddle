# Debug #
init 999 python:
    config.label_overrides["debug_edna"] = "debug_edna_anim_mod"

label debug_edna_anim_mod:
    menu:
        "Edna Scenes":
            call debug_edna_scenes
        "Back":
            call debug_character
    return

# Animates Edna's BJ scene #
init python:
    def edna_blowjob_set_speed(label, is_revisit, dream = False):
        renpy.call(label, is_revisit, dream = dream)

        return

image edna_blowjob_anim:
    "edna_blowjob_anim_0"
    pause 0.09
    "edna_blowjob_anim_1"
    pause 0.09
    "edna_blowjob_anim_2"
    pause 0.09
    "edna_blowjob_anim_3"
    pause 0.09
    "edna_blowjob_anim_4"
    pause 0.09
    "edna_blowjob_anim_5"
    pause 0.09
    "edna_blowjob_anim_6"
    pause 0.09
    "edna_blowjob_anim_7"
    pause 0.09
    "edna_blowjob_anim_8"
    pause 0.09
    "edna_blowjob_anim_9"
    pause 0.09
    "edna_blowjob_anim_10"
    repeat

# Overrides Scenes #
#init 200 python:
#    config.label_overrides["vicky_scene_anal_sex"] = "vicky_scene_anal_sex_anim_mod"
#    config.label_overrides["vicky_scene_anal_revisit"] = "vicky_scene_anal_revisit_anim_mod"
#    config.label_overrides["vicky_scene_anal_revisit_1st_time"] = "vicky_scene_anal_revisit_1st_time_anim_mod"
#    config.label_overrides["vicky_scene_anal_revisit_2nd_time"] = "vicky_scene_anal_revisit_2nd_time_anim_mod"
#    config.label_overrides["vicky_scene_anal_revisit_end"] = "vicky_scene_anal_revisit_end_anim_mod"

init 200 python:
    anim_mod_edna_blowjob_old_gallery_images = Edna.gallery_images

    def anim_mod_edna_blowjob_gallery_images(self):
        images = anim_mod_edna_blowjob_old_gallery_images(self)

        if "edna_scene_blowjob" in scenes_completed:
            images.append("mods/leftovers_mod/images/anim_mod/animations/edna bj/edna_blowjob_anim_0.png")

        return images

    Edna.gallery_images = anim_mod_edna_blowjob_gallery_images

# Animation Class Info #
init 100 python:
    class IA_Animation_Edna_Blowjob_Info(IA_Animation_Info):
        def image_base_path(self):
            return "mods/leftovers_mod/images/anim_mod/animations/edna bj/"

        def image_name(self):
            return "edna_blowjob_anim"

        def section_data(self):
            return [ ( 0 , 11 ) ]

        def last_frame(self):
            return 10

        def frame_durations(self):
            return [0.09]

        def frame_duration_multiplier(self):
            return store.main_animation_speed

        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return [["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]
            return []

# Sets Animation Speeds #
init python:
    edna_blowjob_slow_speed_multiplier = 1.10
    edna_blowjob_fast_speed_multiplier = 0.75
    edna_blowjob_fastest_speed_multiplier = 0.5