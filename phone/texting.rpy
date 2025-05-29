# required to fix a visual issue with the phone
init 101 python:
    character_quick_leave_dissolve = Dissolve(0.25)

###############################################
# Functions #
init 101 python:
    def text_message_icon(self):
        return self.icon()

    Nate.text_message_icon = text_message_icon

    def text_message_icon(self):
        return self.icon()

    Sam.text_message_icon = text_message_icon

    def text_message_icon(self, suffix = ""):
        string = "mods/leftovers_mod/images/interface/" + "Kacey" + "_Face_Icon" + suffix
        string = string + ".png"
        return string

    Gloryhole_Girl.text_message_icon = text_message_icon

    def text_message_icon(self):
        return self.icon()

    Vicky.text_message_icon = text_message_icon

    def icon(self):
        return self.internal_name + " icon"

    Nate.icon = icon

    def icon(self):
        return self.internal_name + " icon"

    Sam.icon = icon

    def icon(self, suffix = ""):
        string = "mods/leftovers_mod/images/interface/" + "Kacey" + "_Face_Icon" + suffix
        string = string + ".png"
        return string

    Gloryhole_Girl.icon = icon

    def icon(self):
        return self.internal_name + " icon"

    Vicky.icon = icon

###############################################
transform character_dialog_icon:
    size (32,32)
    yalign 1.0
    yoffset 3

###############################################
# Backported from IA2 #

# Texting Adjustments #
init offset = 2

define gui.nvl_list_length = None
define config.adv_nvl_transition = None
define config.nvl_adv_transition = None
## ##

define config.nvl_list_length = 999

default phone_current_character = None

define phone_ui_folder = "mods/leftovers_mod/images/interface/phone/"

define phone_send_frame = phone_ui_folder + "phone_send_frame.png"

define phone_dialog_frame_border_left = 23
define phone_dialog_frame_border_top = 23
define phone_dialog_frame_border_right = 23
define phone_dialog_frame_border_bottom = 23

define phone_dialog_standard_frame_image = phone_ui_folder + "phone_received_frame.png"
define phone_light_mode_received_frame_image = phone_dialog_standard_frame_image
define phone_dark_mode_received_frame_image = im.MatrixColor(phone_dialog_standard_frame_image, im.matrix.tint(0.25, 0.25, 0.25))

define phone_light_mode_received_frame = Frame(phone_light_mode_received_frame_image, phone_dialog_frame_border_left, phone_dialog_frame_border_top, phone_dialog_frame_border_right, phone_dialog_frame_border_bottom )
define phone_dark_mode_received_frame = Frame(phone_dark_mode_received_frame_image, phone_dialog_frame_border_left, phone_dialog_frame_border_top, phone_dialog_frame_border_right, phone_dialog_frame_border_bottom )

define phone_send_frame_image = im.MatrixColor(phone_dialog_standard_frame_image, im.matrix.tint(0, 0.51, 1.0))
define phone_send_frame = Frame(phone_send_frame_image, phone_dialog_frame_border_left, phone_dialog_frame_border_top, phone_dialog_frame_border_right, phone_dialog_frame_border_bottom )

define phone_choice_frame_standard_image = phone_dialog_standard_frame_image

define phone_choice_light_mode_frame_image = im.MatrixColor(phone_dialog_standard_frame_image, im.matrix.tint(0.94, 0.94, 0.94))
define phone_choice_dark_mode_frame_image = im.MatrixColor(phone_dialog_standard_frame_image, im.matrix.tint(0.23, 0.23, 0.23))

define phone_choice_light_mode_frame = Frame( phone_choice_light_mode_frame_image, phone_dialog_frame_border_left, phone_dialog_frame_border_top, phone_dialog_frame_border_right, phone_dialog_frame_border_bottom )
define phone_choice_dark_mode_frame = Frame( phone_choice_dark_mode_frame_image, phone_dialog_frame_border_left, phone_dialog_frame_border_top, phone_dialog_frame_border_right, phone_dialog_frame_border_bottom )

define phone_light_mode_text_color = "#000000"
define phone_dark_mode_text_color = "#eeeeee"

define phone_send_icon = phone_ui_folder + "phone_send_icon.png"
define phone_received_icon = phone_ui_folder + "phone_received_icon.png"

