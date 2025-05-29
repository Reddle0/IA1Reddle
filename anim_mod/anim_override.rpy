init offset = 99

#init 2 python:
#    reddle_sam_anim_mod_old_sam_scene_choice_list = Sam.scene_choice_list

#    def reddle_sam_anim_mod_new_sam_scene_choice_list(self):
#        choice_list = reddle_sam_anim_mod_old_sam_scene_choice_list(self)
#        new_choice_list = []

#        for choice in choice_list:
#            if choice[1] == "sam_scene_vaginal_revisit":
#                choice = (choice[0], "sam_scene_vaginal_revisit_anim_mod")
#            new_choice_list.append(choice)

#        return new_choice_list

#    Sam.scene_choice_list = reddle_sam_anim_mod_new_sam_scene_choice_list
# ^ Overrides Choice list in character menus for revisits/dreams ^ #

# Make it appear in the CG Gallery, fully animated upon click #
init 999 python:
    config.label_overrides["character_gallery_fullscreen"] = "character_gallery_fullscreen_anim_mod"

init 300 python:
    character_gallery_fullscreen_old = character_gallery_fullscreen

    def character_gallery_fullscreen_anim_mod(gallery_image, gallery_char, gallery_char_page):
        renpy.call("character_gallery_fullscreen_anim_mod", gallery_image, gallery_char, gallery_char_page)
        return

    character_gallery_fullscreen = character_gallery_fullscreen_anim_mod
## ^^ Way of overriding functions/definitions ##

label character_gallery_fullscreen_anim_mod(character_gallery_fullscreen_image, gallery_char, gallery_char_page):
    python:
        if "kira_titfuck_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_titfuck_anim_gallery"
        elif "kira_titfuck_anim_20" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_titfuck_anim_cum_gallery"
        elif "kira_3_buttjob_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_3_buttjob_anim"
        elif "kira_anal_anim_2" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_anal_anim"
        elif "simone_vaginal_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "simone_vaginal_anim"
        elif "sam_grind_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "sam_grind_anim"
        elif "sam_vaginal_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "sam_vaginal_anim"
        elif "sam_dream_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "sam_dream_anim"
        elif "julia_anal_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "julia_anal_anim"
        elif "janet_anal_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "janet_anal_anim"
        elif "edna_titfuck_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "edna_titfuck_bikini_anim"
        elif "edna_titfuck_nude_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "edna_titfuck_nude_anim"

    show screen character_gallery_fullscreen(character_gallery_fullscreen_image)
    pause
    call gallery_char_show(gallery_char, gallery_char_page)
    return
## ^^ Way of inserting in new animations in the CG Gallery ##
