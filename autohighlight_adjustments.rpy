# Auto Highlight Adjustments #
# Wires up SoDaRa's 01auto-highlight.rpy to work with IA1's bust system.
#
# 01auto-highlight expects ONE sprite per character with the sprite_highlight transform applied to it.
# IA1 instead splits busts into separate image tags (base/face/blush/mouth/glasses/hat/overlays).
# When I tried to dim each piece individually, the face would visibly drift away from the body.
#
# Tried two different approaches to the dimming:
#   1. Combine the pieces into one custom Displayable, then apply sprite_highlight as a transform
#      Looked clean on paper. Didn't work in practice - the matrixcolor from a transform doesn't
#      reach into a hand-built Render the way it does with normal image displayables.
#   2. Combine the pieces into one custom Displayable, but apply the dim INSIDE the render method
#      using im.MatrixColor on each piece. Less elegant but it actually works.
#
# Going with approach 2. The library is still doing the real work - tracking speaking_char,
# providing the callback, telling us who's talking - we just have to handle the actual color
# matrix application ourselves since the transform path doesn't survive the custom Render.


# Settings #
default encore_auto_highlight_enabled = True

# 1.0 = full color, 0.0 = grayscale
default encore_auto_highlight_dim_saturation = 0.45

# 0.0 = normal, negative = darker
default encore_auto_highlight_dim_brightness = -0.18

# default encore_auto_highlight_dim_brightness = -0.25  # tried this first, too dark on edna's lighter pieces