define phone_light_mode_background = phone_ui_folder + "phone_background.png"

define phone_foreground = phone_ui_folder + "phone_foreground.png"

define phone_continue = phone_ui_folder + "continue_btn.png"

define phone_message_outlines = [ (absolute(0), "#000", absolute(0), absolute(0)) ]

define phone_top_bar_height = 50
define phone_name_bar_height = 50

define phone_icon_area_width = 107
define phone_icon_area_height = 112

define phone_width = 533
define phone_height = 928

define phone_choice_area_height = 200
define phone_screen_ystart = 50
define phone_screen_yendoffset = 82

define phone_dark_mode_background_color = "#242526"

define phone_dialog_area_top_padding = phone_screen_ystart + phone_top_bar_height + phone_name_bar_height
define phone_dialog_area_padding = (40, phone_dialog_area_top_padding, 40, phone_screen_yendoffset + phone_choice_area_height)
define phone_dialog_area_padding2 = (40, phone_dialog_area_top_padding, 40, phone_screen_yendoffset)

define phone_dialog_area_width = phone_width - (phone_dialog_area_padding[0] * 2)
define phone_dialog_area_hbox_spacing = 10
define phone_message_appear_xoffset = 50
define phone_message_frame_max_width = phone_dialog_area_width - phone_dialog_area_hbox_spacing -  phone_icon_area_width - phone_message_appear_xoffset
define phone_message_padding = (23, 23, 23, 23)
define phone_message_available_space_width = phone_message_frame_max_width - phone_message_padding[0] - phone_message_padding[2]

define phone_xanchor = 0.5
define phone_yanchor = 0.5
define phone_xpos = 0.5
define phone_ypos = 0.5

