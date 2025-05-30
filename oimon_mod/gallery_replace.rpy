## Sam ##
init 5 python:
    oimon_original_sam_gallery_images = Sam.gallery_images

    # modular edit of a function in gallery.rpy
    old_character_gallery_fullscreen_oimon_sam = character_gallery_fullscreen

    def character_gallery_fullscreen(gallery_image, gallery_char, gallery_char_page):
        # if the thumbnail is the oimon thumbnail, it will lead to the proper animation
        if "sam_dream_anim_oimon_0" in gallery_image:
            gallery_image = "sam_dream_anim_oimon"

        old_character_gallery_fullscreen_oimon_sam(gallery_image, gallery_char, gallery_char_page)
        return

    def oimon_new_sam_gallery_images(self):
        gallery_images = oimon_original_sam_gallery_images(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Sam_1 #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/sam/sam_1/bg sam_1_sam_playing_nip_slip.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_1/bg sam_1_sam_playing_nip_slip_oimon.png"
                if original_image == "images/bg/sam/sam_1/bg sam_1_sam_playing_nip_zoom.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_1/bg sam_1_sam_playing_nip_zoom_oimon.png"

            # Sam_3 #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/sam/sam_3/bg sam_3_touch_eachother.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_3/bg sam_3_touch_eachother_oimon.png"
                if original_image == "images/bg/sam/sam_3/bg sam_3_kiss.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_3/bg sam_3_kiss_oimon.png"
                if original_image == "images/bg/sam/sam_3/bg sam_3_kiss_on_bed.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_3/bg sam_3_kiss_on_bed_oimon.png"
                if original_image == "images/bg/sam/sam_3/bg sam_3_grind.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_3/bg sam_3_grind_oimon.png"
                if original_image == "images/bg/sam/sam_3/bg sam_3_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_3/bg sam_3_cum_oimon.png"
                if original_image == "images/bg/sam/sam_3/bg sam_3_plays_with_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_3/bg sam_3_plays_with_cum_oimon.png"

            # Sam_Vaginal #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/sam/sam_vaginal/bg sam_vaginal_spread.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_vaginal/bg sam_vaginal_spread_oimon.png"
                if original_image == "images/bg/sam/sam_vaginal/bg sam_vaginal_spread_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_vaginal/bg sam_vaginal_spread_cum_oimon.png"

            # Sam_BJ #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/sam/sam_bj/bg sam_bj_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_bj/bg sam_bj_cum_oimon.png"

            # Sam_Anal #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/sam/sam_anal/bg sam_anal.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_anal/bg sam_anal_oimon.png"
                if original_image == "images/bg/sam/sam_anal/bg sam_anal_blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_anal/bg sam_anal_blur_oimon.png"
                if original_image == "images/bg/sam/sam_anal/bg sam_anal_cum_blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_anal/bg sam_anal_cum_blur_oimon.png"
                if original_image == "images/bg/sam/sam_anal/bg sam_anal_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_anal/bg sam_anal_cum_oimon.png"

            # Sam_Swimsuit #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_jump_in_nude.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_jump_in_nude_oimon.png"
                if original_image == "images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_nude.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_nude_oimon.png"
                if original_image == "images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_nude_blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_nude_blur_oimon.png"
                if original_image == "images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_nude_blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_nude_blur_oimon.png"
                if original_image == "images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_nude.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_nude_oimon.png"

            # Sam_Dream #
            if persistent.oimon_mod_enabled:
                if original_image == "images/animations/sam dream/sam_dream_anim_0.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/animations/sam dream/sam_dream_anim_oimon_0.png"
                if original_image == "images/bg/sam/sam_dream/bg sam_dream_Nonates.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_dream/bg sam_dream_NoNates_oimon.png"
                if original_image == "images/bg/sam/sam_dream/bg sam_dream_Nate1_appear.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_dream/bg sam_dream_Nate1_appear_oimon.png"
                if original_image == "images/bg/sam/sam_dream/bg sam_dream_Nate2_appear.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/sam/sam_dream/bg sam_dream_Nate2_appear_oimon.png"

        return gallery_images

    Sam.gallery_images = oimon_new_sam_gallery_images

## Julia ##
# override class method #
    def oimon_new_julia_gallery_thumbnail(self):
        if persistent.oimon_mod_enabled == True:
            return "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_Footjob_Soft_oimon.png"
        else:
            return "images/bg/julia/JuliaFootjob/bg Julia_Footjob_Soft.png"

    Julia.gallery_thumbnail = oimon_new_julia_gallery_thumbnail

init 5 python:
    oimon_original_julia_gallery_images = Julia.gallery_images

    def oimon_new_julia_gallery_images(self):
        gallery_images = oimon_original_julia_gallery_images(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # JuliaFootjob #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_Footjob_Soft.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_Footjob_Soft_oimon.png"
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_Footjob_HardForeskin_NoBlur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_Footjob_HardForeskin_NoBlur_oimon.png"
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_Footjob_HardForeskin_Blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_Footjob_HardForeskin_Blur_oimon.png"
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_Footjob_Hard_NoBlur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_Footjob_Hard_NoBlur_oimon.png"
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_Footjob_Hard_Blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_Footjob_Hard_Blur_oimon.png"
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_FootjobCum_Hard_Blur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_FootjobCum_Hard_Blur_oimon.png"
                if original_image == "images/bg/julia/JuliaFootjob/bg Julia_FootjobAfterCum_Hard_NoBlur.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaFootjob/bg Julia_FootjobAfterCum_Hard_NoBlur_oimon.png"

            # JuliaBlowjob #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_Table.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/JuliaBlowjob/bg Julia_Blowjob_Table_oimon.png"

            # Julia Vaginal #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/julia/Julia Vaginal/bg Julia_Fuck_Tip.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Vaginal/bg Julia_Fuck_Tip_oimon.png"
                if original_image == "images/bg/julia/Julia Vaginal/bg Julia_Fuck_Tip_Xray.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Vaginal/bg Julia_Fuck_Tip_Xray_oimon.png"
                if original_image == "images/bg/julia/Julia Vaginal/bg Julia_Fuck__AfterCum_Nate.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Vaginal/bg Julia_Fuck__AfterCum_Nate_oimon.png"
                if original_image == "images/bg/julia/Julia Vaginal/bg Julia_Fuck__AfterCum_Nate_Xray.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Vaginal/bg Julia_Fuck__AfterCum_Nate_Xray_oimon.png"
                if original_image == "images/bg/julia/Julia Vaginal/bg Julia_Fuck_AfterCum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Vaginal/bg Julia_Fuck_AfterCum_oimon.png"

            # Julia Anal #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/julia/Julia Anal/bg Julia_Anal_Onfloor.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Anal/bg Julia_Anal_Onfloor_oimon.png"
                if original_image == "images/bg/julia/Julia Anal/bg Julia_Anal_Fuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Anal/bg Julia_Anal_Fuck_oimon.png"
                if original_image == "images/bg/julia/Julia Anal/bg Julia_Anal_Fuck_Cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Anal/bg Julia_Anal_Fuck_Cum_oimon.png"
                if original_image == "images/bg/julia/Julia Anal/bg Julia_Anal_Fuck_CumInside.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Anal/bg Julia_Anal_Fuck_CumInside_oimon.png"
                if original_image == "images/bg/julia/Julia Anal/bg Julia_Anal_AfterCum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/julia/Julia Anal/bg Julia_Anal_AfterCum_oimon.png"

        return gallery_images

    Julia.gallery_images = oimon_new_julia_gallery_images

## Group ##
init 100 python:
    oimon_original_sam_simone_threesome_images = IA_Actor.sam_simone_threesome_images

    def oimon_new_sam_simone_threesome_images(self):
        gallery_images = oimon_original_sam_simone_threesome_images(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Sam_Simone_Group #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_watches.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_watches_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_licked.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_licked_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_fuck_simone.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_fuck_simone_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_fuck_sam.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_fuck_sam_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_simone.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_simone_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_sam.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_sam_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_simone.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_simone_oimon.png"
                if original_image == "images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_sam.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_sam_oimon.png"

        return gallery_images

    IA_Actor.sam_simone_threesome_images = oimon_new_sam_simone_threesome_images

init 100 python:
    oimon_original_sam_julia_threesome_images = IA_Actor.sam_julia_threesome_images

    def oimon_new_sam_julia_threesome_images(self):
        gallery_images = oimon_original_sam_julia_threesome_images(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Sam_Julia_Group #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_grind.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_grind_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_stackup.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_stackup_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_SamFuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_cum_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_cum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_cum_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_cum_JuliaCum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_cum_JuliaCum_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_cum_SamCum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_cum_SamCum_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_stackup_samcum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_stackup_samcum_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_stackup_juliacum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_stackup_juliacum_oimon.png"
                if original_image == "images/bg/others/sam_julia_group/bg julia_sam_group_stackup_bothcum.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/sam_julia_group/bg julia_sam_group_stackup_bothcum_oimon.png"

        return gallery_images

    IA_Actor.sam_julia_threesome_images = oimon_new_sam_julia_threesome_images

init 100 python:
    oimon_original_foursome_images_kira = IA_Actor.foursome_images_kira

    def oimon_new_foursome_images_kira(self):
        gallery_images = oimon_original_foursome_images_kira(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Foursome_Images_Kira #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck_oimon.png"

        return gallery_images

    IA_Actor.foursome_images_kira = oimon_new_foursome_images_kira

init 100 python:
    oimon_original_foursome_images_simone = IA_Actor.foursome_images_simone

    def oimon_new_foursome_images_simone(self):
        gallery_images = oimon_original_foursome_images_simone(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Foursome_Images_Simone #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck_oimon.png"

        return gallery_images

    IA_Actor.foursome_images_simone = oimon_new_foursome_images_simone

init 100 python:
    oimon_original_foursome_images_sam = IA_Actor.foursome_images_sam

    def oimon_new_foursome_images_sam(self):
        gallery_images = oimon_original_foursome_images_sam(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Foursome_Images_Sam #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck_oimon.png"

        return gallery_images

    IA_Actor.foursome_images_sam = oimon_new_foursome_images_sam

init 100 python:
    oimon_original_foursome_images_all = IA_Actor.foursome_images_all

    def oimon_new_foursome_images_all(self):
        gallery_images = oimon_original_foursome_images_all(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Foursome_Images_All #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck_oimon.png"

        return gallery_images

    IA_Actor.foursome_images_all = oimon_new_foursome_images_all

init 100 python:
    oimon_original_finale_images = IA_Actor.finale_images

    def oimon_new_finale_images(self):
        gallery_images = oimon_original_finale_images(self)

        for i in range(len(gallery_images)):
            original_image = gallery_images[i]

            # Finale Scene #
            if persistent.oimon_mod_enabled:
                if original_image == "images/bg/others/Finale Scene/bg party_Sam.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/Finale Scene/bg party_Sam_oimon.png"

                if original_image == "images/bg/others/Finale Scene/bg party_Julia.png":
                    gallery_images[i] = "mods/leftovers_mod/images/oimon_mod/bg/others/Finale Scene/bg party_Julia_oimon.png"

        return gallery_images

    IA_Actor.finale_images = oimon_new_finale_images
