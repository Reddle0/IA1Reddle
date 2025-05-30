## Kacey's Apartment ##
default kacey_apartment = Kacey_Apartment()
default had_kacey_apartment_intro = False
default kacey_apartment_visited = False

init 100 python:
    class Kacey_Apartment(Outside_Location):
        def name(self):
            return "[gloryhole_girl.say_name]'s Apartment"

        def internal_name(self):
            return "kacey_apartment"

        def button_image_filename_full_path(self):
            return "mods/leftovers_mod/images/buttons/navigation_kacey_apartment.png"

    leftovers_mod_kacey_old_outside_locations = Outside.base_locations

    def kacey_add_apartment_to_outside(self):
        locations = leftovers_mod_kacey_old_outside_locations(self)
        if store.had_kacey_apartment_intro:
            locations.append(kacey_apartment)
        return locations

    Outside.base_locations = kacey_add_apartment_to_outside

    leftovers_mod_kacey_old_location_list = location_list

    def kacey_add_apartment_to_location_list():
        locations = leftovers_mod_kacey_old_location_list()
        if store.had_kacey_apartment_intro:
            locations.append(kacey_apartment)
        return locations

    location_list = kacey_add_apartment_to_location_list

## Vicky's Apartment ##
default had_vicky_apartment_intro = False

# Kacey Apartment Trigger #
# drx method to start at nate's room, commented out (it worked great, but for consistency sake i opted to instead use the method below of overriding day_start_after_location_reset #
#init 2 python:
#    leftovers_mod_nate_room_start_old = Nate_Room.start

#    def leftovers_mod_nate_room_start_kacey_apartment_intro(self, force_music_change = False, morning_wake_lines = False, force_no_music_change = False):
#        if store.week.time == "day" and not store.had_kacey_apartment_intro and "gloryhole_scene_stall" in scenes_completed and week.days_passed > 21:
#            store.stats.current_location = self
#            store.stats.current_zone = self.zone()
#            renpy.call("kacey_apartment_intro")
#            return

#        leftovers_mod_nate_room_start_old(self, force_music_change = force_music_change, morning_wake_lines = morning_wake_lines, force_no_music_change = force_no_music_change)
#        return

#    Nate_Room.start = leftovers_mod_nate_room_start_kacey_apartment_intro

# Override #
init 300 python:
    config.label_overrides["day_start_after_location_reset"] = "day_start_after_location_reset_leftovers"

label day_start_after_location_reset_leftovers:
    if not had_julia_pre_arrival_scene and week.weeks_passed > 0:
        jump julia_pre_arrival

    if not had_edna_pre_arrival_scene and had_janet_intro_scene and week.days_passed >= 14:
        jump edna_pre_arrival_scene

    if minigame_typing_times_succeeded > 0 and not had_vicky_pre_intro_scene:
        jump vicky_pre_intro

    if minigame_typing_times_succeeded >= 3 and had_vicky_pre_intro_scene and not had_vicky_intro_scene:
        jump vicky_intro

    if store.week.time == "day" and not store.had_kacey_apartment_intro and "gloryhole_scene_stall" in scenes_completed and week.days_passed > 21:
        jump kacey_apartment_intro

    if week.is_school_day():
        call school_morning_start_wakeup

    else:
        show screen hud
        $ advance_time_return_location.start(force_music_change = True, morning_wake_lines = True)

    return

## Kacey/Vicky Hover BG Change park background stuff ##
init 100 python:
    leftovers_park_location_select_background_old = Park.location_select_background

    def leftovers_park_location_select_background_new(self):
       # if the only character at the park is kacey (very likely)
        if len(self.characters) == 1 and store.gloryhole_girl in self.characters:
            return "bg public_bathroom_evening"
        return leftovers_park_location_select_background_old(self)

    Park.location_select_background = leftovers_park_location_select_background_new

    leftovers_vickys_apartment_location_select_background_old = Vicky_Apartment.location_select_background

    def leftovers_vickys_apartment_location_select_background_new(self):
       # if the only character at the apartment is vicky (very likely)
        if len(self.characters) == 1 and store.vicky in self.characters:
            if store.week.time == "day":
                return "bg apartment_daytime"
            else:
                return "bg apartment_evening"

        return leftovers_vickys_apartment_location_select_background_old(self)

    Vicky_Apartment.location_select_background = leftovers_vickys_apartment_location_select_background_new

# Adding (New!) to Mod Locations #
init 100 python:
    leftovers_mod_location_button_render_old = LocationButton.render

    def leftovers_mod_exclamation_mark_render(self, width, height, st, at):
        render = leftovers_mod_location_button_render_old(self, width, height, st, at)

        if self.location == store.kacey_apartment and not self.is_focused():
            if store.had_kacey_apartment_intro and not "kacey_scene_minigame_intro" in store.scenes_completed:
                text = exclamation_mark_scene_transform("New!", int(render.width), xalign = 0.5, yalign = 0.5)
                render.place(text, x = 0, y = 0)

        return render

    LocationButton.render = leftovers_mod_exclamation_mark_render