define phone_standard_insensitive_text_color = gui.insensitive_color

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("mods/leftovers_mod/audio/sounds/phone/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("mods/leftovers_mod/audio/sounds/phone/SendText.ogg")

init offset = 3

transform phone_transform_old:
    xanchor phone_xanchor
    yanchor phone_yanchor 
    xpos phone_xpos
    ypos phone_ypos

transform phone_transform:
    yoffset 0

transform phone_appear_old(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xanchor phone_xanchor
    yanchor phone_yanchor 
    xpos phone_xpos
    ypos phone_ypos

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

define phone_slide_down_anim_time = 0.5
define phone_slide_down_total_pause = phone_slide_down_anim_time + 0.0

transform phone_slide_down: #Used only when the dialogue have one element
    ease 0.5 yoffset 1080 

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0

transform message_appear(pDirection):
    alpha 0.0
    xoffset phone_message_appear_xoffset * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform nvl_choice_appear(pDirection):
    alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

default phone_slide_up = False
default phone_slide_down = False
default nvl_force_hide = False

screen PhoneDialogue(dialogue, items=None):
    if nvl_force_hide:
        # dont show the fucking screen if I dont want it to show
        # I still need to trick the game into thinking the screen is showing text

        for id_d, d in enumerate(dialogue):
            if d.who != None:
                text "":
                    id d.who_id
            text "":
                id d.what_id
    else:
        $ phone_standard_text_color = phone_light_mode_text_color
        $ phone_standard_insensitive_text_color = gui.insensitive_color

    if persistent.dark_mode:
        $ phone_standard_text_color = phone_dark_mode_text_color

    style_prefix "phoneFrame"

    fixed:
        xanchor phone_xanchor
        yanchor phone_yanchor 
        xpos phone_xpos
        ypos phone_ypos

        if phone_slide_up:
            at phone_appear(phone_position_x, phone_position_y)
        elif phone_slide_down:
            at phone_slide_down

        xsize phone_width
        ysize phone_height

        if persistent.dark_mode:
            add Transform(Solid(phone_dark_mode_background_color), xoffset = 18, yoffset = 40, xsize = 500, ysize = 808)
        else:
            add phone_light_mode_background

        vbox:
            spacing 0
            yoffset phone_screen_ystart

            frame:
                padding (phone_dialog_area_padding[0], 10)
                ysize phone_top_bar_height
                background None
                hbox:
                    text "Monday":
                        color phone_standard_text_color
                        outlines phone_message_outlines
                    yalign 0.5
                hbox:
                    xalign 1.0
                    text "69%":
                        color phone_standard_text_color
                        outlines phone_message_outlines
                    yalign 0.5

            frame:
                padding (phone_dialog_area_padding[0], 10)
                ysize phone_name_bar_height
#                background Solid("#00ff00")
                background None

                xfill True
                
                hbox:
                    if phone_current_character is not None:
                        text phone_current_character.say_name:
                            color phone_standard_text_color

                            outlines phone_message_outlines

        frame:
            padding phone_dialog_area_padding2

            background None

            viewport:
                draggable True
                mousewheel True
                yinitial 1.0

                vbox:

                    null height 20
                    use nvl_phonetext(dialogue, items)

                    for i_i, i in enumerate(items): #For each choices...
                        $ nvl_choice_sensitive = choice_enabled(i.caption)
                        button:
                            action i.action
                            sensitive nvl_choice_sensitive
                            frame:
                                if not phone_slide_down:
                                    at message_appear(1 if ((i_i + 1) % 2 == 0) else -1)

                                if persistent.dark_mode:
                                    background phone_choice_dark_mode_frame
                                else:
                                    background phone_choice_light_mode_frame

                                #xmaximum phone_message_frame_max_width
                                xfill True
                                padding (phone_dialog_area_padding[0], 20)

                                text i.caption:
                                    xalign 0.0
                                    yalign 0.5
                                    hover_color gui.button_text_hover_color
                                    outlines phone_message_outlines

                                    color (phone_standard_text_color if nvl_choice_sensitive else phone_standard_insensitive_text_color)

                                    ysize None
                                    min_width None
                                    yoffset None
                                    xsize None

                    #null height 20

        if len(items) <= 0 and False:
            # dummy button that progresses text
            button:
                idle_child Transform(Solid("#000"), alpha = 0.0)
                hover_child Transform(Solid("#000"), alpha = 0.0)

                clicked Return()

                activate_sound None
                hover_sound None
                sensitive not pygame.mouse.get_pressed()[0]

        add phone_foreground 

screen nvl_phonetext(dialogue, items):
    style_prefix None

    if persistent.dark_mode:
        $ phone_dialog_receive_text_color = phone_dark_mode_text_color
    else:
        $ phone_dialog_receive_text_color = phone_light_mode_text_color

    $ previous_d_who = None

    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    id d.what_id
                    if d.current and (items is not None and len(items) == 0):
                        at message_narrator
                    xanchor 0.5
                    xpos 0.5
                    min_width None
                    italic True
        else:
            if d.who == n.say_name:
                $ message_frame = phone_send_frame
            else:
                if persistent.dark_mode:
                    $ message_frame = phone_dark_mode_received_frame
                else:
                    $ message_frame = phone_light_mode_received_frame

            hbox:
                spacing phone_dialog_area_hbox_spacing
                if d.who == n.say_name:
                    xfill True
                
                #If this is the first message of the character, show an icon
                if d.who != n.say_name:
                    if previous_d_who != d.who:
                        if d.who == n.say_name:
                            $ message_icon = phone_send_icon
                        else:
                            $ message_icon = Transform(phone_current_character.text_message_icon(), xsize = 100, ysize = 100)

                        add message_icon:
                            if d.current and (items is not None and len(items) == 0):
                                if not phone_slide_down:
                                    at message_appear_icon()

                    else:
                        null width phone_icon_area_width

                vbox:
                    yalign 1.0
                    if d.who != n.say_name and previous_d_who != d.who:
                        text d.who

                    if d.who == n.say_name:
                        xfill True

                    frame:
                        if d.who == n.say_name:
                            xalign 1.0
                        padding phone_message_padding

                        background Frame(message_frame)

                        if d.who != n.say_name:
                            xmaximum phone_message_frame_max_width

                        if d.current and (items is not None and len(items) == 0):
                            if not phone_slide_down:
                                if d.who == n.say_name:
                                    at message_appear(1)
                                else:
                                    at message_appear(-1)

                        text d.what:
                            xalign 0.0
                            yalign 0.5

                            ysize None
                            min_width None
                            yoffset None
                            xsize None
                            
                            outlines phone_message_outlines

                            slow_cps False

                            id d.what_id

        $ previous_d_who = d.who

init python:
    def nvl_color(tag, argument, contents):
        text_color = "#fff"

        if store.nvl_mode == "phone":
            if persistent.dark_mode:
                text_color = phone_dark_mode_text_color
            else:
                text_color = phone_light_mode_text_color

            return [
                    (renpy.TEXT_TAG, u"color={}".format(text_color)),
                ] + contents + [
                    (renpy.TEXT_TAG, u"/color"),
                ]

        else:
            return contents

    config.custom_text_tags["nvl_color"] = nvl_color

    def nate_nvl_color(tag, argument, contents):
        if store.nvl_mode == "phone":
            text_color = "#e4f2ff"
            return [
                    (renpy.TEXT_TAG, u"color={}".format(text_color)),
                ] + contents + [
                    (renpy.TEXT_TAG, u"/color"),
                ]
        else:
            return contents

    config.custom_text_tags["nate_nvl_color"] = nate_nvl_color
       
style phoneFrame is default

style phoneFrame_viewport:
    yfill True
    xfill True

style phoneFrame_vbox:
    spacing 10
    xfill True


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):
    #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
    if nvl_mode == "phone":
        if len(dialogue) > 0 or (len(dialogue) == 0 and len(items) > 0):
            use PhoneDialogue(dialogue, items)
    else:
        ####
        ## Indent the rest of the screen
        window:
            style "nvl_window"

            has vbox:
                spacing gui.nvl_spacing

            ## Displays dialogue in either a vpgrid or the vbox.
            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True, as it is above.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0

label texting_preparation(texting_character):
    nvl clear
    $ phone_current_character = texting_character
    $ phone_slide_up = True

    window show

    return

label text_finish:
    call texting_hide_phone(hide_window = True)
    return

init python:
    def handle_text_image(data):
        renpy.call("text_image_fullscreen_display", data)
        return True

    config.hyperlink_handlers['text_image_fullscreen_display'] = handle_text_image
 
label text_message_with_image(texting_character, full_image = None, thumb_image = None): 
    $ text_msg = "{{a=text_image_fullscreen_display:{full_image}}}{{image={thumb_image}}}{{/a}}"

    $ text_msg = text_msg.format(full_image = full_image, thumb_image = thumb_image)

    $ texting_character(text_msg)
    return

label text_image_fullscreen_display(text_image_name):
    call screen text_image_fullscreen_display(text_image_name)
    pause
    return

label texting_hide_phone(hide_window = True, clear_nvl = True):
    $ phone_slide_up = False
    $ phone_slide_down = True
    pause phone_slide_down_total_pause

    if clear_nvl:
        nvl clear

    $ nvl_force_hide = True

    if hide_window:
        window hide

    nvl hide
    $ phone_slide_down = False

    if hide_window:
        window auto hide

    $ nvl_force_hide = False
    return

screen text_image_fullscreen_display(txt_fs_image):
    modal True
    zorder 5
    imagebutton idle txt_fs_image action Return(value = None)

##############################
# Defining Characters for Texts #
define nate_nvl = Character("[n.say_name]", kind=nvl, callback=Phone_SendSound, what_prefix = "{nvl_color}", what_suffix = "{/nvl_color}")
define sam_nvl = Character("[sa.say_name]", kind=nvl, callback=Phone_SendSound, what_prefix = "{nvl_color}", what_suffix = "{/nvl_color}")
define kira_nvl = Character("[k.say_name]", kind=nvl, callback=Phone_SendSound, what_prefix = "{nvl_color}", what_suffix = "{/nvl_color}")
define kacey_nvl = Character("[gloryhole_girl.say_name]", kind=nvl, callback=Phone_SendSound, what_prefix = "{nvl_color}", what_suffix = "{/nvl_color}")
define vicky_nvl = Character("[vicky.say_name]", kind=nvl, callback=Phone_SendSound, what_prefix = "{nvl_color}", what_suffix = "{/nvl_color}")

#define anna_nvl = Character("[anna.say_name]", kind=nvl, callback=Phone_SendSound, what_prefix = "{nvl_color}", what_suffix = "{/nvl_color}") # Anna

label play_new_chat:
    play sound new_chat_fn()
    return

label play_phone_ring:
    play sound phone_ring_fn()
    return

init 100 python:
    def new_chat_fn():
        return "mods/leftovers_mod/audio/sounds/phone/ui_menu_button_confirm_02.ogg"

    def phone_ring_fn():
        return "mods/leftovers_mod/audio/sounds/phone/351284__pogmothoin__incoming-call-marimba-ringtone-sound.ogg"

###############
# Emojis #
init 2 python:
    def handle_emoji_name(emoji_name):
        emoji_name = emoji_name.replace(" ", "_")

        if emoji_name in emoji_name_dict:
            emoji_name = emoji_name_dict[emoji_name]

        emoji_name = "emoji_" + emoji_name
        return emoji_name

    for filepath in renpy.list_files():
        if not filepath.lower().endswith(".png") and not filepath.lower().endswith(".jpg"):
            continue

        if filepath.startswith("mods/leftovers_mod/images/interface/phone/emojis"):
            image_name = os.path.basename(filepath)
            image_name = os.path.splitext(image_name)[0]

            image_name = handle_emoji_name(image_name)

            image_d = At(filepath, character_dialog_icon)

            renpy.image(image_name, image_d)

init python:
    def emoji_tag(tag, argument):
        return_tuples = []

        if argument:
            emoji = handle_emoji_name(argument)
        else:
            emoji = handle_emoji_name(tag)

        #return_tuples.append((renpy.TEXT_TEXT, "tag:" + tag + " "))
        return_tuples.append((renpy.TEXT_TEXT, " "))
        return_tuples.append((renpy.TEXT_TAG, "image=" + emoji))
        return_tuples.append((renpy.TEXT_TEXT, " "))
        
        return return_tuples

    config.self_closing_custom_text_tags["emoji"] = emoji_tag

init python:
    emoji_names = [
        ( [ ":(", "🙁" ], "slightly_frowning" ),
        ( [ ":)", "🙂" ], "slightly_smiling" ),
        ( [ "😛", ":P" ], "face_with_tongue" ),
        ( ["🍑"], "peach" ),
        ( [ "grinning_face", ":D", "😀" ], "grinning" ),
        ( [ "😱" ], "face_screaming" ),
        ( [ "man_shrugging️" ], "man_shrugging" ),
        ( [ "woman_facepalming" ], "woman_facepalming" ),
        ( [ "🤏" ], "pinching_hand" ),

        ( ["👀"], "eyes" ),
        ( ["🤔"], "thinking" ),
        ( ["🎉"], "party_popper" ),
        ( ["🎸"], "guitar" ),
        ( [ "😂" ], "face_with_tears_of_joy" ),
        ( [ "🤯" ], "exploding_head" ),
        ( ["😆"], "grinning_squinting_face" ),
        ( ["😅"], "grinning_face_with_sweat" ),
        ( ["🤔"], "thinking" ),
        ( ["😯"], "hushed_face" ),
        ( ["💩"], "pile_of_poo" ),
        ( ["🔨"], "hammer" ),
        ( ["🎵"], "musical_note" ),
        ( ["😑"], "expressionless_face" ),
        ( ["😃"], "grinning_face_with_big_eyes" ),
        ( ["☺️"], "smiling_face_with_smiling_eyes" ),

        ( ["🍆"], "eggplant" ),
        ( ["🥵"], "hot_face" ),
        ( ["😍"], "smiling_face_with_heart-eyes" ),

        ( ["👍"], "thumbs_up" ),
        ( ["😜"], "winking_face_with_tongue" ),
        ( ["💯"], "hundred_points" ),
        ( ["🙄"], "face_with_rolling_eyes" ),
        ( ["👋"], "waving_hand" ),
        ( ["😲"], "astonished_face" ),

        ( ["😕"], "confused" ),

        ( ["😠"], "angry_face" ),
        ( ["😣"], "persevering_face" ),
        ( ["😏"], "smirking" ),
        ( ["🤣"], "rolling_on_the_floor_laughing" ),
        ( ["😉"], "wink" ),
        ( [ "❤️" ], "red_heart" ),
    ]

    emoji_name_dict = {}

    for emoji_name_tuple in emoji_names:
        if emoji_name_tuple[1] not in emoji_name_tuple[0]:
            emoji_name_tuple[0].append(emoji_name_tuple[1])

        for emoji_name in emoji_name_tuple[0]:
            config.self_closing_custom_text_tags[emoji_name] = emoji_tag
            emoji_name_dict[emoji_name] = emoji_name_tuple[1]


