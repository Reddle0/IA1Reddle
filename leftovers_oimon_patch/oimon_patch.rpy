## Sam_Simone_Group ##
image bg sam_simone_group_sprawl_cum_both_samangle = ConditionSwitch(
    "persistent.oimon_mod_enabled == True", "mods/leftovers_mod/images/leftovers_oimon_patch/sam_simone_group/bg sam_simone_group_sprawl_cum_both_samangle_oimon.png",
    "persistent.oimon_mod_enabled == False", "mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_both_samangle.png"
)

image bg sam_simone_group_sprawl_cum_both_simoneangle = ConditionSwitch(
    "persistent.oimon_mod_enabled == True", "mods/leftovers_mod/images/leftovers_oimon_patch/sam_simone_group/bg sam_simone_group_sprawl_cum_both_simoneangle_oimon.png",
    "persistent.oimon_mod_enabled == False", "mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_both_simoneangle.png"
)

image bg sam_simone_group_sprawl_aftercum_both = ConditionSwitch(
    "persistent.oimon_mod_enabled == True", "mods/leftovers_mod/images/leftovers_oimon_patch/sam_simone_group/bg sam_simone_group_sprawl_aftercum_both_oimon.png",
    "persistent.oimon_mod_enabled == False", "mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_both.png"
)

## Photo Epilogue Eye Glare Fix (v0.3d) ##
image bg photo_epilogue_samjulia_np = ConditionSwitch(
    "persistent.oimon_mod_enabled == True", "mods/leftovers_mod/images/leftovers_oimon_patch/Photo_Epilogue/bg photo_epilogue_samjulia_np_new_oimon.png",
    "persistent.oimon_mod_enabled == False", "mods/leftovers_mod/images/bg/others/Photo_Epilogue/bg photo_epilogue_samjulia_np_new.png"
)

## Gallery Fix ##
init 500 python:
    original_sam_simone_threesome_images = IA_Actor.sam_simone_threesome_images

    def leftovers_oimon_patch_sam_simone_threesome_images(self):
        gallery_images = original_sam_simone_threesome_images(self)
        if persistent.oimon_mod_enabled:
            for i in range(len(gallery_images)):
                original_image = gallery_images[i]

                # Sam_Simone_Group Cum_Both #
                if original_image == "mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_both_samangle.png":
                    gallery_images[i] = "mods/leftovers_mod/images/leftovers_oimon_patch/sam_simone_group/bg sam_simone_group_sprawl_cum_both_samangle_oimon.png"
                if original_image == "mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_both_simoneangle.png":
                    gallery_images[i] = "mods/leftovers_mod/images/leftovers_oimon_patch/sam_simone_group/bg sam_simone_group_sprawl_cum_both_simoneangle_oimon.png"
                if original_image == "mods/leftovers_mod/images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_both.png":
                    gallery_images[i] = "mods/leftovers_mod/images/leftovers_oimon_patch/sam_simone_group/bg sam_simone_group_sprawl_aftercum_both_oimon.png"

        return gallery_images

    IA_Actor.sam_simone_threesome_images = leftovers_oimon_patch_sam_simone_threesome_images