init 999 python:
    # The Combined Bust #
    # The whole reason this file is even necessary.
    # Stacks every piece of the bust into one Displayable at (0,0) so the face stays attached to the body.
    # The dim has to be applied to each piece here, since a transform's matrixcolor doesn't penetrate
    # into the custom Render we're building.
    class Encore_Auto_Highlight_Bust(renpy.Displayable):
        def __init__(self, char):
            renpy.Displayable.__init__(self)
            self.char = char

        def piece_names(self):
            # order matters. some characters draw face under base, some over.
            # swap the order and you get a horror-show clipped face
            char = self.char
            pieces = []

            if not char.show_face_under_base():
                pieces.append(char.base_image_filename())
                pieces.append(char.blush_image_filename())
                pieces.append(char.face_image_filename())
            else:
                pieces.append(char.face_image_filename())
                pieces.append(char.blush_image_filename())
                pieces.append(char.base_image_filename())

            # optional pieces, not every character has them
            if char.has_separate_mouth():
                pieces.append(char.mouth_image_filename())

            if char.has_separate_glasses():
                pieces.append(char.glasses_image_filename())

            if char.has_separate_hat():
                pieces.append(char.hat_image_filename())

            # overlays = stuff the game adds on top (sweat, tears, etc.)
            for overlay_name in char.overlays:
                pieces.append(char.overlay_image_filename(overlay_name))

            return pieces

        def piece_displayable(self, image_name):
            # wrap each piece with the dim matrix if this character isn't speaking
            # has to happen here on the displayable itself - a parent transform won't propagate
            # matrixcolor down into our custom render
            piece = renpy.displayable(image_name)

            if encore_auto_highlight_should_dim(self.char):
                piece = im.MatrixColor(piece, encore_auto_highlight_matrixcolor())

            return piece

        def render(self, width, height, st, at):
            # draw the first piece, then stack the rest on top
            pieces = self.piece_names()
            first_piece = self.piece_displayable(pieces[0])
            first_render = renpy.render(first_piece, width, height, st, at)

            main_render = renpy.Render(first_render.width, first_render.height)
            main_render.blit(first_render, (0, 0), False)

            for image_name in pieces[1:]:
                piece = self.piece_displayable(image_name)
                piece_render = renpy.render(piece, width, height, st, at)
                main_render.blit(piece_render, (0, 0), False)

            return main_render


    # Dim Check #
    # reads 01auto-highlight's speaking_char to decide if this character is dimmed
    # the list form is so short tags like "n" don't substring-match into longer ones like "janet"
    def encore_auto_highlight_should_dim(char):
        if not store.encore_auto_highlight_enabled:
            return False

        if store.speaking_char is None:
            return False

        if isinstance(store.speaking_char, list):
            return char.tag() not in store.speaking_char

        return store.speaking_char != char.tag()


    # builds the tint matrix - saturation removes color, brightness darkens
    def encore_auto_highlight_matrixcolor():
        return im.matrix.saturation(store.encore_auto_highlight_dim_saturation) * im.matrix.brightness(store.encore_auto_highlight_dim_brightness)


    # Dialogue Callback #
    # 01auto-highlight uses name_callback to update speaking_char when a line begins.
    # We wrap it in a callable class so we can also:
    #   a) feed it the char's tag automatically (no need to set cb_name on every Character() definition)
    #   b) refresh the other visible busts so their dim state updates
    #   c) raise the speaker's z-order so they pop to the front
    class Encore_Auto_Highlight_Callback(object):
        def __init__(self, char):
            self.char = char

        def __call__(self, event, interact=True, **kwargs):
            if not interact:
                return

            if not store.encore_auto_highlight_enabled:
                return

            if event == "begin":
                # delegate to 01auto-highlight - this is what actually flips speaking_char
                name_callback("begin", name=[self.char.tag()])

                # re-render the other busts so their dim updates to match the new speaker
                # (we have to do this manually since the dim is baked into each bust's render)
                encore_auto_highlight_refresh_visible_characters()

                # bring the speaker's bust to the front
                encore_auto_highlight_raise_character(self.char)


    # Refresh Visible Busts #
    # when the speaker changes, every visible bust needs to re-render so the new dim state takes effect
    # process_character already redraws the speaker, so this only has to redo the others
    def encore_auto_highlight_refresh_visible_characters():
        for char in encore_auto_highlight_character_list():
            if char.variable_name not in store.characters_shown:
                continue
            # skip the speaker themselves - process_character already drew them.
            # without this we get a second render on top of the first, which shows
            # as a double-bust artifact (was hitting nate hardest)
            if isinstance(store.speaking_char, list) and char.tag() in store.speaking_char:
                continue
            refresh_character(char, force_no_dissolve=True)


    # Z-Order Raising #
    # combined bust lives under base_tag, so raise that tag when the character starts talking
    def encore_auto_highlight_raise_character(char):
        layer = character_layer()
        shown_tags = renpy.get_showing_tags(layer=layer)
        bust_tag = char.tag() + "_auto_highlight_bust"

        if bust_tag in shown_tags:
            renpy.change_zorder(layer, bust_tag, 3)


    # Character List #
    # have to wait for player_character to exist before character_list() works.
    # nate2/nate3/debug_character aren't always in the normal list so they get appended after.
    # had a bug where nate2 wouldn't dim during the dream sequence - this fixed it.
    def encore_auto_highlight_character_list():
        chars = []
        player_character = store.__dict__.get("player_character", None)
        nate2 = store.__dict__.get("nate2", None)
        nate3 = store.__dict__.get("nate3", None)
        debug_character = store.__dict__.get("debug_character", None)

        if player_character:
            chars = character_list()

        if nate2 and nate2 not in chars:
            chars.append(nate2)

        if nate3 and nate3 not in chars:
            chars.append(nate3)

        if debug_character and debug_character not in chars:
            chars.append(debug_character)

        return chars


    # Character Setup #
    # replaces IA_Actor.create_renpy_characters so the speaking objects get our callback
    # c = regular say name, c_full = the full name version some scenes use
    def encore_auto_highlight_create_renpy_characters(self):
        self.update_color()

        self.c = DynamicCharacter(
            self.variable_name + ".say_name",
            color=self.color,
            callback=Encore_Auto_Highlight_Callback(self)
        )
        self.c.actor = self

        self.c_full = DynamicCharacter(
            self.variable_name + ".full_name",
            color=self.color,
            callback=Encore_Auto_Highlight_Callback(self)
        )
        self.c_full.actor = self


    # rebuild for old saves - their stored character objects were made before our callback existed
    def encore_auto_highlight_rebuild_character_speakers():
        for char in encore_auto_highlight_character_list():
            char.create_renpy_characters()


    # Hide The Old Pieces #
    # once the combined bust is showing under base_tag, the original split pieces have to be hidden.
    # if you leave them visible they sit on top of the combined bust and the face detaches all over again.
    # second time I had to fix the detached face problem lol
    def encore_auto_highlight_hide_old_piece_tags(char, layer):
        renpy.hide(char.base_tag(), layer) 
        renpy.hide(char.face_tag(), layer)
        renpy.hide(char.blush_tag(), layer)

        if char.has_separate_mouth():
            renpy.hide(char.mouth_tag(), layer)

        renpy.hide(char.glasses_tag(), layer)
        renpy.hide(char.hat_tag(), layer)

        for overlay_image_name in char.displayed_overlay_filenames:
            renpy.hide(overlay_image_name, layer)

        char.reset_displayed_overlay_filenames()


    # Show The Combined Bust #
    # hide old split pieces, then show the combined Displayable under base_tag.
    # no extra transform needed - the dim is handled inside Encore_Auto_Highlight_Bust.render()
    def encore_auto_highlight_show_bust(char, transform_array, layer):
        encore_auto_highlight_hide_old_piece_tags(char, layer)

        bust_name = char.tag() + "_auto_highlight_bust"
        renpy.show(
            bust_name,
            transform_array,
            layer,
            Encore_Auto_Highlight_Bust(char),
            0,
            bust_name   # was char.base_tag() - use stable name as tag instead
        )


    # process_character Hook #
    # two dialogue styles in IA1:
    #   old: call process_character(janet, appearance="...", text="...")
    #   new: call process_character(janet, appearance="...")  then  janet.c "..."
    # we update the speaker whenever there's an appearance change with a bust - that covers both styles.
    # doing it only on text would leave the bust rendering with stale dim during the split-call style
    # (which is what was breaking kacey/vicky since they use the split style heavily)
    def process_character_replace_utility(char, appearance="", text="", show_bust=True, replace=False):
        if replace and store.last_character_that_appeared and store.last_character_that_appeared != char.variable_name:
            character_leave_dissolve(eval(store.last_character_that_appeared))

        if appearance and show_bust:
            store.last_character_that_appeared = char.variable_name

        # set the speaker BEFORE we render the bust so it appears in the right state from frame 1
        if appearance and show_bust and store.encore_auto_highlight_enabled:
            name_callback("begin", name=[char.tag()])

        process_character(char, appearance, show_bust=show_bust)

        # refresh the others (process_character already redrew the speaker) and raise on top
        if appearance and show_bust and store.encore_auto_highlight_enabled:
            encore_auto_highlight_refresh_visible_characters()
            encore_auto_highlight_raise_character(char)

        if text:
            store.last_say_position = char.position
            char.c(text)


    # Cleanup #
    # make sure speaking_char doesn't get stuck pointing at someone who's no longer on screen
    def clear_characters(dissolve=None):
        store.characters_shown = set()
        name_callback("begin", name=None)
        renpy.scene(character_layer())

        if dissolve:
            renpy.with_statement(dissolve)


    def character_leave_dissolve(char):
        char_layer = character_layer()

        # if the leaver was the speaker, clear it so nobody stays "talking" while invisible
        if store.speaking_char == [char.tag()]:
            name_callback("begin", name=None)

        renpy.hide(char.base_tag(), char_layer)
        renpy.hide(char.face_tag(), char_layer)
        renpy.hide(char.blush_tag(), char_layer)

        if char.has_separate_mouth():
            renpy.hide(char.mouth_tag(), char_layer)

        renpy.hide(char.glasses_tag(), char_layer)
        renpy.hide(char.hat_tag(), char_layer)

        for overlay_image_name in char.displayed_overlay_filenames:
            renpy.hide(overlay_image_name, char_layer)

        renpy.with_statement(character_leave_dissolve_speed)
        store.characters_shown.discard(char.variable_name)


    # Position Values #
    # giant if/elif chain mirroring how IA's refresh_character does positioning.
    # kept this way on purpose so when something looks wrong I can compare directly to the base game.
    # TODO eventually convert this to a dict lookup, but not worth the refactor right now
    def encore_auto_highlight_position_values(char):
        position = char.position
        y_pos = char.ypos_adjustment()

        x_scale = -1.0
        x_align = 0.0
        x_destination = -1.0

        if position == "left":
            x_scale = -1.0
            x_align = 0.0
            x_destination = -1.0
        elif position == "left_mirror":
            x_scale = 1.0
            x_align = 0.0
            x_destination = -1.0
        elif position == "right":
            x_scale = 1.0
            x_align = 1.0
            x_destination = 2.0
        elif position == "right_mirror":
            x_scale = -1.0
            x_align = 1.0
            x_destination = 2.0
        elif position == "center":
            x_scale = store.center_position_xscale
            x_align = 0.5
            x_destination = -1.0
        elif position == "janet_special":
            x_scale = -1.0
            x_align = 0.81
            x_destination = 2.0
            y_pos = 545
        elif position == "edna_special":
            x_scale = -1.0
            x_align = 0.88
            x_destination = 2.0
            y_pos = 520
        elif position == "edna_special2":
            x_scale = -1.0
            x_align = 0.87
            x_destination = 2.0
        elif position == "edna_special3":
            x_scale = -1.0
            x_align = 1.0
            x_destination = 2.0
            y_pos = 520
        elif position == "nate_more_right":
            x_scale = 1.0
            x_align = 1.12
            x_destination = 2.0
        elif position == "nate2_special":
            x_scale = -1.0
            x_align = -0.16
            x_destination = -1.0
        elif position == "nate3_special":
            x_scale = -1.0
            x_align = -0.03
            x_destination = -1.0
        elif position == "sam_dream_special":
            x_scale = -1.0
            x_align = 0.1
            x_destination = -1.0
        elif position == "nate_simone_tit_level_nate":
            x_scale = 1.0
            x_align = 0.15
            x_destination = -1.0
            y_pos = 100
        elif position == "nate_simone_tit_level_simone":
            x_scale = -1.0
            x_align = -0.1
            x_destination = -1.0
        elif position == "nate_edna_pussy_level_edna":
            x_scale = -1.0
            x_align = -0.08
            x_destination = -1.0
        elif position == "nate_edna_pussy_level_nate":
            x_scale = 1.0
            x_align = 0.11
            x_destination = -1.0
            y_pos = 340
        elif position == "julia_sam_threesome_closer_sam":
            x_scale = -1.0
            x_align = 0.83
            x_destination = 2.0
        elif position == "julia_sam_threesome_closer_julia":
            x_scale = -1.0
            x_align = 0.67
            x_destination = 2.0
        elif position == "three_person_left_2":
            x_scale = -1.0
            x_align = 0.3
        elif position == "three_person_left_3":
            x_scale = -1.0
            x_align = 0.6

        return x_align, x_scale, y_pos, x_destination


    # places the bust where it belongs and adds a move transform if entering/leaving
    def encore_auto_highlight_transform_array(char, off_screen, on_screen):
        x_align, x_scale, y_pos, x_destination = encore_auto_highlight_position_values(char)

        transform_array = [
            Transform(
                xalign=x_align,
                xzoom=x_scale,
                ypos=y_pos,
                yzoom=1.0
            )
        ]

        if off_screen:
            transform_array.append(Move((x_align, 0.0), (x_destination, 0.0), character_slide_speed))

        if on_screen:
            transform_array.append(Move((x_destination, 0.0), (x_align, 0.0), character_slide_speed))

        return transform_array


    # refresh_character Replacement #
    # the base game version shows separate base/face/blush tags - this version shows the combined bust.
    # same position logic as the original.
    def refresh_character(char, off_screen=False, on_screen=False, force_no_dissolve=False, force_transition=None):
        if wholesome_mode:
            return

        if no_bust_art:
            return

        transition = force_transition if force_transition else character_dissolve

        if not off_screen:
            store.characters_shown.add(char.variable_name)

        transform_array = encore_auto_highlight_transform_array(char, off_screen, on_screen)
        encore_auto_highlight_show_bust(char, transform_array, character_layer())

        if not force_no_dissolve:
            renpy.with_statement(transition)

        if persistent.sfw_mode:
            renpy.show_screen("sfw_mode_character_display")
        else:
            renpy.hide_screen("sfw_mode_character_display")


    # hook it all up
    IA_Actor.create_renpy_characters = encore_auto_highlight_create_renpy_characters

    # rebuild on new game AND on load - older saves don't have the callback yet
    config.start_callbacks.append(encore_auto_highlight_rebuild_character_speakers)
    config.after_load_callbacks.append(encore_auto_highlight_rebuild_character_speakers)
