default now_playing_text = ""

init python:
    def reset_volume():
        preferences.set_volume('music', config.default_music_volume)
        preferences.set_volume('sfx', config.default_sfx_volume)
        preferences.set_volume('voice', config.default_voice_volume)
        return

    def get_redirected_track(filename):
        if persistent.side_story_enabled:
            return music_redirects.get(filename, filename)
        return filename

init 200 python:
    import os
    def play_music(name, channel='music', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False, considered_queue=False):
        name = get_redirected_track(name)

        if not considered_queue:
            store.music_is_queued = False

        renpy.music.play(name, channel=channel, loop=loop, fadeout=fadeout,
                         synchro_start=synchro_start, fadein=fadein,
                         tight=tight, if_changed=if_changed)

        if considered_queue and name:
            store.current_queued_music = name
            renpy.store.now_playing_text = "Now Playing: " + os.path.basename(name)

init 201 python:
    config.overlay_screens.append("now_playing_overlay")

screen now_playing_overlay():
    if now_playing_text:
        text now_playing_text:
            size 36
            xalign 1.0
            yalign 1.0
            xoffset -20
            yoffset -100  # Raised higher up from the bottom
            color "#FFFFFFE0"  # More opaque white
            outlines [ (2, "#000000") ]  # Stronger outline for readability

####################################################################
init 101 python:
# Updates the Reset Volume Function #
    def reset_volume():
        preferences.set_volume('music', config.default_music_volume)
        preferences.set_volume('sfx', config.default_sfx_volume)
        preferences.set_volume('voice', config.default_voice_volume)
        preferences.set_volume('message', default_message_volume)
        preferences.set_volume('chat', default_chat_volume)
        return

# Message Clicks # 
default persistent.set_default_message_volume = False

screen preferences_pref_bar(pref_bar_label, pref_bar_value, pref_bar_display, pref_bar_range = None):
    label _(pref_bar_label)

    hbox:
        if pref_bar_range is None:
            bar value pref_bar_value thumb_offset 0
        else:
            bar value pref_bar_value thumb_offset 0 range pref_bar_range
        text str(pref_bar_display)

screen preferences_volume_bar(volume_title, volume_channel, volume_change_string, pref_bar_range = None):
    use preferences_pref_bar(
        volume_title, 
        MixerValueRangeEditable(volume_channel, (1.0 if pref_bar_range is None else pref_bar_range)),
        "{num}%".format(num = str( int ( round ( preferences.volumes[volume_channel], 2 ) * 100 ) ) ),
        pref_bar_range = pref_bar_range
        )

init python:
    class MixerValueRangeEditable(MixerValue):
        def __init__(self, mixer, max_range):
            self.mixer = mixer
            self.max_range = max_range

        def get_adjustment(self):
            return ui.adjustment(
                range=self.max_range,
                value=_preferences.get_volume(self.mixer),
                changed=self.set_mixer)

screen preferences_default_channels_volume_bar(volume_title, volume_channel, pref_bar_range = None):
    use preferences_volume_bar(volume_title, volume_channel, "{channel} volume", pref_bar_range = pref_bar_range)

screen preferences_custom_channels_volume_bar(volume_title, volume_channel):
    use preferences_volume_bar(volume_title, volume_channel, "mixer {channel} volume")

init python:
    ic_hover_sound = "mods/leftovers_mod/audio/sounds/rollover.ogg"
    
    style.image_button.hover_sound = ic_hover_sound
    style.button.hover_sound = ic_hover_sound
    style.imagemap.hover_sound = ic_hover_sound
    style.choice_button.hover_sound = ic_hover_sound
    style.quick_button.hover_sound = ic_hover_sound

    ic_click_sound = "mods/leftovers_mod/audio/sounds/click.ogg"
    
    style.image_button.activate_sound = ic_click_sound
    style.button.activate_sound = ic_click_sound
    style.imagemap.activate_sound = ic_click_sound
    style.choice_button.activate_sound = ic_click_sound
    style.quick_button.activate_sound = ic_click_sound

