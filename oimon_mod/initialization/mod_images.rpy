init 100 python:
    mod_image_folder_prefixes.append("mods/leftovers_mod/images/oimon_mod")

init 100 python:
    def oimon_new_sam_dream_image_base_path(self):
        if persistent.oimon_mod_enabled == True:
            return "mods/leftovers_mod/images/oimon_mod/animations/sam dream/"
        else:
            return "images/animations/sam dream/"

    IA_Animation_Sam_Dream_Info.image_base_path = oimon_new_sam_dream_image_base_path

    def oimon_new_sam_dream_image_name(self):
        if persistent.oimon_mod_enabled == True:
            return "sam_dream_anim_oimon"
        else:
            return "sam_dream_anim"

    IA_Animation_Sam_Dream_Info.image_name = oimon_new_sam_dream_image_name