init python:
    renpy.music.register_channel("message", "message", loop = False, tight = True)

    default_message_volume = 0.64
    if not persistent.set_default_message_volume:
        preferences.volumes['message'] = default_message_volume
        persistent.set_default_message_volume = True

init 100 python:
    def character_callback_sound(event, interact = True, **kwargs):
        if event == "end" and not renpy.get_screen("choice") and interact:
            renpy.music.play("mods/leftovers_mod/audio/sounds/ui_button_simple_click_07.ogg", channel="message")
        return

    config.all_character_callbacks.append(character_callback_sound)

##############################################################################
# Bleeps #

default persistent.set_default_chat_volume = False

init python:
    renpy.music.register_channel("chat", "chat", loop = True)

    default_chat_volume = 0.50
    if not persistent.set_default_chat_volume:
        preferences.volumes['chat'] = default_chat_volume
        persistent.set_default_chat_volume = True

#########
# Original code: https://github.com/bamboocalc/continuous-text-sounds/blob/main/randomized_text_sound_example.rpy #
    # This function makes the continuous text sounds
    def text_sounds(event, sound_path, interact=True, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 1
            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialog block
                randosound = renpy.random.randint(1, 11) # This generates a random number between 1 and 11 inclusive. Change this based on how many sound files you have
 #               renpy.sound.queue("mods/leftovers_mod/audio/sounds/nate_bleep.ogg", channel="chat", loop=False)
                renpy.sound.queue(sound_path, channel="chat", loop=False)
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="chat")
#########

# Old method but caused the bleep sounds to loop infinitely after right-clicking and the text wasn't completed
#init 100 python:
 #   def bleep_common(event, sound_path, interact = True, **kwargs):
  #      if event == "show":
   #         if not renpy.music.is_playing(channel="chat"):
    #            renpy.music.play(sound_path, channel="chat")
     #   elif event == "slow_done" or event == "end" and not renpy.get_screen("choice") and interact:
      #      renpy.music.stop(channel="chat", fadeout=1)

# Bleeps for Each Character #
    def nate_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/nate_bleep.ogg", **kwargs)
        return

    def kira_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/kira_bleep.ogg", **kwargs)
        return

    def simone_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/simone_bleep.ogg", **kwargs)
        return

    def sam_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/sam_bleep.ogg", **kwargs)
        return

    def julia_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/julia_bleep.ogg", **kwargs)
        return

    def janet_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/janet_bleep.ogg", **kwargs)
        return

    def edna_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/edna_bleep.ogg", **kwargs)
        return

    def kacey_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/kacey_bleep.ogg", **kwargs)
        return

    def vicky_bleep(event, interact, **kwargs):
        text_sounds(event, interact=interact, sound_path="mods/leftovers_mod/audio/sounds/bleeps/vicky_bleep.ogg", **kwargs)
        return

##################

# DrX - Ensuring it works with "x.c" tag
init 2 python:
    # after the .c (renpy character) variable is made for the character, define its callback
    
    old_nate_create_renpy_characters = Nate.create_renpy_characters

    def new_nate_create_renpy_characters(self):
        old_nate_create_renpy_characters(self)

        self.c.display_args["callback"] = nate_bleep

        return

    Nate.create_renpy_characters = new_nate_create_renpy_characters

# Kira #
    old_kira_create_renpy_characters = Kira.create_renpy_characters

    def new_kira_create_renpy_characters(self):
        old_kira_create_renpy_characters(self)

        self.c.display_args["callback"] = kira_bleep

        return

    Kira.create_renpy_characters = new_kira_create_renpy_characters

# Simone #
    old_simone_create_renpy_characters = Simone.create_renpy_characters

    def new_simone_create_renpy_characters(self):
        old_simone_create_renpy_characters(self)

        self.c.display_args["callback"] = simone_bleep

        return

    Simone.create_renpy_characters = new_simone_create_renpy_characters

# Sam #
    old_sam_create_renpy_characters = Sam.create_renpy_characters

    def new_sam_create_renpy_characters(self):
        old_sam_create_renpy_characters(self)

        self.c.display_args["callback"] = sam_bleep

        return

    Sam.create_renpy_characters = new_sam_create_renpy_characters

# Julia #
    old_julia_create_renpy_characters = Julia.create_renpy_characters

    def new_julia_create_renpy_characters(self):
        old_julia_create_renpy_characters(self)

        self.c.display_args["callback"] = julia_bleep

        return

    Julia.create_renpy_characters = new_julia_create_renpy_characters

# Janet #
    old_janet_create_renpy_characters = Janet.create_renpy_characters

    def new_janet_create_renpy_characters(self):
        old_janet_create_renpy_characters(self)

        self.c.display_args["callback"] = janet_bleep

        return

    Janet.create_renpy_characters = new_janet_create_renpy_characters

# Edna #
    old_edna_create_renpy_characters = Edna.create_renpy_characters

    def new_edna_create_renpy_characters(self):
        old_edna_create_renpy_characters(self)

        self.c.display_args["callback"] = edna_bleep

        return

    Edna.create_renpy_characters = new_edna_create_renpy_characters

# Kacey #
    old_kacey_create_renpy_characters = Gloryhole_Girl.create_renpy_characters

    def new_kacey_create_renpy_characters(self):
        old_kacey_create_renpy_characters(self)

        self.c.display_args["callback"] = kacey_bleep

        return

    Gloryhole_Girl.create_renpy_characters = new_kacey_create_renpy_characters

# Vicky #
    old_vicky_create_renpy_characters = Vicky.create_renpy_characters

    def new_vicky_create_renpy_characters(self):
        old_vicky_create_renpy_characters(self)

        self.c.display_args["callback"] = vicky_bleep

        return

    Vicky.create_renpy_characters = new_vicky_create_renpy_characters

########################################################################################
# DrX - have it work for saves created before this mod was made #
    leftovers_old_after_load_special = after_load_setup_special

    def after_load_setup_special():
        leftovers_old_after_load_special()

    # Nate # 
        if store.n.c.display_args["callback"] == None:
            store.n.c.display_args["callback"] = nate_bleep
    # Kira #
        if store.k.c.display_args["callback"] == None:
            store.k.c.display_args["callback"] = kira_bleep
    # Simone #
        if store.si.c.display_args["callback"] == None:
            store.si.c.display_args["callback"] = simone_bleep
    # Sam #
        if store.sa.c.display_args["callback"] == None:
            store.sa.c.display_args["callback"] = sam_bleep
    # Julia #
        if store.julia.c.display_args["callback"] == None:
            store.julia.c.display_args["callback"] = julia_bleep
    # Janet #
        if store.janet.c.display_args["callback"] == None:
            store.janet.c.display_args["callback"] = janet_bleep
    # Edna #
        if store.edna.c.display_args["callback"] == None:
            store.edna.c.display_args["callback"] = edna_bleep
    # Kacey #
        if store.gloryhole_girl.c.display_args["callback"] == None:
            store.gloryhole_girl.c.display_args["callback"] = kacey_bleep
    # Vicky #
        if store.vicky.c.display_args["callback"] == None:
            store.vicky.c.display_args["callback"] = vicky_bleep

        return

########################################################################################
## Additional Preferences ##
screen audio_preferences():
    vbox:
        use preferences_default_channels_volume_bar("Music Volume", "music")
        use preferences_default_channels_volume_bar("Sound Volume", "sfx")
        use preferences_custom_channels_volume_bar("Message Click Volume", "message")
        use preferences_custom_channels_volume_bar("Dialogue Bleep Volume", "chat")

        if config.has_music or config.has_sound or config.has_voice:
            null height gui.pref_spacing

            textbutton _("Reset Volume"):
                action Function(reset_volume)
                style "mute_all_button"

            textbutton _("Mute All"):
                action Preference("all mute", "toggle")
                style "mute_all_button"

########################################################################################